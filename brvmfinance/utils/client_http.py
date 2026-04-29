import random
import string
from brvmfinance.const import USER_AGENTS


def get_header() -> dict:
    """Headers HTTP avec User-Agent aléatoire."""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": "https://www.sikafinance.com/",
        "Accept": "application/json",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    }


def get_faux_guid(length: int = 30) -> str:
    """Génère un identifiant alphanumérique aléatoire."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))