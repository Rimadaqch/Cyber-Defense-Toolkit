import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.1)

    def train(self, data):
        """Train the anomaly detection model."""
        # Handle NaN and infinity values
        data_clean = data[np.isfinite(data['Flow Bytes/s'])].dropna(subset=['Flow Bytes/s'])
        self.model.fit(data_clean[['Flow Bytes/s']])

    def detect(self, data):
        """Detect anomalies in the dataset."""
        # Handle NaN and infinity values
        data_clean = data[np.isfinite(data['Flow Bytes/s'])].dropna(subset=['Flow Bytes/s'])
        data_clean['anomaly'] = self.model.predict(data_clean[['Flow Bytes/s']])
        anomalies = data_clean[data_clean['anomaly'] == -1]
        return anomalies
