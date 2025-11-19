from scapy.all import sniff
from logger import log_event
from config import config
import threading

class NetworkAnomaly:
    def __init__(self):
        self.port_scan_threshold = config.get('network', {}).get('port_scan_threshold', 10)
        self.traffic_anomaly_threshold = config.get('network', {}).get('traffic_anomaly_threshold', 10000)
        self.port_counts = {}
        self.packet_count = 0

    def packet_callback(self, pkt):
        self.packet_count += 1
        if hasattr(pkt, 'dport'):
            port = pkt.dport
            self.port_counts[port] = self.port_counts.get(port, 0) + 1
            if self.port_counts[port] > self.port_scan_threshold:
                log_event(f"Scan de port détecté sur {port}")
        if self.packet_count > self.traffic_anomaly_threshold:
            log_event("Trafic réseau inhabituel détecté")
            self.packet_count = 0

    def start(self):
        threading.Thread(target=lambda: sniff(prn=self.packet_callback, store=0), daemon=True).start()
