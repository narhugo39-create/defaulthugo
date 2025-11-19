import re
import requests
from logger import log_event
from config import config

class PhishingDetector:
    SUSPICIOUS_KEYWORDS = ['login', 'secure', 'update', 'verify', 'account', 'bank']
    URL_REGEX = re.compile(r'https?://[\w.-]+(?:/[\w./?%&=-]*)?')

    def is_suspicious_url(self, url):
        if any(kw in url.lower() for kw in self.SUSPICIOUS_KEYWORDS):
            log_event(f"URL suspecte détectée: {url}")
            return True
        try:
            resp = requests.get(url, timeout=3)
            if resp.status_code != 200:
                log_event(f"URL inaccessible: {url}")
                return True
        except Exception:
            log_event(f"Erreur lors de l'accès à l'URL: {url}")
            return True
        return False

    def scan_text(self, text):
        urls = self.URL_REGEX.findall(text)
        return [url for url in urls if self.is_suspicious_url(url)]
