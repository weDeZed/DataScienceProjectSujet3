import pandas as pd
import os

def clean_missing_values(input_filepath, output_filepath):
    """
    Charge le dataset, supprime les lignes contenant des valeurs manquantes,
    affiche un bilan pour le rapport, et sauvegarde le dataset nettoyé.
    """
    print("=== ÉTAPE 1 : Nettoyage des valeurs manquantes ===")
    
    # 1. Vérification de l'existence du fichier
    if not os.path.exists(input_filepath):
        print(f"Erreur : Le fichier '{input_filepath}' est introuvable.")
        return None

    # 2. Chargement des données
    df = pd.read_csv(input_filepath)
    lignes_initiales = df.shape[0]

    # 3. Suppression des lignes incomplètes
    # dropna() supprime toute ligne ayant au moins un 'NaN'
    df_clean = df.dropna()
    lignes_finales = df_clean.shape[0]
    
    lignes_supprimees = lignes_initiales - lignes_finales
    
    # 4. Sauvegarde du fichier propre
    # index=False évite de rajouter une colonne avec les anciens numéros de ligne
    df_clean.to_csv(output_filepath, index=False)
    
    # 5. Affichage du bilan (très utile pour rédiger ton rapport !)
    print(f"-> Lignes au départ  : {lignes_initiales}")
    print(f"-> Lignes supprimées : {lignes_supprimees}")
    print(f"-> Lignes restantes  : {lignes_finales}")
    print(f"-> Fichier sauvegardé sous : '{output_filepath}'\n")
    
    return df_clean

# --- Bloc d'exécution ---
if __name__ == "__main__":
    # Noms de tes fichiers (à adapter si besoin)
    fichier_brut = "marketing_and_sales.csv"
    fichier_nettoye = "marketing_and_sales_clean.csv"
    
    # Exécution de la fonction
    dataset_propre = clean_missing_values(fichier_brut, fichier_nettoye)