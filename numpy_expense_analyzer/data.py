import numpy as np


CSV_FILE = "expenses.csv"


categories = np.array([
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment"
])


budget = np.array([
    5000,
    2500,
    1500,
    2000,
    1000
], dtype=float)


def load_expense_data():
    """
    Load expense data from CSV.

    Returns:
        months: NumPy array of month names
        expenses: 2D NumPy array of expense values
    """

    try:

        data = np.genfromtxt(
            CSV_FILE,
            delimiter=",",
            skip_header=1
        )

        months = np.genfromtxt(
            CSV_FILE,
            delimiter=",",
            skip_header=1,
            usecols=0,
            dtype=str
        )

        expenses = data[:, 1:]

        return months, expenses

    except FileNotFoundError:

        print(
            f"Error: {CSV_FILE} was not found."
        )

        return (
            np.array([]),
            np.empty((0, len(categories)))
        )

    except Exception as error:

        print(
            f"Error loading expense data: {error}"
        )

        return (
            np.array([]),
            np.empty((0, len(categories)))
        )


def save_expense_data(months, expenses):
    """
    Save updated expense data back to CSV.
    """

    try:

        header = ",".join(
            ["Month"] + categories.tolist()
        )

        data_to_save = np.column_stack(
            (months, expenses)
        )

        np.savetxt(
            CSV_FILE,
            data_to_save,
            delimiter=",",
            fmt="%s",
            header=header,
            comments=""
        )

        return True

    except Exception as error:

        print(
            f"Error saving expense data: {error}"
        )

        return False