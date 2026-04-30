import pandas as pd
import os

def clean_and_normalize_data(input_filepath, output_filepath):
    """
    Charge le dataset, supprime les valeurs manquantes, 
    normalise la colonne 'Influencer' en valeurs numériques, 
    et sauvegarde le résultat.
    """
    print("=== ÉTAPE 1 : Nettoyage et Normalisation ===")
    
    # 1. Vérification de l'existence du fichier
    if not os.path.exists(input_filepath):
        print(f"Erreur : Le fichier '{input_filepath}' est introuvable.")
        return None

    # 2. Chargement des données
    df = pd.read_csv(input_filepath)
    lignes_initiales = df.shape[0]

    # 3. Suppression des lignes incomplètes
    # On utilise .copy() pour s'assurer qu'on travaille sur un nouveau tableau propre
    # et éviter un avertissement pandas (SettingWithCopyWarning) à l'étape suivante.
    df_clean = df.dropna().copy()
    
    # 4. Normalisation de la colonne 'Influencer' avec replace()
    # On crée un dictionnaire de correspondance (mapping)
    mapping_influencer = {
        'Nano': 1,
        'Micro': 2,
        'Macro': 3,
        'Mega': 4
    }
    # On remplace les textes par les chiffres correspondants
    df_clean['Influencer'] = df_clean['Influencer'].replace(mapping_influencer)
    
    # 5. Sauvegarde du fichier propre
    lignes_finales = df_clean.shape[0]
    df_clean.to_csv(output_filepath, index=False)
    
    # 6. Affichage du bilan
    print(f"-> Lignes au départ  : {lignes_initiales}")
    print(f"-> Lignes supprimées : {lignes_initiales - lignes_finales}")
    print(f"-> Lignes restantes  : {lignes_finales}")
    print(f"-> Normalisation 'Influencer' appliquée : {mapping_influencer}")
    print(f"-> Fichier sauvegardé sous : '{output_filepath}'\n")
    
    return df_clean

# --- Bloc d'exécution ---
if __name__ == "__main__":
    # Noms de tes fichiers (à adapter si besoin)
    fichier_brut = "marketing_and_sales.csv"
    fichier_nettoye = "marketing_and_sales_clean.csv"
    
    # Exécution de la fonction
    dataset_propre = clean_and_normalize_data(fichier_brut, fichier_nettoye)
    
    # Petit aperçu pour vérifier que ça a bien fonctionné
    if dataset_propre is not None:
        print("\nAperçu des 5 premières lignes après traitement :")
        print(dataset_propre.head())