import pandas as pd

def detect_threats(data):
    """Simple rule-based threat detection."""
    suspicious_bytes_per_sec = 1000  # Adjust this threshold as needed
    threats = data[data['Flow Bytes/s'] > suspicious_bytes_per_sec]
    return threats
