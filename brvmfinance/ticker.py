import pandas as pd
from brvmfinance.scrapers.scrapers import fetch_history
from brvmfinance.const import BRVM_MAPPING


class Ticker:
    """
    Représente un titre coté sur la BRVM.

    Exemple
    -------
    >>> ticker = Ticker("SNTS.SN")
    >>> df = ticker.history()
    >>> ticker.summary()
    """
    _mapping = BRVM_MAPPING.copy()

    @classmethod
    def add_mapping(cls, short_name: str, full_name: str) -> None:
        """
        Permet d'ajouter ou de modifier un symbole de manière dynamique.
        Ex: Ticker.add_mapping("NOUV", "NOUV.CI")
        """
        cls._mapping[short_name.strip().upper()] = full_name.strip().upper()
        print(f"Mapping ajouté : {short_name.upper()} -> {full_name.upper()}")

    def __init__(self, ticker_name: str):
        if not ticker_name or not ticker_name.strip():
            raise ValueError("Le nom du ticker ne peut pas être vide.")
        raw_symbol = ticker_name.strip().upper()
        # --- APPLICATION DU MAPPING ---
        if raw_symbol in self._mapping:
            self.symbol = self._mapping[raw_symbol]
        else:
            self.symbol = raw_symbol
        self._history: pd.DataFrame | None = None

    def history(self, length: int = 365, force_refresh: bool = False) -> pd.DataFrame | None:
        """
        Retourne l'historique des cotations.

        Parameters
        ----------
        length : int
            Nombre de jours (max fiable en journalier : 365).
        force_refresh : bool
            Force un nouveau fetch même si le cache existe.

        Returns
        -------
        pd.DataFrame | None
        """
        if length <= 0:
            raise ValueError("length doit être un entier positif.")

        if self._history is not None and not force_refresh:
            return self._history

        df = fetch_history(self.symbol, length=length)
        if df is not None:
            self._history = df
        return df

    def summary(self) -> None:
        """Affiche un résumé des performances sur la période disponible."""
        df = self.history()
        if df is None or df.empty:
            print(f"Aucune donnée disponible pour {self.symbol}.")
            return   
        last = df["Close"].iloc[-1]
        first = df["Close"].iloc[0]
        perf = (last - first) / first * 100

        print(f"{'─' * 35}")
        print(f"  {self.symbol}")
        print(f"{'─' * 35}")
        print(f"  Dernier cours  : {last:,.0f} FCFA")
        print(f"  Performance    : {perf:+.2f}%")
        print(f"  Plus haut      : {df['High'].max():,.0f} FCFA")
        print(f"  Plus bas       : {df['Low'].min():,.0f} FCFA")
        print(f"  Volume total   : {df['Volume'].sum():,.0f}")
        print(f"  Période        : {df.index[0].date()} → {df.index[-1].date()}")
        print(f"{'─' * 35}")

    def __repr__(self) -> str:
        return f"brvmfinance.Ticker('{self.symbol}')"

    def __str__(self) -> str:
        return self.symbol
