import pandas as pd

df = pd.read_csv("locust_metrics_stats_history.csv")
print("📊 Columns in your CSV:", df.columns.tolist())