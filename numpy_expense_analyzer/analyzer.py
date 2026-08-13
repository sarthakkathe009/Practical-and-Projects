import numpy as np


def calculate_monthly_total(expenses):
    return np.sum(expenses, axis=1)


def calculate_category_total(expenses):
    return np.sum(expenses, axis=0)


def calculate_average_expense(expenses):
    return np.mean(expenses, axis=0)

def calculate_std_expense(expenses):
    return np.std(expenses, axis=0)

def find_highest_spending_month(expenses, months):
    monthly_total = np.sum(expenses, axis=1)
    index = np.argmax(monthly_total)

    return months[index], monthly_total[index]


def find_lowest_spending_month(expenses, months):
    monthly_total = np.sum(expenses, axis=1)
    index = np.argmin(monthly_total)

    return months[index], monthly_total[index]

def compare_with_budget(expenses, budget):
    """
    Compare each month's category expenses
    with the category budget.

    Broadcasting allows the 1D budget array
    to be compared with every row.
    """
    return expenses - budget

def find_overspending(expenses,budget):
    """
    Returns True wherever actual expense
    is greater than the budget.
    """
    return expenses > budget

def calculate_category_percentage(expenses):
    category_total = np.sum(expenses, axis=0)
    total_expense = np.sum(expenses)

    return (category_total / total_expense) * 100

def rank_months(expenses, months):
    monthly_total = np.sum(expenses, axis=1)

    # Sort the indices of the monthly totals in descending order
    ranking_indexes = np.argsort(monthly_total)[::-1]

    return months[ranking_indexes], monthly_total[ranking_indexes]

def spending_status(expenses, budget):
    return np.where(
        expenses > budget,
        "OVER",
        "UNDER"
    )

# -----------------------------------------
# NEW FUNCTIONS
# -----------------------------------------

def find_months_above_average(expenses, months):
    monthly_total = np.sum(expenses, axis=1)

    average_monthly_expense = np.mean(monthly_total)

    result = monthly_total > average_monthly_expense

    return months[result], monthly_total[result]


def find_highest_category(expenses, categories):
    category_total = np.sum(expenses, axis=0)

    index = np.argmax(category_total)

    return categories[index], category_total[index]


def calculate_monthly_change(expenses):
    monthly_total = np.sum(expenses, axis=1)

    return np.diff(monthly_total)


def find_expense_increase(expenses, months):
    monthly_total = np.sum(expenses, axis=1)

    change = np.diff(monthly_total)

    increased = change > 0

    return months[1:][increased], change[increased]


def get_category_ranking(expenses, categories):
    category_total = np.sum(expenses, axis=0)

    indexes = np.argsort(category_total)[::-1]

    return categories[indexes], category_total[indexes]