import numpy as np

from data import categories


def validate_month(month):
    """
    Validate month input.
    """

    valid_months = np.array([
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ])

    matches = np.char.lower(valid_months) == month.lower()

    if np.any(matches):
        return valid_months[np.argmax(matches)]

    return None


def validate_amount(value):
    """
    Validate expense amount.
    """

    try:

        amount = float(value)

        if amount < 0:

            return None

        return amount

    except ValueError:

        return None


def validate_category(category):

    matches = (
        np.char.lower(categories)
        == category.lower()
    )

    if np.any(matches):

        return categories[np.argmax(matches)]

    return None