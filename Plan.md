# Livrables :
- Code source de la solution fonctionnelle (+ documentation technique en annexe)
- Rapport du projet (6 pages)
- Support de Présentation du projet OU Vidéo de démonstration
# Etapes :
- [x] Analyse du dataset
	- [x] Clean le dataset
	- [x] Analyser la corrélation
- [x] Commencer par un modèle simple de référence (régression linéaire)
- [ ] Comparer 3 modèles + complexe
- [ ] En choisir un
- [ ] Analyser les erreurs 
	- [ ] Validation croisée
	- [ ] Matrice de confusion
- [ ] Interpréter les résultats
	- [ ] Faire un dashboard
# Répartition :

# Notes : 
- On remarque une très faible quantité de lignes avec des colonnes manquantes (- de 30 sur 4562). On décide de les supprimer
- Le modèle de régression linéaire permet d'évaluer en se basant sur une combination des budgets des 3 canaux de communication. On peut envisager en piste d'amélioration de permettre une simulation ciblée par canal.
- XGB model pas retenu : la RMSE est plus élevé