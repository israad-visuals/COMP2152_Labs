# ============================================================
#  WEEK 11 LAB — Q1: PORT SCANNER CLASS
#  COMP2152 — ISMAIL ABDI
# ============================================================
#
#  You already know how to scan ports from Assignment 2.
#  Now you'll wrap that same logic inside a CLASS.
#  The scanning code doesn't change — just the organization.
#
# ============================================================

import socket


class SimpleScanner:

    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            result = sock.connect_ex((self.target, port))
            if result == 0:
                print(f"  Port {port}: OPEN")
                self.open_ports.append(port)
                return True
            return False
        finally:
            sock.close()


    # TODO: Write scan_range(self, start_port, end_port)
    #   Loop from start_port to end_port (inclusive)
    #   Call self.scan_port(port) for each one
    def scan_range(self, start_port, end_port):
       for port in range(start_port, end_port):
           for port in range(start_port + 1, end_port):
               self.scan_port(port)


    # TODO: Write display_results(self)
    #   Print "Results for {self.target}:"
    #   If self.open_ports is empty, print "  No open ports found."
    #   Otherwise, print each port: "  Port {port}"
    def display_results(self):
        print(f"  Results for {self.target}:")

        if not self.open_ports:
            print("    No open ports found.")
        else:
            for port in self.open_ports:
                print(f"    Port {port}")


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: PORT SCANNER CLASS")
    print("=" * 60)

    # Create first scanner object
    print("\n--- Scanner 1: localhost ---")
    scanner1 = SimpleScanner("127.0.0.1")
    print(f"  Scanning {scanner1.target} ports 78-82...")
    scanner1.scan_range(78, 82)
    scanner1.display_results()

    # Create second scanner object — separate target, separate results
    print("\n--- Scanner 2: different target ---")
    scanner2 = SimpleScanner("127.0.0.1")
    print(f"  Scanning {scanner2.target} ports 20-25...")
    scanner2.scan_range(20, 25)
    scanner2.display_results()

    print("\n" + "=" * 60)