from brvmfinance.ticker import Ticker

# On crée l'objet
ticker = Ticker("SNTS.SN")

# On récupère l'historique
df = ticker.history(length=365)

if df is not None:
    print(df.tail())
    print(f"\nNombre de lignes : {len(df)}")
    # LA LIGNE À CORRIGER EST ICI :
    # Remplace ticker.ticker par ticker.symbol
    print(f" Données récupérées pour {ticker.symbol}")
else:
    print(" Échec de la récupération.")