from typing import List, Union
import pandas as pd
from .ticker import Ticker


class Tickers:
    """
    Gère un groupe de plusieurs titres cotés sur la BRVM.

    Exemple
    -------
    >>> tickers = Tickers("SNTS ORGC SGBC") # Plus besoin des suffixes !
    >>> df_multi = tickers.history(length=365)
    """

    def __init__(self, tickers_input: Union[str, List[str]]):
        """
        Accepte soit une liste de chaînes ['SNTS', 'ORGC'],
        soit une seule chaîne séparée par des espaces 'SNTS ORGC'.
        """
        if isinstance(tickers_input, str):
            raw_symbols = [s.strip().upper() for s in tickers_input.replace(',', ' ').split() if s.strip()]
        else:
            raw_symbols = [s.strip().upper() for s in tickers_input if s.strip()]
        if not raw_symbols:
            raise ValueError("La liste de tickers ne peut pas être vide.")
        self.tickers_dict = {}
        for raw_sym in raw_symbols:
            t = Ticker(raw_sym)
            self.tickers_dict[t.symbol] = t
        # On met à jour la liste avec les noms officiels (ex: SNTS.SN)
        self.symbols = list(self.tickers_dict.keys())

    def history(self, length: int = 365, force_refresh: bool = False) -> pd.DataFrame:
        """
        Récupère l'historique pour tous les tickers et les combine.
        """
        all_dfs = []
        print(f"Récupération des données pour {len(self.symbols)} tickers...")

        for sym, ticker_obj in self.tickers_dict.items():
            try:
                # La méthode history du Ticker
                df = ticker_obj.history(length=length, force_refresh=force_refresh)
                if df is not None and not df.empty:
                    # On utilise le symbole officiel corrigé
                    df['Symbol'] = sym
                    all_dfs.append(df)
                    print(f" {sym} : OK ({len(df)} lignes)")
                else:
                    print(f" {sym} : Aucune donnée.")
            except Exception as e:
                print(f" {sym} : Erreur ({e})")
        if not all_dfs:
            print("Aucune donnée n'a pu être collectée au total.")
            return pd.DataFrame()
        combined_df = pd.concat(all_dfs)
        # Tri par Date pour un format propre
        combined_df = combined_df.sort_index()
        return combined_df
