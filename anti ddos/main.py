from ddos_protection import DDoSProtection
from phishing_detector import PhishingDetector
from network_anomaly import NetworkAnomaly
from logger import log_event
from config import config

import getpass

def collect_email():
    email = input("Entrez votre email pour l'enregistrement : ")
    config.data['email'] = email
    log_event(f"Email utilisateur enregistré : {email}")
    return email

def main():
    print("--- Système de protection défensif ---")
    email = collect_email()
    ddos = DDoSProtection()
    phishing = PhishingDetector()
    network = NetworkAnomaly()
    ddos.start()
    network.start()
    print("Protection activée. Surveillance en cours...")
    while True:
        text = input("Texte à analyser (liens phishing) ou 'exit' : ")
        if text.lower() == 'exit':
            break
        suspects = phishing.scan_text(text)
        if suspects:
            print(f"URLs suspectes détectées : {suspects}")
        else:
            print("Aucune URL suspecte détectée.")

if __name__ == "__main__":
    main()
