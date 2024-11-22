import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the results directory
results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))

def visualize_combined_results():
    # Create a figure with subplots
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    
    # Threat Detection Results
    threats_path = os.path.join(results_dir, 'threat_detection.csv')
    threats = pd.read_csv(threats_path)
    sns.countplot(data=threats, x=' Label', order=threats[' Label'].value_counts().index, ax=axes[0])
    axes[0].set_title('Threat Detection Results')
    axes[0].set_xlabel('Threat Label')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)
    
    # Anomaly Detection Results
    anomalies_path = os.path.join(results_dir, 'anomaly_detection.csv')
    anomalies = pd.read_csv(anomalies_path)
    sns.histplot(anomalies['Flow Bytes/s'], bins=50, kde=True, ax=axes[1])
    axes[1].set_title('Anomaly Detection Results')
    axes[1].set_xlabel('Flow Bytes/s')
    axes[1].set_ylabel('Count')

    # Vulnerability Scan Results
    vulnerabilities_path = os.path.join(results_dir, 'vulnerability_scan.csv')
    vulnerabilities = pd.read_csv(vulnerabilities_path)
    sns.countplot(data=vulnerabilities, x='vulnerability', order=vulnerabilities['vulnerability'].value_counts().index, ax=axes[2])
    axes[2].set_title('Vulnerability Scan Results')
    axes[2].set_xlabel('Vulnerability Type')
    axes[2].set_ylabel('Count')
    axes[2].tick_params(axis='x', rotation=45)
    
    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'combined_results.png'))
    plt.show()

if __name__ == "__main__":
    visualize_combined_results()
