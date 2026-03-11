#!/usr/bin/env python3

import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    id_archiv = input("Enter archivist ID: ")
    status_archiv = input("Enter status report: ")

    print(f"\n[STANDARD] Archive status"
          f" from {id_archiv}: {status_archiv}", file=sys.stdout)

    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stdout)
    print("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
