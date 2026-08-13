def show_menu():

    print("\n")
    print("=" * 45)
    print("        PERSONAL EXPENSE ANALYZER")
    print("=" * 45)

    print("1.  Monthly Summary")
    print("2.  Category Analysis")
    print("3.  Budget Analysis")
    print("4.  Expense Ranking")
    print("5.  Statistical Analysis")
    print("6.  Monthly Trend Chart")
    print("7.  Category Expense Chart")
    print("8.  Expense Distribution")
    print("9.  Budget Comparison Chart")
    print("10. Export Expense Analysis PDF")
    print("11. Add New Expense")
    print("12. View Current Expenses")
    print("13. Save Changes")
    print("0.  Exit")

    return input(
        "\nEnter your choice: "
    ).strip()