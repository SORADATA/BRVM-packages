# Endpoint principal Sika Finance
_BASE_URL_ = "https://www.sikafinance.com/api/charting/GetTicksEOD"
_ROOT_URL_ = "https://www.sikafinance.com"

# Colonnes de prix standard
_PRICE_COLNAMES_ = ['Open', 'High', 'Low', 'Close', 'Adj Close']

# Mapping JSON Sika → noms standard
_SIKA_MAPPING_ = {
    'd': 'Date',
    'o': 'Open',
    'h': 'High',
    'l': 'Low',
    'c': 'Close',
    'v': 'Volume'
}

# Dictionnaire de mapping complet des 47 actions cotées à la BRVM
BRVM_MAPPING = {
    # --- CÔTE D'IVOIRE (.CI) ---
    "ABJC": "ABJC.CI",   # SERVAIR ABIDJAN CI
    "BICC": "BICC.CI",   # BICI CI
    "BNBC": "BNBC.CI",   # BERNABE CI
    "BOAC": "BOAC.CI",   # BANK OF AFRICA CI
    "CABC": "CABC.CI",   # SICABLE CI
    "CFAC": "CFAC.CI",   # CFAO MOTORS CI
    "CIEC": "CIEC.CI",   # CIE CI
    "ECOC": "ECOC.CI",   # ECOBANK COTE D'IVOIRE
    "FTSC": "FTSC.CI",   # FILTISAC CI
    "NEIC": "NEIC.CI",   # NEI-CEDA CI
    "NSBC": "NSBC.CI",   # NSIA BANQUE COTE D'IVOIRE
    "NTLC": "NTLC.CI",   # NESTLE CI
    "ORAC": "ORAC.CI",   # ORANGE COTE D'IVOIRE
    "PALC": "PALC.CI",   # PALM CI
    "PRSC": "PRSC.CI",   # TRACTAFRIC MOTORS CI
    "SAFC": "SAFC.CI",   # SAFCA CI
    "SCRC": "SCRC.CI",   # SUCRIVOIRE
    "SDCC": "SDCC.CI",   # SODE CI
    "SDSC": "SDSC.CI",   # AFRICA GLOBAL LOGISTICS CI
    "SEMC": "SEMC.CI",   # EVIOSYS PACKAGING SIEM CI
    "SGBC": "SGBC.CI",   # SOCIETE GENERALE COTE D'IVOIRE
    "SHEC": "SHEC.CI",   # VIVO ENERGY CI
    "SIBC": "SIBC.CI",   # SOCIETE IVOIRIENNE DE BANQUE
    "SICC": "SICC.CI",   # SICOR CI
    "SIVC": "SIVC.CI",   # ERIUM CI (Ex AIR LIQUIDE CI)
    "SLBC": "SLBC.CI",   # SOLIBRA CI
    "SMBC": "SMBC.CI",   # SMB CI
    "SOGC": "SOGC.CI",   # SOGB CI
    "SPHC": "SPHC.CI",   # SAPH CI
    "STAC": "STAC.CI",   # SETAO CI
    "STBC": "STBC.CI",   # SITAB CI
    "TTLC": "TTLC.CI",   # TOTALENERGIES MARKETING CI
    "UNLC": "UNLC.CI",   # UNILEVER CI
    "UNXC": "UNXC.CI",   # UNIWAX CI

    # --- SÉNÉGAL (.SN) ---
    "BOAS": "BOAS.SN",   # BANK OF AFRICA SENEGAL
    "SNTS": "SNTS.SN",   # SONATEL SN
    "TTLS": "TTLS.SN",   # TOTALENERGIES MARKETING SN

    # --- BURKINA FASO (.BF) ---
    "BOABF": "BOABF.BF",  # BANK OF AFRICA BF
    "CBIBF": "CBIBF.BF",  # CORIS BANK INTERNATIONAL
    "ONTBF": "ONTBF.BF",  # ONATEL BF

    # --- MALI (.ML) ---
    "BOAM": "BOAM.ML",   # BANK OF AFRICA ML

    # --- TOGO (.TG) ---
    "ETIT": "ETIT.TG",   # ECOBANK TRANS. INCORP. TG
    "ORGT": "ORGT.TG",   # ORAGROUP TOGO

    # --- BÉNIN (.BJ) ---
    "BICB": "BICB.BJ",   # BIIC BN
    "LNBB": "LNBB.BJ",   # LOTERIE NATIONALE DU BENIN
    "BOAB": "BOAB.BJ",   # BANK OF AFRICA BN

    # --- NIGER (.NE) ---
    "BOAN": "BOAN.NE",   # BANK OF AFRICA NG
}

# Limite journalière connue de l'API (au-delà → compression hebdo)
MAX_DAILY_LENGTH = 365

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (X11; Linux i686; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/131.0.2903.86",
]