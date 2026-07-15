"""
USING PANDAS - Assignment Solutions

SET 1 uses a generic "data.csv" workflow. Because that file may not exist,
Set 1 functions build a small sample DataFrame so the code is runnable, while
still showing the exact pandas calls the assignment asks for.

SET 2 uses the classic Iris dataset, loaded from seaborn if available,
otherwise from a small built-in fallback.
"""

import numpy as np
import pandas as pd


# ======================================================================
# SET 1
# ======================================================================

# ----- Load Data -----
def load_data(path="data.csv"):
    """Load a CSV file named 'data.csv' into a DataFrame called df."""
    # The real assignment call:
    #     df = pd.read_csv("data.csv")
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        # Fallback sample data so the script still runs.
        df = pd.DataFrame({
            "column_name": [5, 12, 8, 20, 3, 15],
            "category": ["A", "B", "A", "C", "B", "A"],
            "date": ["2023-01-05", "2023-02-11", "2023-02-20",
                     "2023-03-15", "2023-03-30", "2023-04-01"],
            "value": [10, np.nan, 30, 40, np.nan, 60],
        })
    return df


# ----- Basic Operations -----
def display_head(df):
    """Display the first 5 rows of the DataFrame."""
    return df.head(5)


# ----- Data Exploration -----
def shape_info(df):
    """Find the number of rows and columns in the DataFrame."""
    rows, cols = df.shape
    return rows, cols


# ----- Filtering Data -----
def filter_data(df):
    """Rows where 'column_name' > 10."""
    df_filtered = df[df["column_name"] > 10]
    return df_filtered


# ----- Handling Missing Data -----
def handle_missing(df):
    """Check for missing values and handle them (fill with column mean)."""
    missing_counts = df.isnull().sum()
    df_filled = df.copy()
    for col in df_filled.select_dtypes(include="number").columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
    return missing_counts, df_filled


# ----- Grouping and Aggregation -----
def group_mean(df):
    """Group by 'category' and calculate the mean value for each group."""
    return df.groupby("category")["value"].mean()


# ----- Merging DataFrames -----
def merge_example():
    """Create two DataFrames with a common key and merge them."""
    df1 = pd.DataFrame({"key": [1, 2, 3], "name": ["Alice", "Bob", "Cara"]})
    df2 = pd.DataFrame({"key": [1, 2, 3], "score": [90, 85, 88]})
    merged = pd.merge(df1, df2, on="key")
    return merged


# ----- Data Visualization -----
def category_bar_chart(df, show=False):
    """Bar chart of counts of unique values in 'category'."""
    counts = df["category"].value_counts()
    if show:
        import matplotlib.pyplot as plt
        counts.plot(kind="bar", title="Category counts")
        plt.xlabel("Category")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    return counts


# ----- Datetime Operations -----
def datetime_month(df):
    """Convert 'date' to datetime and extract the month."""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    return df[["date", "month"]]


# ----- Saving Data -----
def save_data(df, path="output_data.csv"):
    """Save the modified DataFrame to 'output_data.csv'."""
    df.to_csv(path, index=False)
    return path


# ======================================================================
# SET 2 - Iris dataset
# ======================================================================

def load_iris():
    """Load the Iris dataset (seaborn if available, else a small fallback)."""
    try:
        import seaborn as sns
        iris = sns.load_dataset("iris")
    except Exception:
        try:
            from sklearn.datasets import load_iris as skload
            data = skload(as_frame=True)
            iris = data.frame.rename(columns={
                "sepal length (cm)": "sepal_length",
                "sepal width (cm)": "sepal_width",
                "petal length (cm)": "petal_length",
                "petal width (cm)": "petal_width",
            })
            iris["species"] = data.target_names[data.target]
        except Exception:
            iris = pd.DataFrame({
                "sepal_length": [5.1, 4.9, 6.2, 5.9, 6.7, 4.6],
                "sepal_width": [3.5, 3.0, 3.4, 3.0, 3.1, 3.2],
                "petal_length": [1.4, 1.4, 5.4, 5.1, 4.7, 1.5],
                "petal_width": [0.2, 0.2, 2.3, 1.8, 1.5, 0.2],
                "species": ["setosa", "setosa", "virginica",
                            "virginica", "versicolor", "setosa"],
            })
    return iris


# ----- Problem 1: Loading and Exploring Data -----
def iris_head(iris):
    return iris.head()


# ----- Problem 2: Data Selection and Filtering -----
def iris_filter(iris):
    """Sepal length > 5 AND species == setosa."""
    return iris[(iris["sepal_length"] > 5) & (iris["species"] == "setosa")]


