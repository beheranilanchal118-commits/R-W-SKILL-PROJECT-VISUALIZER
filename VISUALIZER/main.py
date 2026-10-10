import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_plot = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)

            if "order_date" in self.data.columns:
                self.data["order_date"] = pd.to_datetime(
                    self.data["order_date"], errors="coerce"
                )

            print("\n" + "=" * 60)
            print("             DATA LOADED SUCCESSFULLY")
            print("=" * 60)
            print("Total rows    :", len(self.data))
            print("Total columns :", len(self.data.columns))

        except FileNotFoundError:
            print("\nCSV file was not found.")
        except Exception as error:
            print("\nError while loading file:", error)

    def press_enter(self):
        input("\nPress Enter to continue...")

    def check_data(self):
        if self.data is None:
            print("\nPlease load the dataset first.")
            return False
        return True

    def heading(self, text):
        print("\n" + "-" * 60)
        print(" " + text)
        print("-" * 60)

    def explore_data(self):
        if not self.check_data():
            return

        while True:
            self.heading("EXPLORE DATA")

            print("1. Show first 5 rows")
            print("2. Show last 5 rows")
            print("3. Show column names")
            print("4. Show data types")
            print("5. Show basic information")
            print("0. Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\nFirst 5 rows:\n")
                print(self.data.head().to_string(index=False))

            elif choice == "2":
                print("\nLast 5 rows:\n")
                print(self.data.tail().to_string(index=False))

            elif choice == "3":
                print("\nColumn Names:\n")
                for column in self.data.columns:
                    print("-", column)

            elif choice == "4":
                print("\nData Types:\n")
                print(self.data.dtypes)

            elif choice == "5":
                print("\nDataset Information")
                print("Rows       :", len(self.data))
                print("Columns    :", len(self.data.columns))
                print("Missing    :", self.data.isnull().sum().sum())
                print("Duplicates :", self.data.duplicated().sum())

            elif choice == "0":
                break

            else:
                print("\nInvalid choice.")

            if choice != "0":
                self.press_enter()

    def dataframe_operations(self):
        if not self.check_data():
            return

        self.heading("DATAFRAME OPERATIONS")

        print("1. Search product category")
        print("2. Sort by profit")
        print("3. Filter by country")
        print("4. Group sales by country")
        print("5. Create pivot table")
        print("6. NumPy array operations")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            category = input("Enter product category: ")

            result = self.data[
                self.data["product_category"].astype(str).str.contains(
                    category, case=False, na=False
                )
            ]

            print("\nMatching records:", len(result))
            print(result.head(10).to_string(index=False))

        elif choice == "2":
            result = self.data.sort_values("profit", ascending=False)

            print("\nTop 10 records by profit:\n")
            print(
                result[
                    ["order_id", "product_category", "revenue", "profit"]
                ].head(10).to_string(index=False)
            )

        elif choice == "3":
            country = input("Enter country: ")

            result = self.data[
                self.data["customer_country"].astype(str).str.lower()
                == country.lower()
            ]

            print("\nRecords found:", len(result))
            print(result.head(10).to_string(index=False))

        elif choice == "4":
            result = self.data.groupby("customer_country")[
                ["revenue", "profit"]
            ].sum().sort_values("profit", ascending=False)

            print("\nCountry-wise sales summary:\n")
            print(result.to_string())

        elif choice == "5":
            result = pd.pivot_table(
                self.data,
                index="customer_country",
                columns="product_category",
                values="revenue",
                aggfunc="sum",
                fill_value=0
            )

            print("\nRevenue Pivot Table:\n")
            print(result.round(2).to_string())

        elif choice == "6":
            numbers = self.data["profit"].to_numpy()

            print("\nNumPy Array Information")
            print("Array shape :", numbers.shape)
            print("First 10 values:")
            print(numbers[:10])

            print("\nFirst 5 values + 100:")
            print(numbers[:5] + 100)

            print("\nAverage profit:", round(np.mean(numbers), 2))

        elif choice == "0":
            return

        else:
            print("\nInvalid choice.")

        self.press_enter()

    def handle_missing_data(self):
        if not self.check_data():
            return

        self.heading("HANDLE MISSING DATA")

        print("1. Display missing values")
        print("2. Fill missing numeric values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with 0")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            missing = self.data.isnull().sum()
            print("\nMissing values:\n")
            print(missing[missing > 0])

            if missing.sum() == 0:
                print("No missing values found.")

        elif choice == "2":
            for column in self.data.select_dtypes(include=np.number).columns:
                self.data[column] = self.data[column].fillna(
                    self.data[column].mean()
                )
            print("\nNumeric missing values filled with mean.")

        elif choice == "3":
            old_rows = len(self.data)
            self.data = self.data.dropna()
            print("\nRows removed:", old_rows - len(self.data))

        elif choice == "4":
            self.data = self.data.fillna(0)
            print("\nMissing values replaced with 0.")

        elif choice == "0":
            return

        else:
            print("\nInvalid choice.")

        self.press_enter()

    def statistics(self):
        if not self.check_data():
            return

        self.heading("DESCRIPTIVE STATISTICS")

        numeric_data = self.data.select_dtypes(include=np.number)

        print("\nMean:\n")
        print(numeric_data.mean().round(2))

        print("\nStandard Deviation:\n")
        print(numeric_data.std().round(2))

        print("\nMinimum:\n")
        print(numeric_data.min().round(2))

        print("\nMaximum:\n")
        print(numeric_data.max().round(2))

        self.press_enter()

    def visualization(self):
        if not self.check_data():
            return

        self.heading("DATA VISUALIZATION")

        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Seaborn Heatmap")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        try:
            plt.figure(figsize=(9, 6))

            if choice == "1":
                data = self.data.groupby("product_category")["profit"].sum()
                data.plot(kind="bar")
                plt.title("Profit by Product Category")
                plt.xlabel("Product Category")
                plt.ylabel("Profit")

            elif choice == "2":
                data = self.data.groupby("order_date")["revenue"].sum()
                data = data.sort_index().head(30)
                data.plot(kind="line")
                plt.title("Revenue Trend")
                plt.xlabel("Date")
                plt.ylabel("Revenue")
                plt.xticks(rotation=45)

            elif choice == "3":
                plt.scatter(
                    self.data["quantity"],
                    self.data["profit"]
                )
                plt.title("Quantity vs Profit")
                plt.xlabel("Quantity")
                plt.ylabel("Profit")

            elif choice == "4":
                data = self.data.groupby("customer_country")["revenue"].sum()
                plt.pie(
                    data,
                    labels=data.index,
                    autopct="%1.1f%%"
                )
                plt.title("Revenue by Country")

            elif choice == "5":
                plt.hist(self.data["profit"], bins=20)
                plt.title("Profit Distribution")
                plt.xlabel("Profit")
                plt.ylabel("Frequency")

            elif choice == "6":
                data = self.data.groupby("product_category")["revenue"].sum()
                plt.stackplot(
                    range(len(data)),
                    data.values,
                    labels=data.index
                )
                plt.title("Revenue Stack Plot")
                plt.legend()

            elif choice == "7":
                data = pd.pivot_table(
                    self.data,
                    index="customer_country",
                    columns="product_category",
                    values="profit",
                    aggfunc="sum",
                    fill_value=0
                )

                sns.heatmap(data, cmap="Blues")
                plt.title("Profit Heatmap")

            elif choice == "0":
                plt.close()
                return

            else:
                plt.close()
                print("\nInvalid choice.")
                self.press_enter()
                return

            plt.tight_layout()
            self.last_plot = plt.gcf()

            print("\nChart created successfully.")
            print("Close the graph window to continue.")
            plt.show()

        except Exception as error:
            plt.close()
            print("\nCould not create graph:", error)

        self.press_enter()

    def save_visualization(self):
        if self.last_plot is None:
            print("\nPlease create a graph first.")
            self.press_enter()
            return

        self.heading("SAVE VISUALIZATION")

        file_name = input(
            "Enter file name (example: profit_chart.png): "
        ).strip()

        if file_name == "":
            file_name = "sales_chart.png"

        if not file_name.lower().endswith(".png"):
            file_name += ".png"

        os.makedirs("outputs", exist_ok=True)

        path = os.path.join("outputs", file_name)
        self.last_plot.savefig(path, dpi=300, bbox_inches="tight")

        print("\nVisualization saved successfully.")
        print("Saved at:", path)

        self.press_enter()

    def run(self):
        while True:
            print("\n" + "=" * 60)
            print("              SALES DATA ANALYZER")
            print("=" * 60)

            if self.data is not None:
                print(
                    f"Records: {len(self.data):,}   "
                    f"Columns: {len(self.data.columns)}"
                )

            print("\n1. Explore Data")
            print("2. DataFrame Operations")
            print("3. Handle Missing Data")
            print("4. Generate Descriptive Statistics")
            print("5. Data Visualization")
            print("6. Save Visualization")
            print("0. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.explore_data()

            elif choice == "2":
                self.dataframe_operations()

            elif choice == "3":
                self.handle_missing_data()

            elif choice == "4":
                self.statistics()

            elif choice == "5":
                self.visualization()

                self.save_visualization()

            elif choice == "0":
                print("\n" + "=" * 60)
                print("              Program closed. Thank you!")
                print("=" * 60)
                break

            else:
                print("\nPlease enter a valid option.")
                self.press_enter()


if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.load_data("data/sales_data.csv")
    analyzer.run()
