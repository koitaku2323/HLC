import matplotlib.pyplot as plt
import numpy as np

# Data preparation (sample data)
services = ['LC Combined', 'EP Combined', 'E1', 'ST']
total_inqs = [64, 14, 3, 14]
ae_rate = [36, 29, 33, np.nan]  # assuming NaN for missing data
enr_rate = [60, 50, 0, np.nan]  # assuming NaN for missing data
ic_rate = [76, 0, 0, 0]

# Number of metrics
metrics = len(total_inqs)
bar_width = 0.2
index = np.arange(metrics)

# Plotting
plt.figure(figsize=(12, 8))

# Total INQs
plt.bar(index, total_inqs, bar_width, label='Total INQs', color='blue', alpha=0.7)

# AE Rate
plt.bar(index + bar_width, ae_rate, bar_width, label='AE Rate (%)', color='orange', alpha=0.7)

# ENR Rate
plt.bar(index + 2 * bar_width, enr_rate, bar_width, label='ENR Rate (%)', color='green', alpha=0.7)

# IC Rate
plt.bar(index + 3 * bar_width, ic_rate, bar_width, label='IC Rate (%)', color='purple', alpha=0.7)

# Labels and title
plt.xlabel('Services')
plt.ylabel('Percentage / Count')
plt.title('Comparison of Metrics Across Services')
plt.xticks(index + 1.5 * bar_width, services)
plt.legend()

plt.tight_layout()
plt.show()
