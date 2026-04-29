import random
from .const import USER_AGENTS


def get_header():
    """Genere des agents aléatoires pour eviter blocage"""
    return
    {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': 'https://www.sikafinance.com/',
        'Accept': 'application/json',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }
