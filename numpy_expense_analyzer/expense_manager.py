import numpy as np

from data import categories
from validation import (
    validate_month,
    validate_amount,
    validate_category
)


def add_expense(months, expenses):

    print("\n===== ADD EXPENSE =====")

    # -----------------------------------------
    # Month
    # -----------------------------------------

    while True:

        month_input = input(
            "Enter month: "
        ).strip()

        month = validate_month(
            month_input
        )

        if month is not None:
            break

        print(
            "Invalid month. "
            "Example: January"
        )


    # -----------------------------------------
    # Category
    # -----------------------------------------

    print("\nAvailable categories:")

    for category in categories:

        print(
            f"- {category}"
        )

    while True:

        category_input = input(
            "\nEnter category: "
        ).strip()

        category = validate_category(
            category_input
        )

        if category is not None:
            break

        print(
            "Invalid category."
        )


    # -----------------------------------------
    # Amount
    # -----------------------------------------

    while True:

        amount_input = input(
            "Enter amount: ₹"
        ).strip()

        amount = validate_amount(
            amount_input
        )

        if amount is not None:
            break

        print(
            "Please enter a valid "
            "positive amount."
        )


    # -----------------------------------------
    # Find month
    # -----------------------------------------

    month_indexes = (
        np.char.lower(months)
        == month.lower()
    )

    month_exists = np.any(
        month_indexes
    )


    if month_exists:

        month_index = np.argmax(
            month_indexes
        )

        category_index = np.argmax(
            np.char.lower(categories)
            == category.lower()
        )

        expenses[
            month_index,
            category_index
        ] += amount

        print(
            f"\n₹{amount:,.2f} added to "
            f"{category} for {month}."
        )

    else:

        print(
            f"\n{month} does not exist "
            f"in the current dataset."
        )

        print(
            "Please add months to "
            "expenses.csv first."
        )

    return months, expenses

def view_expenses(months, expenses):

    print("\n===== CURRENT EXPENSES =====")

    header = (
        f"{'Month':<12}"
        f"{'Food':>12}"
        f"{'Transport':>12}"
        f"{'Shopping':>12}"
        f"{'Bills':>12}"
        f"{'Entertainment':>16}"
    )

    print(header)
    print("-" * len(header))

    for month, row in zip(
        months,
        expenses
    ):

        values = [
            f"₹{value:,.0f}"
            for value in row
        ]

        print(
            f"{month:<12}"
            f"{values[0]:>12}"
            f"{values[1]:>12}"
            f"{values[2]:>12}"
            f"{values[3]:>12}"
            f"{values[4]:>16}"
        )