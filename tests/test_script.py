import sys
import os
import pandas as pd

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.detection import detect_threats
from src.anomaly_detection import AnomalyDetector
from src.vulnerability_scan import scan_vulnerabilities

# Create results directory if it doesn't exist
results_dir = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(results_dir, exist_ok=True)

# Load sample data
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
data_path = os.path.abspath(data_path)

try:
    data = pd.read_csv(data_path)
    print(data.columns)  # Check the columns in the DataFrame

except FileNotFoundError:
    print(f"File not found: {data_path}")
    sys.exit()
except pd.errors.EmptyDataError:
    print(f"Empty data file: {data_path}")
    sys.exit()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

# Test Threat Detection
print("=== Threat Detection Results ===")
if 'Flow Bytes/s' in data.columns:
    threats = detect_threats(data)
    threats.to_csv(os.path.join(results_dir, 'threat_detection.csv'), index=False)
    if isinstance(threats, pd.DataFrame) and not threats.empty:
        print(threats)
    else:
        print("No threats detected.")
else:
    print("Column 'Flow Bytes/s' not found in data")
    sys.exit()

# Test Anomaly Detection
print("\n=== Anomaly Detection Results ===")
anomaly_detector = AnomalyDetector()
anomaly_detector.train(data)  # Train on the dataset
anomalies = anomaly_detector.detect(data)
anomalies.to_csv(os.path.join(results_dir, 'anomaly_detection.csv'), index=False)
if not anomalies.empty:
    print(anomalies)
else:
    print("No anomalies detected.")

# Test Vulnerability Scan
print("\n=== Vulnerability Scan Results ===")
scan_results = scan_vulnerabilities(data)  # Pass data to the function
scan_results.to_csv(os.path.join(results_dir, 'vulnerability_scan.csv'), index=False)
print(scan_results)
