#!/usr/bin/env python3

def crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as archive:
            contenu = archive.read()
            print(f"{contenu}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as vault:
            data = vault.read()
            print(f"{data}")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as standard:
            contenu_archive = standard.read()
            print(f"SUCCESS: Archive recovered - ``{contenu_archive}''")
            print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(f"RESPONSE: Error - {e}")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
