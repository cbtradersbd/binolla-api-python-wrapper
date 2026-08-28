import requests

BASE_URL = "https://api1.api.cbtraderbd.xyz"

def get_binolla_payouts():
    url = f"{BASE_URL}/docs"
    print(f"Connecting to Binolla API at {url}...")

if __name__ == "__main__":
    get_binolla_payouts()
