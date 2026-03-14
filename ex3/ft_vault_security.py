#!/usr/bin/env python3

def vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION: ")
    with open("classified_data.txt", "r") as fichier:
        contenu = fichier.read()
    print(f"{contenu}\n")

    print("SECURE PRESERVATION:")
    with open("new_file.txt", "w") as vault:
        vault.write("[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security()
