import time
from logger import log_event
from config import config
import threading

import json
import smtplib
from email.mime.text import MIMEText

class DDoSProtection:
    def __init__(self):
        self.rate_limit = config.get('ddos', {}).get('rate_limit', 100)
        self.block_duration = config.get('ddos', {}).get('block_duration', 600)
        self.requests = {}
        self.blocked_ips = self.load_blocked_ips()
        self.whitelist = set(config.get('ddos', {}).get('whitelist', []))
        self.email = config.get('email', '')

    def check_request(self, ip):
        now = int(time.time())
        if ip in self.whitelist:
            return True
        if ip in self.blocked_ips and now < self.blocked_ips[ip]:
            log_event(f"IP bloquée: {ip}")
            return False
        self.requests.setdefault(ip, []).append(now)
        self.requests[ip] = [t for t in self.requests[ip] if now - t < 60]
        if len(self.requests[ip]) > self.rate_limit:
            self.blocked_ips[ip] = now + self.block_duration
            self.save_blocked_ips()
            log_event(f"Blocage automatique IP: {ip} ({len(self.requests[ip])} requêtes/min)")
            self.notify_block(ip)
            return False
        return True

    def unblock_ips(self):
        now = int(time.time())
        for ip in list(self.blocked_ips):
            if now >= self.blocked_ips[ip]:
                del self.blocked_ips[ip]
                self.save_blocked_ips()
                log_event(f"IP débloquée: {ip}")

    def start(self):
        def run():
            while True:
                self.unblock_ips()
                time.sleep(10)
        threading.Thread(target=run, daemon=True).start()

    def save_blocked_ips(self):
        try:
            with open('blocked_ips.json', 'w') as f:
                json.dump(self.blocked_ips, f)
        except Exception as e:
            log_event(f"Erreur sauvegarde IPs: {e}")

    def load_blocked_ips(self):
        try:
            with open('blocked_ips.json', 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def notify_block(self, ip):
        if not self.email:
            return
        try:
            msg = MIMEText(f"Blocage automatique de l'IP {ip} suite à une suspicion d'attaque DDoS.")
            msg['Subject'] = 'Alerte DDoS'
            msg['From'] = 'defense@localhost'
            msg['To'] = self.email
            s = smtplib.SMTP('localhost')
            s.send_message(msg)
            s.quit()
            log_event(f"Notification email envoyée pour IP: {ip}")
        except Exception as e:
            log_event(f"Erreur notification email: {e}")

    def status(self):
        return {
            'blocked_ips': self.blocked_ips,
            'whitelist': list(self.whitelist),
            'rate_limit': self.rate_limit
        }

input("Appuyez sur Entrée pour quitter...")
