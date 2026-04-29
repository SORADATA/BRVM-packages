import pandas as pd
from .scrapers.scrapers import fetch_history


class Ticker:
    """Classe représentant un actif de la BRVM."""
    def __init__(self, ticker_name: str):
        self.symbol = ticker_name.upper()
        self._history = None

    def history(self, length=365, force_refresh=False) -> pd.DataFrame:
        """
        Récupère l'historique des cotations.
        Si les données ont déjà été téléchargées, retourne le cache,
        sauf si force_refresh est True.
        """
        # Si on a déjà les données ET qu'on ne force pas le rafraîchissement
        if self._history is not None and not force_refresh:
            return self._history

        # Sinon, on fait la requête web
        df = fetch_history(self.symbol, length=length)
        if df is not None:
            self._history = df
        return df

    def __repr__(self):
        return f"brvmfinance.Ticker('{self.symbol}')"