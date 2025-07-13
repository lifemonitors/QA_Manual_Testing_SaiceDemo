import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin
from colorama import Fore, init

init(autoreset=True)

def extract_forms(url):
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] Could not connect to {url}:\n{e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    print(f"\nFound {len(forms)} form(s) on {Fore.CYAN + url}:\n")

    for i, form in enumerate(forms, 1):
        action = form.get("action")
        method = form.get("method", "get").upper()
        full_action = urljoin(url, action)

        print(Fore.YELLOW + f"Form #{i}")
        print(f"  Method: {method}")
        print(f"  Action: {full_action}")
        print(f"  Inputs:")

        inputs = form.find_all(["input", "textarea", "select"])
        for inp in inputs:
            name = inp.get("name")
            type_ = inp.get("type", "text") if inp.name == "input" else inp.name
            print(Fore.GREEN + f"    - {type_} | name={name}")
        print("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and list forms from a web page.")
    parser.add_argument("url", help="Target URL (e.g., https://example.com/login)")
    args = parser.parse_args()

    extract_forms(args.url)
