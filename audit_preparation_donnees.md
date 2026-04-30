# Rapport d'Audit et de Préparation des Données

## Présentation du Jeu de Données
Le jeu de données **marketing_and_sales.csv** recense l'historique de plus de **4 500 campagnes publicitaires**. Pour chacune d'entre elles, il détaille de manière précise les investissements marketing (exprimés en millions) répartis sur trois principaux canaux d'acquisition :
* **Télévision (TV)**
* **Radio**
* **Réseaux sociaux (Social Media)**

Le jeu de données précise également le type de partenariat d'influence mis en place lors de la campagne, classé en quatre catégories : **Mega, Macro, Micro et Nano**. 

La variable clé de ce fichier est le volume de ventes généré (**Sales**, également en millions). Ce jeu de données permet d'étudier la relation entre l'allocation du budget publicitaire multicanal et la performance commerciale, dans le but d'optimiser le retour sur investissement (ROI).

---

## 1. Audit initial du jeu de données
L'analyse exploratoire a révélé que le dataset brut contient **4 572 enregistrements**. Globalement, les données sont de très bonne qualité :
* **Aucun doublon** n'a été détecté.
* **Aucune valeur aberrante** illogique (telle que des budgets négatifs) n'est présente.
* **Équilibre des classes** : La variable catégorielle *Influencer* est parfaitement équilibrée entre ses quatre catégories, ce qui écarte tout problème de déséquilibre de classe pour la modélisation.

## 2. Traitement des valeurs manquantes : Stratégie de suppression
L'audit a mis en évidence la présence de valeurs manquantes (NaN) sur **26 lignes**, impactant les colonnes de budget ainsi que la variable cible (*Sales*).

Nous avons opté pour une **stratégie de suppression stricte** (Listwise Deletion) plutôt qu'un remplacement par la moyenne ou la médiane. Ce choix est justifié par :
* **Faible impact quantitatif** : Les 26 lignes ne représentent qu'environ 0,5 % du volume total. Leur suppression laisse 4 546 observations saines, ce qui est largement suffisant.
* **Préservation de la dynamique** : Le dataset présente des corrélations extrêmement fortes (notamment entre la TV et les ventes). L'imputation risquerait d'introduire un biais statistique et de fausser l'apprentissage des relations ou l'évaluation des performances.

## 3. Traitement des valeurs extrêmes (Outliers)
Nous avons identifié quelques valeurs extrêmes légitimes (budgets très élevés sur la Radio et les Social Media). La décision a été prise de **les conserver**. 
* **Contexte métier** : Ces données représentent des campagnes à fort investissement réelles et non des erreurs de saisie.
* **Robustesse des modèles** : Des algorithmes comme le *Random Forest* ou le *Gradient Boosting* captureront ces effets sans être biaisés, permettant d'étudier l'impact de ces investissements massifs.

---

## Conclusion
Le pipeline de nettoyage mis en place garantit un jeu de données **100 % sain**. Cette rigueur prévient tout risque de fuite de données (*Data Leakage*) lors des phases d'encodage et de standardisation à venir sur les ensembles d'entraînement et de test.
