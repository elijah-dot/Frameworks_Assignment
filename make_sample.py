import pandas as pd

# Load only first 1000 rows to keep things light
df = pd.read_csv("metadata.csv", nrows=1000)

# Save as smaller file
df.to_csv("metadata_sample.csv", index=False)

print("✅ Created metadata_sample.csv with 1000 rows")
