# Frameworks_Assignment - CORD-19 Data Explorer
This project is a beginner-friendly data analysis and visualization of the **CORD-19 COVID-19 research dataset**.  
It uses **pandas** for data cleaning, **matplotlib/seaborn** for visualizations, and **Streamlit** to build an interactive web app.

---
## 📌 Features

![Project Screenshot](./images/Screenshot%202025-09-22%20010319.png "Homepage Preview")
![Project Screenshot](./images/Screenshot%202025-09-22%20010348.png "Homepage Preview")



- Load and explore the `metadata.csv` dataset (sampled for performance).
- Clean missing values and convert dates.
- Analyze:
  - Number of publications by year
  - Top publishing journals
  - Word frequency in titles
- Visualize results with clear charts.
- Interactive **Streamlit app** with:
  - Year range slider
  - Filtered charts
  - Data preview

---
## 📌 Overview
This project explores the CORD-19 metadata dataset, which contains information about COVID-19 research papers.  
It demonstrates:
- Data loading, cleaning, and preprocessing using **pandas**
- Exploratory data analysis and visualizations with **matplotlib** and **seaborn**
- An interactive web application built with **Streamlit** for data exploration

## 📂 Project Structure
```
Frameworks_Assignment/
├── data/
│   └── metadata.csv           # CORD-19 metadata file (not included, see below)
├── app.py                     # Streamlit application
├── analysis.ipynb             # Jupyter notebook for EDA and visualization
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 How to Run

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Frameworks_Assignment
    ```

2. **Download the CORD-19 metadata:**
    - Visit [CORD-19 Dataset](https://www.semanticscholar.org/cord19/download) and download the latest `metadata.csv`.
    - Place `metadata.csv` in the `data/` directory.

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

5. **(Optional) Explore the analysis notebook:**
    - Open `analysis.ipynb` in Jupyter Notebook or VS Code.

## 🛠️ Features

- **Data Cleaning:** Handles missing values, filters relevant columns, and standardizes data.
- **Visualizations:** 
  - Publication trends over time
  - Top journals and authors
  - Keyword and topic analysis
- **Interactive App:** 
  - Filter papers by year, journal, or author
  - Search and explore metadata

## 📦 Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- streamlit

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 📑 Notes

- The dataset (`metadata.csv`) is not included due to size and licensing. Please download it manually.
- For questions or issues, open an issue in this repository.

## 📄 License

This project is for educational purposes.  
CORD-19 dataset is provided by the Allen Institute for AI under its [terms of use](https://www.semanticscholar.org/cord19/download).

