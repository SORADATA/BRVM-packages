import requests
import pandas as pd
import random
import string


def fetch_history(symbole, length=365):
    base_url = "https://www.sikafinance.com/api/charting/GetTicksEOD"
    
    # On s'assure que le symbole est en majuscules
    s = symbole.upper()
    
    # Génération du guid pour simuler un navigateur réel
    faux_guid = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    
    parametres = {
        'symbol': s, 
        'length': length, 
        'period': '0', 
        'guid': faux_guid
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.sikafinance.com/'
    }

    try:
        reponse = requests.get(base_url, params=parametres, headers=headers, timeout=10)
        reponse.raise_for_status()
        
        donnees = reponse.json()

        # Si le serveur renvoie une liste vide
        if not donnees:
            print(f"❌ Aucune donnée trouvée pour {s}")
            return None

        df_brut = pd.DataFrame(donnees)
        
        # On vérifie si la colonne QuoteTab est présente
        if 'QuoteTab' in df_brut.columns:
            # Extraction des données financières
            df_propre = df_brut['QuoteTab'].apply(pd.Series)
            
            # Renommage des colonnes (format standard financier)
            colonnes_noms = {
                'd': 'Date', 
                'o': 'Open', 
                'h': 'High', 
                'l': 'Low', 
                'c': 'Close', 
                'v': 'Volume'
            }
            df_propre = df_propre.rename(columns=colonnes_noms)
            
            # Conversion du timestamp Sika en vraie Date
            if 'Date' in df_propre.columns:
                df_propre['Date'] = pd.to_datetime(df_propre['Date'], unit='D', origin='1970-01-01')
                df_propre.set_index('Date', inplace=True)
            
            return df_propre
        else:
            print(f"❌ Format de données invalide pour {s}")
            return None

    except Exception as e:
        print(f"⚠️ Erreur lors de la récupération de {s} : {e}")
        return None