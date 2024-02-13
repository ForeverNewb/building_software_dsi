import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

df = pd.read_csv('ttc-bus-delay-data-2023.csv')

unique_routes = df['Incident'].unique()


# Count the occurrences of each incident
incident_counts = df['Incident'].value_counts()

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a bar plot with alternating colors
colors = ['b', 'g'] * (len(incident_counts) // 2 + len(incident_counts) % 2)
ax.barh(incident_counts.index, incident_counts, color=colors)

# Set the labels
ax.set_xlabel('Number of Occurrences')
ax.set_ylabel('Incident')

plt.savefig('incident_counts.png', bbox_inches='tight')

# Show the plot
plt.show()

