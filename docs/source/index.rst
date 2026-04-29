brvmfinance documentation
=========================

Télécharger les données boursières de la BRVM (Bourse Régionale des Valeurs Mobilières)
--------------------------------------------------------------------------------------

.. image:: _static/logo.png
   :width: 200
   :alt: brvmfinance logo
   :align: center

.. admonition:: AVERTISSEMENT LÉGAL IMPORTANT

   **BRVM est une marque déposée de la Bourse Régionale des Valeurs Mobilières.**

   brvmfinance n'est **pas** affilié, approuvé ou validé par la BRVM. Il s'agit d'un outil 
   open-source utilisant des données publiques, destiné à la recherche et à des fins éducatives.

   **Vous devez vous référer aux conditions d'utilisation de la source** pour plus de détails 
   sur vos droits d'utilisation des données téléchargées.

Installation
------------

.. code-block:: bash

    $ pip install brvmfinance

Démarrage rapide
----------------

Voici un petit exemple de l'API brvmfinance.

.. code-block:: python

   from brvmfinance import Ticker
   
   # Initialiser un titre (ex: Orange CI)
   dat = Ticker("ORAC")

   # Récupérer l'historique du dernier mois
   hist = dat.history(period='1mo')
   print(hist)

Plusieurs titres
----------------

.. code-block:: python

   from brvmfinance import Tickers
   
   tickers = Tickers('SNTS ORAC SGBC')
   # Télécharger les données pour tous les titres
   data = tickers.history(period='1mo')

.. toctree::
   :maxdepth: 2
   :caption: Sommaire: