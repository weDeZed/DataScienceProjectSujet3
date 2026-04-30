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
* **Équilibre des classes** : La variable catégorielle *Influencer* est parfaitement équilibrée entre ses quatre catégories, ce qui facilite l'apprentissage du modèle.

## 2. Traitement des valeurs manquantes : Stratégie de suppression
L'audit a mis en évidence la présence de valeurs manquantes (NaN) sur **26 lignes**, impactant les colonnes de budget ainsi que la variable cible (*Sales*).

Nous avons opté pour une **stratégie de suppression stricte** (Listwise Deletion). Ce choix est justifié par le faible impact quantitatif (0,5 % des données) et la nécessité de préserver l'intégrité des relations statistiques entre les budgets et les ventes sans introduire de biais d'imputation.

## 3. Normalisation de la variable "Influencer" (Encodage Ordinal)
La colonne *Influencer* étant textuelle, elle n'est pas directement exploitable par les algorithmes de Machine Learning. Nous avons appliqué une **normalisation ordinale** via la méthode `replace()` de Pandas.

Ce choix se justifie par la hiérarchie naturelle de la taille des audiences d'influenceurs. Nous avons établi la correspondance suivante :
* **Nano** : 1
* **Micro** : 2
* **Macro** : 3
* **Mega** : 4

Cette transformation permet au modèle de traiter cette information comme une échelle de puissance d'influence plutôt que comme de simples étiquettes distinctes.

## 4. Traitement des valeurs extrêmes (Outliers)
Nous avons identifié des valeurs extrêmes légitimes sur les budgets Radio et Social Media. Elles ont été **conservées** car elles représentent des campagnes à fort investissement réelles. Les modèles basés sur les arbres (Random Forest, Gradient Boosting) sont nativement robustes à ces variations.

---

## Conclusion
Le pipeline de nettoyage et de normalisation garantit un jeu de données **100 % numérique et sain**. Le passage d'un format texte à un format ordinal pour les influenceurs, combiné à la suppression des données incomplètes, fournit une base robuste pour l'entraînement de nos modèles prédictifs.