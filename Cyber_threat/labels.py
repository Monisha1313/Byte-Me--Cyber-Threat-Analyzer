import pandas as pd

df = pd.read_csv("Cyber_threat/cyber-threat-intelligence_all.csv")

# Get unique labels
labels = df['label'].unique()

print("All Labels:\n")
for l in labels:
    print(l)