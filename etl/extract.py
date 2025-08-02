import os
import requests
from bs4 import BeautifulSoup

DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

ABS_FILES = {
    "rppi_full": "https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/residential-property-price-indexes-eight-capital-cities/latest-release",
    "median_transfers": "https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/residential-property-price-indexes-eight-capital-cities/latest-release",
    "erp_population": "https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release",
    "net_migration": "https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release"
}

def download_file(name, url):
    dest = os.path.join(DATA_DIR, f"{name}.xlsx")

    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f"[Extract] Skipping {name}, already exists.")
        return dest

    print(f"[Extract] Scraping {name} page for Excel link...")
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Find first Excel file link
    link = soup.find("a", href=lambda h: h and h.endswith(".xlsx"))
    if not link:
        raise RuntimeError(f"[Extract] No Excel file found for {name}")

    file_url = "https://www.abs.gov.au" + link["href"]
    print(f"[Extract] Downloading {name} from {file_url}")

    file_resp = requests.get(file_url)
    file_resp.raise_for_status()

    with open(dest, "wb") as f:
        f.write(file_resp.content)
    print(f"[Extract] Saved {dest}")
    return dest

def extract_all():
    files = {}
    for name, url in ABS_FILES.items():
        files[name] = download_file(name, url)
    return files

if __name__ == "__main__":
    extract_all()
