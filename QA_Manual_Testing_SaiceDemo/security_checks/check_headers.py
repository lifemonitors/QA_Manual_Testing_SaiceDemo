import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

REQUIRED_HEADERS = {
    "Content-Security-Policy": "Helps prevent XSS attacks",
    "X-Frame-Options": "Mitigates clickjacking",
    "X-Content-Type-Options": "Prevents MIME type sniffing",
    "Strict-Transport-Security": "Enforces HTTPS connections",
    "Access-Control-Allow-Origin": "Controls cross-origin requests"
}

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] Could not connect to {url}:\n{e}")
        return

    print(f"\nChecked URL: {Fore.CYAN + url}")
    print(f"Status Code: {Fore.YELLOW + str(response.status_code)}")

    headers = response.headers
    print("\nSecurity Headers Check:")
    for header, purpose in REQUIRED_HEADERS.items():
        if header in headers:
            print(Fore.GREEN + f"[OK] {header} — {purpose}")
        else:
            print(Fore.RED + f"[MISSING] {header} — {purpose}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check security-related HTTP headers.")
    parser.add_argument("url", help="Target URL (e.g., https://example.com)")
    args = parser.parse_args()

    check_security_headers(args.url)
