import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def check_redirect_chain(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] Could not connect to {url}:\n{e}")
        return

    history = response.history

    print(f"\nInitial URL: {Fore.CYAN + url}")
    print(f"Final URL:   {Fore.CYAN + response.url}")
    print(f"Status Code: {Fore.YELLOW + str(response.status_code)}")
    print(f"\nRedirect Chain ({len(history)} step(s)):")

    if not history:
        print(Fore.GREEN + "No redirects — direct connection.")
    else:
        for i, resp in enumerate(history):
            print(Fore.MAGENTA + f"{i+1}. {resp.status_code} → {resp.headers.get('Location', 'N/A')}")

        if response.url.startswith("https://"):
            print(Fore.GREEN + "\n✅ Final URL uses HTTPS.")
        else:
            print(Fore.RED + "\n⚠️ Final URL does NOT use HTTPS!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check HTTP to HTTPS redirects and redirect chain.")
    parser.add_argument("url", help="Target URL (e.g., http://example.com)")
    args = parser.parse_args()

    check_redirect_chain(args.url)
