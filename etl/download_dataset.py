import os
import requests
from bs4 import BeautifulSoup

DATA_DIR = "data/raw"
ABS_URL = "https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/residential-property-price-indexes-eight-capital-cities/latest-release"
SA_URL = "https://data.sa.gov.au/data/dataset/metro-median-house-sales"

def download_abs():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("[Download ABS] Fetching ABS dataset...")

    response = requests.get(ABS_URL)
    if response.status_code != 200:
        raise Exception("Failed to access ABS website")

    soup = BeautifulSoup(response.text, "html.parser")

    # Find Excel download link (look for .xlsx)
    link = soup.find("a", href=lambda href: href and href.endswith(".xlsx"))
    if not link:
        raise Exception("Could not find ABS .xlsx link")

    file_url = link["href"]
    if not file_url.startswith("http"):
        file_url = "https://www.abs.gov.au" + file_url

    abs_file = os.path.join(DATA_DIR, "abs_house_prices.xlsx")
    with requests.get(file_url, stream=True) as r:
        with open(abs_file, "wb") as f:
            f.write(r.content)

    print(f"[Download ABS] Saved to {abs_file}")
    return abs_file

def download_sa():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("[Download SA] Fetching South Australia dataset...")

    response = requests.get(SA_URL)
    if response.status_code != 200:
        raise Exception("Failed to access SA data portal")

    soup = BeautifulSoup(response.text, "html.parser")

    # Find CSV download link
    link = soup.find("a", href=lambda href: href and href.endswith(".csv"))
    if not link:
        raise Exception("Could not find SA .csv link")

    file_url = link["href"]
    if not file_url.startswith("http"):
        file_url = "https://data.sa.gov.au" + file_url

    sa_file = os.path.join(DATA_DIR, "sa_suburb_prices.csv")
    with requests.get(file_url, stream=True) as r:
        with open(sa_file, "wb") as f:
            f.write(r.content)

    print(f"[Download SA] Saved to {sa_file}")
    return sa_file

if __name__ == "__main__":
    download_abs()
    download_sa()
