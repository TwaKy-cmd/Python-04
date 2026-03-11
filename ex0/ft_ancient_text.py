#!/usr/bin/env python3

def recover_data() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        fichier = open("ancient_fragment.txt", "r")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        contenu = fichier.read()
        print(f"{contenu}")

        print("\nData recovery complete. Storage unit disconnected.")
        fichier.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_data()
