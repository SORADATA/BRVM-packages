<p align="center">
  <img src="brvmfinance/docs/source/_static/logo.png" width="550" alt="brvmfinance logo">
</p>

# Télécharger les données boursières de la BRVM

<p align="left">
  <a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/badge/python-3.7+-blue.svg?style=flat" alt="Version Python"></a>
  <a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/v/brvmfinance.svg?maxAge=60%" alt="Version PyPi"></a>
  <a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/status/brvmfinance.svg?maxAge=60" alt="Statut PyPi"></a>
  <a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/dm/brvmfinance.svg?maxAge=86400&label=installations&color=%2327B1FF" alt="Téléchargements PyPi"></a>
  <a target="new" href="https://github.com/SORADATA/brvmfinance"><img border=0 src="https://img.shields.io/github/stars/SORADATA/brvmfinance.svg?style=social&label=Étoiles&maxAge=60" alt="Suivre ce projet"></a>
</p>

**brvmfinance** offre une solution Pythonique pour récupérer les données financières et boursières de la **Bourse Régionale des Valeurs Mobilières (BRVM)**.

---

> [!IMPORTANT]  
> **BRVM est une marque déposée de la Bourse Régionale des Valeurs Mobilières.**
>
> brvmfinance n'est **pas** affilié, approuvé ou validé par la BRVM. Il s'agit d'un outil open-source utilisant des données publiques, destiné à la recherche et à des fins éducatives.
> 
> **Vous devez vous référer aux conditions d'utilisation de la source pour plus de détails sur vos droits d'utilisation des données téléchargées.**

---

## 🚀 Présentation

Inspiré par `yfinance`, ce package permet aux analystes et développeurs de récupérer facilement les cotations, les historiques et les informations sur les sociétés cotées à la BRVM (UEMOA).

## 🛠 Composants principaux

- `Ticker` : données pour un titre unique (ex: `SNTS`, `ETIT`)
- `Tickers` : données pour plusieurs titres simultanément
- `download` : téléchargement massif de données historiques du marché
- `Market` : obtenir des informations sur l'état du marché et les indices

## 📦 Installation

Installez `brvmfinance` depuis PYPI via `pip` :

```bash
$ pip install brvmfinance