import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque
from .utils import is_valid_url

def crawl_and_extract(urls, max_pages=20):
    visited = set()
    queue = deque(urls)
    combined_text = ""

    while queue and len(visited) < max_pages:
        link = queue.popleft()
        if link in visited or not is_valid_url(link):
            continue
        
        try:
            html = requests.get(link, timeout=5)
            soup = BeautifulSoup(html.text, "html.parser")
            visited.add(link)

            text = soup.get_text(separator=" ", strip=True)
            combined_text += "\n" + text

            # enqueue hyperlinks
            for a in soup.find_all("a", href=True):
                full_url = urljoin(link, a["href"])
                if is_valid_url(full_url) and full_url not in visited:
                    queue.append(full_url)

        except Exception as e:
            print("[Crawl Error]", e)
            continue
    
    return combined_text
