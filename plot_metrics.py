import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("locust_metrics_stats_history.csv")

# Normalize timestamp
df["Time (s)"] = df["Timestamp"] - df["Timestamp"].iloc[0]

# Plot helper
def plot_metric(col_name, title, ylabel, color):
    if col_name not in df.columns:
        print(f"⚠️ Column '{col_name}' not found. Skipping.")
        return
    plt.figure(figsize=(10, 4))
    plt.plot(df["Time (s)"], df[col_name], label=col_name, color=color)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{col_name.replace('/', '_')}.png")  # Save as image
    plt.close()


# ✅ Core Metrics (matching your CSV)
plot_metric("User Count", "User Count Over Time", "Users", "purple")
plot_metric("Requests/s", "Requests Per Second (RPS)", "RPS", "blue")
plot_metric("Failures/s", "Failures Per Second", "Failures", "red")
plot_metric("Total Average Response Time", "Avg Response Time (ms)", "ms", "orange")
plot_metric("Total Median Response Time", "Median Response Time (ms)", "ms", "green")
plot_metric("Total Min Response Time", "Min Response Time (ms)", "ms", "cyan")
plot_metric("Total Max Response Time", "Max Response Time (ms)", "ms", "magenta")

# ✅ Percentiles (your CSV has them!)
for percentile in ["50%", "66%", "75%", "80%", "90%", "95%", "98%", "99%", "99.9%", "99.99%", "100%"]:
    plot_metric(percentile, f"Response Time {percentile}", "ms", "gray")