# ----- Problem 3: Data Cleaning -----
def iris_clean(iris):
    """Replace missing values with the mean of the respective column."""
    iris = iris.copy()
    num_cols = iris.select_dtypes(include="number").columns
    iris[num_cols] = iris[num_cols].fillna(iris[num_cols].mean())
    return iris


# ----- Problem 4: Grouping and Aggregation -----
def iris_group_stats(iris):
    """Group by species; mean, median, std of each numeric column."""
    return iris.groupby("species").agg(["mean", "median", "std"])


# ----- Problem 5: Merging DataFrames -----
def students_courses_merge():
    """Merge students and courses on a common student_id."""
    students = pd.DataFrame({
        "student_id": [1, 2, 3],
        "name": ["Alice", "Bob", "Cara"],
    })
    courses = pd.DataFrame({
        "student_id": [1, 2, 3],
        "course": ["Math", "Physics", "Chemistry"],
    })
    return pd.merge(students, courses, on="student_id")


# ----- Problem 6: Time Series Analysis -----
def time_series_analysis(show=False):
    """Analyse a synthetic stock-price series: trend + daily returns."""
    dates = pd.date_range("2023-01-01", periods=30, freq="D")
    prices = 100 + np.cumsum(np.random.randn(30))
    df = pd.DataFrame({"date": dates, "price": prices}).set_index("date")
    df["daily_return"] = df["price"].pct_change()
    df["rolling_mean"] = df["price"].rolling(window=5).mean()
    if show:
        import matplotlib.pyplot as plt
        df[["price", "rolling_mean"]].plot(title="Price & 5-day rolling mean")
        plt.tight_layout()
        plt.show()
    return df


# ----- Problem 7: Pivot Tables -----
def sales_pivot():
    """Pivot table: total sales per product category per month."""
    sales = pd.DataFrame({
        "category": ["A", "B", "A", "B", "A", "B"],
        "month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
        "sales": [100, 200, 150, 250, 120, 300],
    })
    return pd.pivot_table(sales, values="sales", index="category",
                          columns="month", aggfunc="sum", fill_value=0)


# ----- Problem 8: Data Visualization -----
def iris_visualizations(iris, show=False):
    """Create a couple of meaningful visualizations of the Iris dataset."""
    if show:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        iris["sepal_length"].plot(kind="hist", bins=15, ax=axes[0],
                                  title="Sepal length histogram")
        iris.plot(kind="scatter", x="sepal_length", y="petal_length",
                  ax=axes[1], title="Sepal vs Petal length")
        plt.tight_layout()
        plt.show()
    # Return summary stats as the "result".
    return iris.describe()


# ----- Problem 9: Data Transformation -----
def iris_transform(iris):
    """New column = square root of an existing numeric column."""
    iris = iris.copy()
    iris["sqrt_sepal_length"] = iris["sepal_length"].apply(np.sqrt)
    return iris[["sepal_length", "sqrt_sepal_length"]]


# ----- Problem 10: Handling Categorical Data -----
def one_hot_encode(iris):
    """Convert the categorical 'species' column to one-hot encoding."""
    return pd.get_dummies(iris, columns=["species"])


# ======================================================================
if __name__ == "__main__":
    pd.set_option("display.width", 120)

    print("========== SET 1 ==========")
    df = load_data()
    print("\nHead:\n", display_head(df))
    print("\nShape (rows, cols):", shape_info(df))
    print("\nFiltered (column_name > 10):\n", filter_data(df))
    missing, filled = handle_missing(df)
    print("\nMissing counts:\n", missing)
    print("\nAfter filling:\n", filled)
    print("\nGroup mean by category:\n", group_mean(df))
    print("\nMerged DataFrames:\n", merge_example())
    print("\nCategory counts:\n", category_bar_chart(df))
    print("\nDatetime month:\n", datetime_month(df))
    saved = save_data(filled)
    print("\nSaved to:", saved)

    print("\n========== SET 2 (Iris) ==========")
    iris = load_iris()
    print("\nIris head:\n", iris_head(iris))
    print("\nFiltered (sepal_length>5 & setosa):\n", iris_filter(iris))
    print("\nCleaned (no nulls remain):", iris_clean(iris).isnull().sum().sum())
    print("\nGroup stats by species:\n", iris_group_stats(iris))
    print("\nStudents-courses merge:\n", students_courses_merge())
    print("\nTime series tail:\n", time_series_analysis().tail())
    print("\nSales pivot:\n", sales_pivot())
    print("\nIris describe:\n", iris_visualizations(iris))
    print("\nSqrt transform:\n", iris_transform(iris).head())
    print("\nOne-hot encoded columns:", list(one_hot_encode(iris).columns))
