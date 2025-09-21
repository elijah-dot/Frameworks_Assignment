import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# -----------------------------
# Layout
# -----------------------------
st.title("CORD-19 Data Explorer")
st.write("A simple app to explore COVID-19 research papers metadata")

# Show sample
if st.checkbox("Show raw data"):
    st.dataframe(df.head())

# -----------------------------
# Year Filter
# -----------------------------
years = df['year'].dropna().unique()
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_value=year_min, max_value=year_max, value=(year_min, year_max))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -----------------------------
# Visualization 1: Publications per Year
# -----------------------------
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# -----------------------------
# Visualization 2: Top Journals
# -----------------------------
st.subheader("Top Journals Publishing Papers")
top_journals = filtered['journal'].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)
