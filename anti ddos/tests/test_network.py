import pytest
from network_anomaly import NetworkAnomaly

def test_network_anomaly_init():
    anomaly = NetworkAnomaly()
    assert anomaly.port_scan_threshold > 0
    assert anomaly.traffic_anomaly_threshold > 0
