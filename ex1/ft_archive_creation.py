#!/usr/bin/env python3

def archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    fichier = open("new_discovery.txt", "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    fichier.write("[ENTRY 001] New quantum algorithm discovered\n"
                  "[ENTRY 002] Efficiency increased by 347%\n"
                  "[ENTRY 003] Archived by Data Archivist trainee")
    print("[ENTRY 001] New quantum algorithm discovered\n"
          "[ENTRY 002] Efficiency increased by 347%\n"
          "[ENTRY 003] Archived by Data Archivist trainee\n")

    fichier.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    archive_creation()
