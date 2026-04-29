import requests
import pandas as pd
from brvmfinance.const import _BASE_URL_, _SIKA_MAPPING_, _PRICE_COLNAMES_
from brvmfinance.utils.client_http import get_header, get_faux_guid


def fetch_history(symbole, length=365):
    """
    Récupère l'historique EOD d'un titre via l'API Sika Finance.
    """
    s = symbole.upper()
    # Paramètres de la requête
    parametres = {
        'symbol': s,
        'length': length,
        'period': '0',
        'guid': get_faux_guid()
    }

    try:
        # Exécution de la requête HTTP
        reponse = requests.get(
            _BASE_URL_,
            params=parametres,
            headers=get_header(),
            timeout=10
        )
        reponse.raise_for_status()
        donnees = reponse.json()

        # Sécurité si aucune donnée n'est renvoyée
        if not donnees or 'QuoteTab' not in donnees:
            print(f"Aucune donnée ou format invalide pour {s}")
            return None

        # Transformation du JSON en DataFrame Pandas
        df = pd.json_normalize(donnees, record_path=['QuoteTab'])
        df = df.rename(columns=_SIKA_MAPPING_)
        if 'Date' in df.columns:
            # Conversion des dates (Origine Unix 1970 avec unité Jours)
            df['Date'] = pd.to_datetime(df['Date'], unit='D', origin='1970-01-01')
            # Suppression des heures pour ne garder que la date YYYY-MM-DD
            df['Date'] = df['Date'].dt.normalize()
            # Tri chronologique (Ancien -> Récent)
            df = df.sort_values('Date')
            df.set_index('Date', inplace=True)
            # Conversion
            cols_to_convert = [col for col in _PRICE_COLNAMES_ if col in df.columns]
            df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce')
        return df

    except Exception as e:
        print(f" Erreur lors de la récupération de {s} : {e}")
        return None