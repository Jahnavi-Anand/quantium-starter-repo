# SoulFoods Sales Insights 📊

A data analysis and visualization project that transforms raw transaction data into actionable business insights using Python, Pandas, and Dash.

---

## 🚀 Overview

This project analyzes sales data for *Pink Morsels* to answer a key business question:

> **Were sales higher before or after the price increase on January 15, 2021?**

The solution includes:

* Data cleaning and transformation pipeline
* Interactive Dash dashboard
* Automated testing suite
* CI-ready test execution script

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** – Data processing
* **Plotly & Dash** – Data visualization
* **Pytest + Dash Testing** – Testing framework

---

## 📂 Project Structure

```
quantium-starter-repo/
│── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   ├── daily_sales_data_2.csv
│
│── app.py                  # Dash application
│── index.py                # Data processing script
│── formatted_output.csv    # Cleaned dataset
│── test_app.py             # Test suite
│── run_tests.bat           # Windows test runner
│── run_tests.sh            # Bash test runner
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd quantium-starter-repo
```

### 2. Create & activate virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 📊 Run Data Processing

```
python data/index.py
```

Generates:

```
formatted_output.csv
```

---

## 📈 Run Dashboard

```
python app.py
```

Open in browser:

```
http://127.0.0.1:8050/
```

---

## 🧪 Run Tests

### Windows:

```
run_tests.bat
```

### Bash:

```
bash run_tests.sh
```

---

## ✅ Test Coverage

The test suite verifies:

* Header is rendered
* Sales visualization is displayed
* Region filter is functional

---

## 📌 Key Insight

The dashboard clearly shows the sales trend before and after the **January 15, 2021 price increase**, enabling quick business decision-making.

---

## 🎯 Outcome

This project demonstrates:

* End-to-end data pipeline development
* Interactive dashboard design
* Automated testing integration
* CI-ready scripting

---

## 👩‍💻 Author

Jahnavi Anand
