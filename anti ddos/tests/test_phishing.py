import pytest
from phishing_detector import PhishingDetector

def test_phishing_url():
    detector = PhishingDetector()
    url = 'http://secure-login.com'
    assert detector.is_suspicious_url(url)
