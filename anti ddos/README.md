# Logiciel défensif anti-DDoS, phishing et anomalies réseau

## Description
Ce projet Python protège un serveur ou une application contre les attaques DDoS, les tentatives de phishing et les anomalies réseau. Il est modulaire, éthique et défensif.

## Structure
- `main.py` : Point d’entrée, collecte email utilisateur
- `ddos_protection.py` : Détection/mitigation DDoS
- `phishing_detector.py` : Détection de liens suspects
- `network_anomaly.py` : Détection d’anomalies réseau
- `logger.py` : Journalisation
- `config.yaml` : Configuration
- `tests/` : Tests unitaires

## Dépendances
- Python 3.8+
- PyYAML
- requests
- scapy
- pytest

## Installation
1. Installe Python 3.8+
2. Installe les dépendances :
   ```powershell
   pip install pyyaml requests scapy pytest
   ```
3. Lance le programme :
   ```powershell
   python main.py
   ```

## Exemple d’exécution
Lance `main.py`, entre ton email, la surveillance démarre et les logs s’affichent.

## Personnalisation
Modifie `config.yaml` pour adapter la protection à ton environnement.
