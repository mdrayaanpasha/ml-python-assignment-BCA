"""
USING NUMPY - Assignment Solutions
Each function corresponds to one task from the assignment.
Run this file to see the output of every task.
"""

import numpy as np


# ----------------------------------------------------------------------
# Creating Arrays
# ----------------------------------------------------------------------
def create_1d_array():
    """Create a 1D array with elements from 0 to 9."""
    arr = np.arange(10)
    return arr


def create_2d_random_array():
    """Create a 2D array with shape (3, 4) filled with random numbers."""
    arr = np.random.rand(3, 4)
    return arr


# ----------------------------------------------------------------------
# Array Operations
# ----------------------------------------------------------------------
def mean_and_std(arr):
    """Calculate the mean and standard deviation of a given array."""
    return arr.mean(), arr.std()


def normalize(arr):
    """Normalize the values of an array (subtract mean, divide by std)."""
    return (arr - arr.mean()) / arr.std()


# ----------------------------------------------------------------------
# Indexing and Slicing
# ----------------------------------------------------------------------
def third_column(arr_2d):
    """Extract the third column from a 2D array (index 2)."""
    return arr_2d[:, 2]


def reverse_1d(arr):
    """Reverse the order of elements in a 1D array."""
    return arr[::-1]


# ----------------------------------------------------------------------
# Matrix Operations
# ----------------------------------------------------------------------
def matrix_multiplication():
    """Create two matrices (2x3 and 3x4) and perform matrix multiplication."""
    a = np.random.randint(0, 10, size=(2, 3))
    b = np.random.randint(0, 10, size=(3, 4))
    product = a @ b  # result shape (2, 4)
    return a, b, product


def determinant_3x3():
    """Find the determinant of a 3x3 matrix."""
    m = np.array([[2, 1, 1],
                  [1, 3, 2],
                  [1, 0, 0]])
    return m, np.linalg.det(m)


# ----------------------------------------------------------------------
# Generating Arrays
# ----------------------------------------------------------------------
def evenly_spaced():
    """Create a 1D array of 10 evenly spaced values between 0 and 1."""
    return np.linspace(0, 1, 10)


def identity_matrix():
    """Generate a 3x3 identity matrix."""
    return np.eye(3)


# ----------------------------------------------------------------------
# Reshaping and Stacking
# ----------------------------------------------------------------------
def reshape_1d_to_2d():
    """Reshape a 1D array into a 2D array with shape (2, 5)."""
    arr = np.arange(10)
    return arr.reshape(2, 5)


def stack_arrays():
    """Stack two arrays vertically and horizontally."""
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    vertical = np.vstack((a, b))
    horizontal = np.hstack((a, b))
    return vertical, horizontal


# ----------------------------------------------------------------------
# Boolean Indexing
# ----------------------------------------------------------------------
def extract_greater_than_half():
    """Create a random 1D array and extract elements greater than 0.5."""
    arr = np.random.rand(10)
    return arr, arr[arr > 0.5]


def replace_negatives_with_zero():
    """Replace all negative values in an array with 0."""
    arr = np.array([-3, 5, -1, 2, -7, 8])
    result = arr.copy()
    result[result < 0] = 0
    return arr, result


# ----------------------------------------------------------------------
# Statistical Operations
# ----------------------------------------------------------------------
def mean_along_axes():
    """Generate a random 2D array and calculate the mean along each axis."""
    arr = np.random.rand(3, 4)
    return arr, arr.mean(axis=0), arr.mean(axis=1)


def min_and_max(arr):
    """Find the minimum and maximum values in a given array."""
    return arr.min(), arr.max()


# ----------------------------------------------------------------------
# Broadcasting
# ----------------------------------------------------------------------
def add_constant():
    """Add a constant value to each element without using a loop."""
    arr = np.arange(5)
    return arr + 10


def multiply_rows_by_constants():
    """Multiply each row of a 2D array by a different constant."""
    arr = np.ones((3, 4))
    constants = np.array([1, 2, 3]).reshape(3, 1)
    return arr * constants


# ----------------------------------------------------------------------
# Advanced
# ----------------------------------------------------------------------
def apply_custom_function():
    """Apply a custom mathematical operation to each element of an array."""
    def f(x):
        return x ** 2 + 2 * x + 1
    arr = np.arange(5)
    vectorized = np.vectorize(f)
    return arr, vectorized(arr)


def solve_linear_system():
    """
    Solve a system of linear equations:
        2x +  y = 5
         x + 3y = 10
    """
    a = np.array([[2, 1],
                  [1, 3]])
    b = np.array([5, 10])
    solution = np.linalg.solve(a, b)
    return solution


# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("1D array 0..9:\n", create_1d_array())
    print("\n2D (3,4) random:\n", create_2d_random_array())

    sample = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
    print("\nMean & std:", mean_and_std(sample))
    print("Normalized:", normalize(sample))

    grid = np.arange(12).reshape(3, 4)
    print("\nThird column:", third_column(grid))
    print("Reversed 1D:", reverse_1d(create_1d_array()))

    a, b, prod = matrix_multiplication()
    print("\nMatrix mult result shape:", prod.shape)
    m, det = determinant_3x3()
    print("Determinant of 3x3:", round(det, 4))

    print("\nEvenly spaced 0..1:", evenly_spaced())
    print("Identity 3x3:\n", identity_matrix())

    print("\nReshape (2,5):\n", reshape_1d_to_2d())
    v, h = stack_arrays()
    print("Vertical stack:\n", v)
    print("Horizontal stack:", h)

    orig, gt = extract_greater_than_half()
    print("\n>0.5 elements:", gt)
    o, r = replace_negatives_with_zero()
    print("Negatives -> 0:", r)

    arr2d, m0, m1 = mean_along_axes()
    print("\nMean axis 0:", m0)
    print("Mean axis 1:", m1)
    print("Min & max:", min_and_max(sample))

    print("\nAdd constant:", add_constant())
    print("Multiply rows by constants:\n", multiply_rows_by_constants())

    orig, applied = apply_custom_function()
    print("\nCustom f applied:", applied)
    print("Linear system solution [x, y]:", solve_linear_system())
