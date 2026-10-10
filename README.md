# 📊 Sales Data Analyzer

## 📌 Project Overview

Sales Data Analyzer is a Python-based data analysis project that helps users explore, analyze, and visualize sales data stored in CSV files. It uses popular Python libraries to perform data operations, generate statistical summaries, handle missing values, and create different types of charts.

This project is designed to practice Python programming, data analysis, and data visualization using real-world sales data.

## ✨ Features

- **Load CSV Data:** Import sales datasets from CSV files.
- **Explore Data:** View the first and last five rows, column names, data types, and dataset information.
- **DataFrame Operations:** Search product categories, sort profits, filter records by country, group sales data, and create pivot tables.
- **Missing Data Handling:** Identify missing values, fill numeric missing values with the mean, remove incomplete rows, or replace missing values with zero.
- **Descriptive Statistics:** Calculate mean, standard deviation, minimum, and maximum values.
- **Data Visualization:** Generate bar plots, line plots, scatter plots, pie charts, histograms, stack plots, and Seaborn heatmaps.
- **Save Charts:** Save generated visualizations as PNG images in the output folder.
- **NumPy Operations:** Perform basic array operations and calculate average profit.
- **Interactive Menu:** Navigate through different features using a simple console-based menu.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## 📂 Project Structure

```text
VISUALIZER/
│
├── data/
│   └── sales_data.csv
│
├── outputs/
│   └── saved charts
│
├── main.py
```

*Note: Adjust the filenames and folders according to your actual repository structure.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Sales-Data-Analyzer
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib seaborn
```

Alternatively, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Add the Dataset

Place your sales CSV file inside the `data` folder and ensure its name and path match the one used in the Python program.

### 5. Run the Program

```bash
python main.py
```

## 📈 Visualizations

The project supports different visualizations to understand sales performance, profit distribution, revenue trends, and country-wise results.

Available charts include:

- Profit by Product Category
- Revenue Trend
- Quantity vs Profit
- Revenue by Country
- Profit Distribution
- Revenue Stack Plot
- Profit Heatmap

Generated charts can be saved as PNG files for future reference.

## 🎯 Learning Objectives

This project demonstrates practical knowledge of Python classes, functions, exception handling, CSV file processing, Pandas DataFrames, NumPy arrays, descriptive statistics, and data visualization.

## 🚀 Future Improvements

- Add a graphical user interface.
- Include more interactive charts.
- Export analysis reports to CSV or PDF.
- Add advanced sales performance comparisons.
- Improve dataset validation and error handling.

## 👨‍💻 Author

Developed as a Python data analysis project to practice programming, data processing, and visualization skills.

## 📄 License

This project is available for educational and learning purposes.
