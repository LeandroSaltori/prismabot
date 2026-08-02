import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin

BASE_URL = "https://ajuda.zdg.com.br/"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, ".gitbook", "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)

def rebrand(text):
    if not text:
        return ""
    text = re.sub(r'\bZ-PRO\b', 'Prismabot', text, flags=re.IGNORECASE)
    text = re.sub(r'\bZPRO\b', 'Prismabot', text, flags=re.IGNORECASE)
    text = re.sub(r'\bZ PRO\b', 'Prismabot', text, flags=re.IGNORECASE)
    text = re.sub(r'\bZDG\b', 'Prisma Telecom', text, flags=re.IGNORECASE)
    return text

def download_image(url, save_path):
    if os.path.exists(save_path):
        return True
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(r.content)
            return True
    except Exception as e:
        print(f"Error downloading image {url}: {e}")
    return False

def sync():
    print(f"Starting sync from {BASE_URL}...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        res = requests.get(BASE_URL, headers=headers, timeout=15)
        if res.status_code != 200:
            print(f"Failed to load home page: status {res.status_code}")
            return
        soup = BeautifulSoup(res.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching home page: {e}")
        return

    links = soup.find_all('a', href=True)
    pages_to_crawl = []
    seen = set()

    for a in links:
        href = a['href']
        if href.startswith('/') and len(href) > 1 and not href.startswith('/~') and 'http' not in href:
            if href not in seen:
                seen.add(href)
                pages_to_crawl.append((href, a.text.strip()))

    print(f"Found {len(pages_to_crawl)} pages to sync.")

    for href, title in pages_to_crawl:
        full_url = urljoin(BASE_URL, href)
        try:
            r = requests.get(full_url, headers=headers, timeout=15)
            if r.status_code != 200:
                continue
            psoup = BeautifulSoup(r.text, 'html.parser')
            main = psoup.find('main')
            if not main:
                continue

            sr_only = main.find('div', class_='sr-only')
            if sr_only:
                sr_only.decompose()

            rel_path = href.lstrip('/') + ".md"
            rel_path = rebrand(rel_path).lower().replace(' ', '-')

            out_md_path = os.path.join(ROOT_DIR, rel_path)
            os.makedirs(os.path.dirname(out_md_path), exist_ok=True)

            for img in main.find_all('img'):
                src = img.get('src')
                if not src:
                    continue
                img_url = urljoin(full_url, src)
                img_name = f"img_{abs(hash(img_url)) % 10000000}.png"
                img_save_path = os.path.join(ASSETS_DIR, img_name)
                download_image(img_url, img_save_path)

                depth = len([p for p in rel_path.replace('\\', '/').split('/') if p]) - 1
                prefix = "../" * depth if depth > 0 else "./"
                img['src'] = f"{prefix}.gitbook/assets/{img_name}"

            html_str = str(main)
            html_str = rebrand(html_str)
            md_text = md(html_str, heading_style="ATX")

            with open(out_md_path, "w", encoding="utf-8") as f:
                f.write(md_text)

        except Exception as e:
            print(f"Error processing page {href}: {e}")

    print("Sync complete!")

if __name__ == "__main__":
    sync()
