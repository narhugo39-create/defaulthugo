import pytest
from ddos_protection import DDoSProtection

def test_ddos_blocking():
    ddos = DDoSProtection()
    ip = '1.2.3.4'
    for _ in range(ddos.rate_limit + 1):
        ddos.check_request(ip)
    assert not ddos.check_request(ip)
