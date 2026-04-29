import requests
import pandas as pd
from brvmfinance.const import (
    _BASE_URL_,
    _SIKA_MAPPING_,
    _PRICE_COLNAMES_,
    MAX_DAILY_LENGTH,
)
from brvmfinance.utils.client_http import get_header, get_faux_guid


class SikaAPIError(Exception):
    """Erreur levée quand l'API Sika Finance ne répond pas correctement."""
    pass


def fetch_history(symbole: str, length: int = 365) -> pd.DataFrame | None:
    """
    Récupère l'historique EOD d'un titre via Sika Finance.

    Parameters
    ----------
    symbole : str
        Ticker BRVM, ex: 'SNTS.SN'
    length : int
        Nombre de points à récupérer (max journalier fiable : 365)

    Returns
    -------
    pd.DataFrame | None
        DataFrame indexé par Date, ou None si échec.

    Raises
    ------
    ValueError
        Si le symbole est vide.
    """
    if not symbole or not symbole.strip():
        raise ValueError("Le symbole ne peut pas être vide.")

    s = symbole.strip().upper()

    if length > MAX_DAILY_LENGTH:
        print(
            f"  {s} : length={length} dépasse {MAX_DAILY_LENGTH}. "
            f"L'API va compresser en hebdomadaire. "
            f"Utilisez length≤{MAX_DAILY_LENGTH} pour du journalier."
        )

    params = {
        "symbol": s,
        "length": length,
        "period": "0",
        "guid": get_faux_guid(),
    }

    try:
        response = requests.get(
            _BASE_URL_,
            params=params,
            headers=get_header(),
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.Timeout:
        print(f"⏱ Timeout pour {s}.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f" Erreur HTTP {e.response.status_code} pour {s}.")
        return None
    except requests.exceptions.RequestException as e:
        print(f" Erreur réseau pour {s} : {e}")
        return None
    except ValueError:
        print(f" Réponse non-JSON pour {s}.")
        return None

    if not data or "QuoteTab" not in data or not data["QuoteTab"]:
        print(f" Aucune donnée retournée pour {s}.")
        return None

    return _parse(data)


def _parse(data: dict) -> pd.DataFrame:
    """Parse le JSON Sika → DataFrame propre."""
    df = pd.json_normalize(data, record_path=["QuoteTab"])
    df = df.rename(columns=_SIKA_MAPPING_)

    df["Date"] = (
        pd.to_datetime(df["Date"], unit="D", origin="1970-01-01")
        .dt.normalize()
    )
    df = df.sort_values("Date").drop_duplicates("Date")
    df = df.set_index("Date")

    cols = [c for c in _PRICE_COLNAMES_ if c in df.columns]
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

    return df
