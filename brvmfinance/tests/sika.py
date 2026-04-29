from brvmfinance.ticker import Ticker
from brvmfinance.tickers import Tickers

# On crée l'objet
ticker = Ticker("BOAM")

# On récupère l'historique
df = ticker.history(length=365)

if df is not None:
    print(df.tail())
    print(f"\nNombre de lignes : {len(df)}")
    # Remplace ticker.ticker par ticker.symbol
    print(f" Données récupérées pour {ticker.symbol}")
else:
    print(" Échec de la récupération.")


print(df.tail(200))


# Tu peux passer une chaîne avec des espaces
mes_actions = Tickers("SNTS ORAC BOAM SGBC")

# Récupération globale
df_global = mes_actions.history(length=365)

print("\n📊 APERÇU DU DATAFRAME GLOBAL :")
print(df_global.head())

print("\n📈 RÉPARTITION DES DONNÉES PAR ACTION :")
print(df_global['Symbol'].value_counts())
print(df_global.tail(200))

df = Ticker("BOAM")
df = ticker.history(length=365)
print(df.tail(20))