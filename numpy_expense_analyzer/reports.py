import matplotlib.pyplot as plt
import numpy as np
import csv
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)


def show_monthly_expense_chart(months, monthly_total):
    plt.figure(figsize=(10, 5))

    plt.plot(
        months,
        monthly_total,
        marker="o"
    )

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Expense (₹)")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def show_category_expense_chart(categories, category_total):
    plt.figure(figsize=(8, 5))

    plt.bar(
        categories,
        category_total
    )

    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Expense (₹)")

    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.show()


def show_category_distribution(categories, category_total):

    plt.figure(figsize=(7, 7))

    plt.pie(
        category_total,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")

    plt.tight_layout()
    plt.show()


def show_budget_comparison(
    categories,
    actual,
    budget
):

    x = np.arange(len(categories))

    width = 0.35

    plt.figure(figsize=(10, 5))

    plt.bar(
        x - width / 2,
        actual,
        width,
        label="Actual"
    )

    plt.bar(
        x + width / 2,
        budget,
        width,
        label="Budget"
    )

    plt.xticks(
        x,
        categories,
        rotation=30
    )

    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")

    plt.title("Actual vs Budget")

    plt.legend()

    plt.tight_layout()
    plt.show()

def export_expense_analysis_pdf(
    months,
    categories,
    expenses,
    budget
):
    # -----------------------------------------
    # Create report folder
    # -----------------------------------------

    report_folder = "expense_reports"

    os.makedirs(
        report_folder,
        exist_ok=True
    )

    # PDF path
    file_path = os.path.join(
        report_folder,
        "overall_expense_analysis.pdf"
    )

    # -----------------------------------------
    # Calculations
    # -----------------------------------------

    monthly_total = np.sum(
        expenses,
        axis=1
    )

    category_total = np.sum(
        expenses,
        axis=0
    )

    total_expense = np.sum(
        expenses
    )

    monthly_budget = np.sum(
        budget
    )

    yearly_budget = monthly_budget * 12

    yearly_variance = (
        total_expense - yearly_budget
    )

    # -----------------------------------------
    # Create PDF
    # -----------------------------------------

    document = SimpleDocTemplate(
        file_path,
        pagesize=landscape(A4),
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontSize=9,
        alignment=TA_CENTER,
        spaceAfter=12
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=8,
        spaceAfter=6
    )

    right_style = ParagraphStyle(
        "RightStyle",
        parent=styles["Normal"],
        alignment=TA_RIGHT
    )

    elements = []

    # -----------------------------------------
    # Title
    # -----------------------------------------

    elements.append(
        Paragraph(
            "PERSONAL EXPENSE ANALYSIS REPORT",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "Overall monthly and category-wise expense analysis",
            subtitle_style
        )
    )

    # -----------------------------------------
    # Summary
    # -----------------------------------------

    elements.append(
        Paragraph(
            "Financial Summary",
            heading_style
        )
    )

    summary_data = [
        [
            "Total Expense",
            "Yearly Budget",
            "Variance",
            "Highest Month",
            "Lowest Month"
        ],
        [
            f"Rs. {total_expense:,.2f}",
            f"Rs. {yearly_budget:,.2f}",
            f"Rs. {yearly_variance:,.2f}",
            months[np.argmax(monthly_total)],
            months[np.argmin(monthly_total)]
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[
            42 * mm,
            42 * mm,
            42 * mm,
            42 * mm,
            42 * mm
        ]
    )

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#EAF2F8")),
            ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
        ])
    )

    elements.append(summary_table)

    elements.append(Spacer(1, 10))

    # -----------------------------------------
    # Monthly Expense Table
    # -----------------------------------------

    elements.append(
        Paragraph(
            "Monthly Expense Breakdown",
            heading_style
        )
    )

    table_header = (
        ["Month"]
        + categories.tolist()
        + [
            "Total Expense",
            "Budget",
            "Variance",
            "Status"
        ]
    )

    table_data = [table_header]

    for i, month in enumerate(months):

        total = monthly_total[i]

        variance = (
            total - monthly_budget
        )

        if variance > 0:
            status = "OVER BUDGET"

        elif variance < 0:
            status = "UNDER BUDGET"

        else:
            status = "ON BUDGET"

        row = (
            [month]
            + [
                f"Rs. {value:,.0f}"
                for value in expenses[i]
            ]
            + [
                f"Rs. {total:,.0f}",
                f"Rs. {monthly_budget:,.0f}",
                f"Rs. {variance:,.0f}",
                status
            ]
        )

        table_data.append(row)

    monthly_table = Table(
        table_data,
        repeatRows=1
    )

    monthly_table.setStyle(
        TableStyle([
            # Header
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1F4E78")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            # Body
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                "Helvetica"
            ),

            (
                "ALIGN",
                (1, 1),
                (-2, -1),
                "RIGHT"
            ),

            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "LEFT"
            ),

            (
                "ALIGN",
                (-1, 1),
                (-1, -1),
                "CENTER"
            ),

            # Grid
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.grey
            ),

            # Alternating rows
            (
                "ROWBACKGROUNDS",
                (0, 1),
                (-1, -1),
                [
                    colors.white,
                    colors.HexColor("#F5F7FA")
                ]
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                5
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                5
            )
        ])
    )

    elements.append(monthly_table)

    elements.append(Spacer(1, 12))

    # -----------------------------------------
    # Category Summary
    # -----------------------------------------

    elements.append(
        Paragraph(
            "Category-wise Expense Summary",
            heading_style
        )
    )

    category_data = [
        [
            "Category",
            "Total Expense",
            "Average / Month",
            "Percentage"
        ]
    ]

    for i, category in enumerate(categories):

        percentage = (
            category_total[i]
            / total_expense
        ) * 100

        category_data.append([
            category,
            f"Rs. {category_total[i]:,.2f}",
            f"Rs. {category_total[i] / len(months):,.2f}",
            f"{percentage:.2f}%"
        ])

    category_table = Table(
        category_data,
        colWidths=[
            55 * mm,
            50 * mm,
            55 * mm,
            40 * mm
        ]
    )

    category_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1F4E78")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (-1, -1),
                "RIGHT"
            ),
            (
                "ROWBACKGROUNDS",
                (0, 1),
                (-1, -1),
                [
                    colors.white,
                    colors.HexColor("#F5F7FA")
                ]
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    elements.append(category_table)

    # -----------------------------------------
    # Final report
    # -----------------------------------------

    document.build(elements)

    return file_path