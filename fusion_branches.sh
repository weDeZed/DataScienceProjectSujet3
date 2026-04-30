#!/bin/bash
# Script pour fusionner data-engineer et product-designer dans main

git checkout main
git pull origin main

echo "Fusion de data-engineer dans main..."
git merge data-engineer

echo "Fusion de product-designer dans main..."
git merge product-designer

echo "Push de main vers le dépôt distant..."
git push origin main

echo "Fusion terminée !"
