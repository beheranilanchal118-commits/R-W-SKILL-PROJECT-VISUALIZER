<div align="center">
📊 Sales Data Analyzer & Visualization

---
📝 About the Project
Sales Data Analyzer & Visualization is a Python application that works with sales records stored in a CSV file. It provides a simple terminal menu so users can choose different operations without needing to write a separate command for each task.
The project demonstrates data analysis using Pandas and NumPy, visualization using Matplotlib and Seaborn, and basic Object-Oriented Programming (OOP).
✨ Features
Feature	Description
🔍 Data Exploration	Display the first and last five rows, column names, and data types.
🧹 Missing Data	Find missing values and fill or remove them.
🔎 Search	Search sales records by product category.
↕️ Sort & Filter	Sort by profit and filter records by customer country.
🌍 Grouped Summary	Calculate total revenue and profit for each country.
📋 Pivot Table	Summarize revenue by country and product category.
🔢 NumPy Operations	Convert profit values to an array and perform basic calculations.
📈 Statistics	Calculate mean, standard deviation, minimum, and maximum.
💾 Save Charts	Save generated visualizations as PNG images.
📊 Available Charts
Bar Plot — compare profit across product categories
Line Plot — view revenue trends by date
Scatter Plot — compare quantity and profit
Pie Chart — compare revenue share by country
Histogram — view the distribution of profit values
Stack Plot — display revenue by product category
Heatmap — explore profit across countries and product categories
🧰 Built With
<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge">
  <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-76B900?style=for-the-badge">
</p>
📁 Project Structure
```text
VISUALIZER/
├── data/
│   └── sales_data.csv
├── outputs/
├── main.py
└── README.md
```
`main.py` — main Python program
`data/sales_data.csv` — dataset used by the analyzer
`outputs/` — location for saved chart images
`README.md` — project documentation
⚙️ Installation & Setup
1. Download or clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```
Then open the project folder in VS Code.
2. Install the required libraries
```bash
pip install pandas numpy matplotlib seaborn
```
3. Run the application
Run this command from the `VISUALIZER` folder:
```bash
python main.py
```
The program expects the CSV file to be located at `data/sales_data.csv`. Keep the folder and filename unchanged unless you also update the file path in the code.
🧠 OOP Concepts
The project uses a `SalesDataAnalyzer` class to organize its operations. Class methods are used for loading and exploring data, handling missing values, performing calculations, creating charts, and saving visualizations.
🎓 Learning Outcomes
By working on this project, users can practice:
Reading CSV files with Pandas
Working with DataFrames and NumPy arrays
Searching, sorting, filtering, and grouping data
Handling missing values
Using descriptive statistical functions
Creating plots with Matplotlib and Seaborn
Organizing a Python program with a class
👤 Author
Created as a Python data analysis and visualization project for educational purposes.
---
<div align="center">
Made with Python • Pandas • NumPy • Matplotlib • Seaborn
</div>
