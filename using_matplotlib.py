"""
USING MATPLOTLIB - Assignment Solutions

Each function creates one plot from the assignment. Running this file will
produce every figure. Set SHOW = True to display interactively, or leave it
False to save each plot as a PNG into the 'matplotlib_outputs' folder.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (enables 3d projection)

SHOW = False
OUTDIR = "matplotlib_outputs"


def _finish(fig, name):
    """Show or save the figure depending on SHOW."""
    if SHOW:
        plt.show()
    else:
        os.makedirs(OUTDIR, exist_ok=True)
        fig.savefig(os.path.join(OUTDIR, name), dpi=100, bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------------
# 1. Basic Line Plot: y = x^2 for x in [0, 5]
# ----------------------------------------------------------------------
def basic_line_plot():
    x = np.linspace(0, 5, 100)
    y = x ** 2
    fig, ax = plt.subplots()
    ax.plot(x, y, color="blue")
    ax.set_title("Line Plot of y = x^2")
    ax.set_xlabel("x")
    ax.set_ylabel("y = x^2")
    _finish(fig, "01_line_plot.png")


# ----------------------------------------------------------------------
# 2. Scatter Plot with Labels
# ----------------------------------------------------------------------
def scatter_plot():
    x1, y1 = np.random.rand(50), np.random.rand(50)
    x2, y2 = np.random.rand(50), np.random.rand(50)
    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color="red", label="Set 1")
    ax.scatter(x2, y2, color="green", label="Set 2")
    ax.set_title("Scatter Plot of Two Data Sets")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    _finish(fig, "02_scatter_plot.png")


# ----------------------------------------------------------------------
# 3. Histogram with 20 bins
# ----------------------------------------------------------------------
def histogram():
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="purple", edgecolor="black")
    ax.set_title("Histogram (20 bins)")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    _finish(fig, "03_histogram.png")


# ----------------------------------------------------------------------
# 4. Bar Chart of product sales
# ----------------------------------------------------------------------
def bar_chart():
    products = ["A", "B", "C", "D"]
    sales = [120, 90, 150, 60]
    fig, ax = plt.subplots()
    ax.bar(products, sales, color="teal")
    ax.set_title("Product Sales")
    ax.set_xlabel("Product")
    ax.set_ylabel("Units Sold")
    _finish(fig, "04_bar_chart.png")


# ----------------------------------------------------------------------
# 5. Multiple Subplots: sin line + scatter
# ----------------------------------------------------------------------
def multiple_subplots():
    x = np.linspace(0, 2 * np.pi, 100)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(x, np.sin(x), color="blue")
    ax1.set_title("y = sin(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("sin(x)")

    ax2.scatter(np.random.rand(50), np.random.rand(50), color="orange")
    ax2.set_title("Random Scatter")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")

    fig.tight_layout()
    _finish(fig, "05_subplots.png")


# ----------------------------------------------------------------------
# 6. Customizing Plot Appearance (title, labels, grid)
# ----------------------------------------------------------------------
def customized_plot():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color="darkred", linewidth=2)
    ax.set_title("Customized Cosine Plot")
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.grid(True, linestyle="--", alpha=0.6)
    _finish(fig, "06_customized_plot.png")


# ----------------------------------------------------------------------
# 7. Box Plot
# ----------------------------------------------------------------------
def box_plot():
    data = [np.random.normal(0, std, 100) for std in (1, 2, 3)]
    fig, ax = plt.subplots()
    ax.boxplot(data, tick_labels=["std=1", "std=2", "std=3"])
    ax.set_title("Box Plot of Three Distributions")
    ax.set_ylabel("Value")
    _finish(fig, "07_box_plot.png")


# ----------------------------------------------------------------------
# 8. Pie Chart
# ----------------------------------------------------------------------
def pie_chart():
    categories = ["Category A", "Category B", "Category C", "Category D"]
    sizes = [35, 25, 25, 15]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=categories, autopct="%1.1f%%", startangle=90)
    ax.set_title("Category Distribution")
    ax.axis("equal")
    _finish(fig, "08_pie_chart.png")


# ----------------------------------------------------------------------
# 9. 3D Surface Plot: z = sin(sqrt(x^2 + y^2))
# ----------------------------------------------------------------------
def surface_plot_3d():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x ** 2 + y ** 2))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(x, y, z, cmap="viridis")
    ax.set_title("3D Surface: z = sin(sqrt(x^2 + y^2))")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    fig.colorbar(surf, shrink=0.5, aspect=10)
    _finish(fig, "09_surface_3d.png")


# ----------------------------------------------------------------------
# 10. Error Bars
# ----------------------------------------------------------------------
def error_bars():
    x = np.arange(1, 11)
    y = np.random.rand(10) * 10
    yerr = np.random.rand(10) * 2
    fig, ax = plt.subplots()
    ax.errorbar(x, y, yerr=yerr, fmt="-o", capsize=4, color="navy",
                ecolor="gray")
    ax.set_title("Line Plot with Error Bars")
    ax.set_xlabel("Data point")
    ax.set_ylabel("Mean value")
    _finish(fig, "10_error_bars.png")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    tasks = [
        basic_line_plot,
        scatter_plot,
        histogram,
        bar_chart,
        multiple_subplots,
        customized_plot,
        box_plot,
        pie_chart,
        surface_plot_3d,
        error_bars,
    ]
    for task in tasks:
        print(f"Running {task.__name__} ...")
        task()
    if not SHOW:
        print(f"\nAll figures saved to '{OUTDIR}/'")
    else:
        print("\nDone.")
