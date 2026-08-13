from data import (
    load_expense_data,
    save_expense_data,
    categories,
    budget
)

from expense_manager import (
    add_expense,
    view_expenses
)

from analyzer import (
    calculate_monthly_total,
    calculate_category_total,
    calculate_average_expense,
    calculate_std_expense,
    find_highest_spending_month,
    find_lowest_spending_month,
    compare_with_budget,
    calculate_category_percentage,
    rank_months,
    find_highest_category,
    find_months_above_average,
    get_category_ranking
)

from reports import (
    show_monthly_expense_chart,
    show_category_expense_chart,
    show_category_distribution,
    show_budget_comparison,
    export_expense_analysis_pdf
)

from menu import show_menu


# -----------------------------------------
# Pre-calculate common values
# -----------------------------------------

months, expenses = load_expense_data()


# -----------------------------------------
# Main Application
# -----------------------------------------

while True:

    choice = show_menu()

    # Recalculate analysis from latest expenses
    monthly_total = calculate_monthly_total(expenses)

    category_total = calculate_category_total(expenses)

    average_expense = calculate_average_expense(expenses)

    std_expense = calculate_std_expense(expenses)

    # -------------------------------------
    # 1. Monthly Summary
    # -------------------------------------

    if choice == "1":

        print("\n--- Monthly Summary ---")

        for month, total in zip(
            months,
            monthly_total
        ):
            print(
                f"{month:<10} ₹{total:,.2f}"
            )

        highest_month, highest_amount = (
            find_highest_spending_month(
                expenses,
                months
            )
        )

        lowest_month, lowest_amount = (
            find_lowest_spending_month(
                expenses,
                months
            )
        )

        print(
            f"\nHighest : {highest_month} "
            f"₹{highest_amount:,.2f}"
        )

        print(
            f"Lowest  : {lowest_month} "
            f"₹{lowest_amount:,.2f}"
        )


    # -------------------------------------
    # 2. Category Analysis
    # -------------------------------------

    elif choice == "2":

        print("\n--- Category Analysis ---")

        for category, total, average in zip(
            categories,
            category_total,
            average_expense
        ):

            print(
                f"{category:<15}"
                f" Total: ₹{total:,.2f}"
                f" | Avg: ₹{average:,.2f}"
            )

        highest_category, amount = (
            find_highest_category(
                expenses,
                categories
            )
        )

        print(
            f"\nHighest category: "
            f"{highest_category} → ₹{amount:,.2f}"
        )


    # -------------------------------------
    # 3. Budget Analysis
    # -------------------------------------

    elif choice == "3":

        print("\n--- Budget Analysis ---")

        difference = compare_with_budget(
            expenses,
            budget
        )

        for index, category in enumerate(
            categories
        ):

            actual = category_total[index]

            yearly_budget = budget[index] * 12

            diff = actual - yearly_budget

            if diff > 0:

                print(
                    f"{category:<15} "
                    f"OVER by ₹{diff:,.2f}"
                )

            elif diff < 0:

                print(
                    f"{category:<15} "
                    f"UNDER by ₹{abs(diff):,.2f}"
                )

            else:

                print(
                    f"{category:<15} "
                    f"EXACT budget"
                )


    # -------------------------------------
    # 4. Expense Ranking
    # -------------------------------------

    elif choice == "4":

        print("\n--- Monthly Ranking ---")

        ranked_months, ranked_values = (
            rank_months(
                expenses,
                months
            )
        )

        for position, (
            month,
            amount
        ) in enumerate(
            zip(
                ranked_months,
                ranked_values
            ),
            start=1
        ):

            print(
                f"{position}. "
                f"{month:<10} "
                f"₹{amount:,.2f}"
            )


        print("\n--- Category Ranking ---")

        ranked_categories, ranked_category_values = (
            get_category_ranking(
                expenses,
                categories
            )
        )

        for position, (
            category,
            amount
        ) in enumerate(
            zip(
                ranked_categories,
                ranked_category_values
            ),
            start=1
        ):

            print(
                f"{position}. "
                f"{category:<15} "
                f"₹{amount:,.2f}"
            )


    # -------------------------------------
    # 5. Statistical Analysis
    # -------------------------------------

    elif choice == "5":

        print("\n--- Statistical Analysis ---")

        for category, average, std in zip(
            categories,
            average_expense,
            std_expense
        ):

            print(
                f"{category:<15}"
                f" Mean: ₹{average:,.2f}"
                f" | STD: ₹{std:,.2f}"
            )


        above_months, above_values = (
            find_months_above_average(
                expenses,
                months
            )
        )

        print(
            "\nMonths above average:"
        )

        for month, value in zip(
            above_months,
            above_values
        ):

            print(
                f"{month:<10} "
                f"₹{value:,.2f}"
            )


    # -------------------------------------
    # 6. Monthly Chart
    # -------------------------------------

    elif choice == "6":

        show_monthly_expense_chart(
            months,
            monthly_total
        )


    # -------------------------------------
    # 7. Category Chart
    # -------------------------------------

    elif choice == "7":

        show_category_expense_chart(
            categories,
            category_total
        )


    # -------------------------------------
    # 8. Pie Chart
    # -------------------------------------

    elif choice == "8":

        show_category_distribution(
            categories,
            category_total
        )


    # -------------------------------------
    # 9. Budget Chart
    # -------------------------------------

    elif choice == "9":

        show_budget_comparison(
            categories,
            category_total,
            budget * 12
        )

    # -------------------------------------
    # 10. Export PDF Report
    # -------------------------------------

    elif choice == "10":

        file_path = export_expense_analysis_pdf(
            months,
            categories,
            expenses,
            budget
        )

        print(
            "\nExpense analysis PDF generated successfully!"
        )

        print(
            f"File saved at: {file_path}"
        )
    
    elif choice == "11":

        months, expenses = add_expense(
            months,
            expenses
        )

    elif choice == "12":

        view_expenses(
            months,
            expenses
        )

    elif choice == "13":

        success = save_expense_data(
            months,
            expenses
        )

        if success:

            print(
                "\nChanges saved successfully!"
            )

        else:

            print(
                "\nFailed to save changes."
            )

    # -------------------------------------
    # 0. Exit
    # -------------------------------------

    elif choice == "0":

        print(
            "\nThank you for using "
            "Personal Expense Analyzer!"
        )

        break


    else:

        print(
            "\nInvalid choice."
            " Please select 0-9."
        )