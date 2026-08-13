# Personal Expense Analyzer

A portfolio-ready **intermediate-level Python data analysis project** built around **NumPy**. The application reads expense data from CSV, performs numerical and statistical analysis, provides interactive expense management, generates visualizations with Matplotlib, and exports a professionally formatted PDF report.

---

## 1. Project Overview

The **Personal Expense Analyzer** is a command-line expense management and analytics application.

The main goal of this project is to demonstrate how NumPy can be used for real-world data processing instead of only basic array manipulation.

The application can:

- Load expense data from a CSV file.
- Store and process the expense dataset using NumPy arrays.
- Calculate monthly and category-wise expenses.
- Calculate averages and standard deviation.
- Detect high and low spending periods.
- Compare expenses against monthly budgets.
- Detect over-budget spending.
- Rank months and expense categories.
- Identify months with above-average spending.
- Calculate month-to-month expense changes.
- Display expense charts using Matplotlib.
- Accept new expenses from the user.
- Validate user input.
- Save updated expense data back to CSV.
- Generate a professional PDF expense report.
- Handle common file and input errors.

---

# 2. Project Objectives

This project was developed to practice and demonstrate:

1. NumPy fundamentals and intermediate operations.
2. Vectorized numerical computation.
3. Array indexing and slicing.
4. Broadcasting.
5. Boolean masking.
6. Statistical analysis.
7. Data loading and saving.
8. Modular Python programming.
9. Input validation and exception handling.
10. Data visualization.
11. Report generation.
12. Building a complete command-line mini application.

---

# 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical processing and data analysis |
| Matplotlib | Data visualization |
| ReportLab | PDF report generation |
| CSV | Persistent expense data storage |

---

# 4. Project Structure

```text
numpy_expense_analyzer/
│
├── main.py
├── data.py
├── analyzer.py
├── reports.py
├── menu.py
├── validation.py
├── expense_manager.py
├── expenses.csv
│
├── expense_reports/
│   └── overall_expense_analysis.pdf
│
└── README.md
```

---

# 5. File Responsibilities

## `main.py`

The main entry point of the application.

Responsibilities:

- Starts the application.
- Displays the menu.
- Handles user choices.
- Recalculates analysis using the latest expense data.
- Connects the data, analysis, validation, management, and reporting modules.

---

## `data.py`

Handles data loading and saving.

Responsibilities:

- Defines expense categories.
- Defines monthly budgets.
- Loads expense data from `expenses.csv`.
- Saves updated expense data to `expenses.csv`.

Important NumPy functions:

```python
np.genfromtxt()
np.column_stack()
np.savetxt()
```

---

## `analyzer.py`

Contains the main NumPy-based analysis functions.

Responsibilities:

- Monthly expense totals.
- Category totals.
- Average expense.
- Standard deviation.
- Highest and lowest spending month.
- Budget comparison.
- Overspending detection.
- Category percentage contribution.
- Monthly ranking.
- Category ranking.
- Above-average month detection.
- Month-to-month change analysis.

---

## `reports.py`

Responsible for visualization and PDF generation.

Responsibilities:

- Monthly expense trend chart.
- Category expense bar chart.
- Expense distribution pie chart.
- Actual vs budget comparison chart.
- Professional PDF expense report.

Libraries used:

```python
matplotlib
reportlab
numpy
```

---

## `menu.py`

Contains the command-line menu and keeps the user interface separate from the business logic.

---

## `validation.py`

Handles input validation for:

- Month names.
- Expense categories.
- Expense amounts.

---

## `expense_manager.py`

Handles interactive expense operations:

- Add a new expense.
- Update an existing month/category amount.
- View the current expense dataset.

---

## `expenses.csv`

The main source data file.

Example:

```csv
Month,Food,Transport,Shopping,Bills,Entertainment
January,4500,2200,1200,1800,900
February,5200,2100,1500,1900,1100
March,4800,2500,1300,2100,950
```

---

## `expense_reports/`

Contains generated reports.

Example:

```text
expense_reports/
└── overall_expense_analysis.pdf
```

---

# 6. Data Model

The application uses a 2D NumPy array.

Example:

```python
expenses = np.array([
    [4500, 2200, 1200, 1800, 900],
    [5200, 2100, 1500, 1900, 1100],
    [4800, 2500, 1300, 2100, 950]
])
```

The structure is:

```text
                 Food  Transport  Shopping  Bills  Entertainment

January           4500    2200       1200    1800      900
February          5200    2100       1500    1900     1100
March             4800    2500       1300    2100      950
```

### Shape

```python
expenses.shape
```

For 12 months and 5 categories:

```text
(12, 5)
```

This means:

- 12 rows = months
- 5 columns = categories

---

# 7. NumPy Concepts Used

This project intentionally uses a broad range of NumPy concepts.

## 7.1 NumPy Arrays

```python
np.array()
```

Used to represent categories, budgets, months, and expense values.

## 7.2 2D Arrays

The expense dataset is represented as a matrix:

```python
expenses[row, column]
```

Example:

```python
expenses[0, 0]
```

Accesses January's Food expense.

## 7.3 Array Slicing

```python
data[:, 1:]
```

Meaning:

- `:` → all rows
- `1:` → all columns starting from index 1

This removes the Month column and keeps numeric expense columns.

## 7.4 Axis

### Category totals

```python
np.sum(expenses, axis=0)
```

`axis=0` works vertically through the rows.

### Monthly totals

```python
np.sum(expenses, axis=1)
```

`axis=1` works horizontally across columns.

## 7.5 Mean

```python
np.mean(expenses, axis=0)
```

Calculates the average spending for every category.

## 7.6 Standard Deviation

```python
np.std(expenses, axis=0)
```

Measures how much spending varies in each category.

## 7.7 Maximum and Minimum Index

```python
np.argmax()
np.argmin()
```

Used to locate highest/lowest spending month and category.

## 7.8 Broadcasting

```python
expenses - budget
```

Applies the 1D budget array to every row of the 2D expense array automatically.

## 7.9 Boolean Masking

```python
expenses > budget
```

Returns a Boolean matrix used for overspending detection.

## 7.10 `np.where()`

```python
np.where(
    expenses > budget,
    "OVER",
    "UNDER"
)
```

Converts conditions into readable results.

## 7.11 `np.argsort()`

```python
indexes = np.argsort(monthly_total)[::-1]
```

Used for monthly and category rankings.

## 7.12 `np.diff()`

```python
np.diff(monthly_total)
```

Calculates month-to-month expense changes.

## 7.13 `np.any()`

Used during validation and condition checking.

## 7.14 `np.char.lower()`

Used for case-insensitive comparisons on string arrays.

## 7.15 `np.genfromtxt()`

Loads CSV data into NumPy arrays.

## 7.16 `np.savetxt()`

Saves updated NumPy data back to CSV.

## 7.17 `np.column_stack()`

Combines month names and expense data before saving.

---

# 8. Application Features

## 8.1 Monthly Summary

Displays every month's expense, highest spending month, and lowest spending month.

## 8.2 Category Analysis

Displays total, average, and highest spending category.

## 8.3 Budget Analysis

Compares actual spending against monthly category budgets and identifies over/under budget categories.

## 8.4 Expense Ranking

Ranks months and categories by spending.

## 8.5 Statistical Analysis

Displays mean, standard deviation, and months above average spending.

## 8.6 Visualizations

Provides:

1. Monthly expense trend.
2. Category-wise expenses.
3. Expense distribution.
4. Actual vs budget comparison.

## 8.7 Add New Expense

The user can enter a month, category, and amount. The amount is added to the selected month/category cell.

## 8.8 View Current Expenses

Displays the current in-memory expense matrix as a readable table.

## 8.9 Save Changes

Changes remain in memory until the user selects **Save Changes**, which writes the updated data to `expenses.csv`.

## 8.10 PDF Report

Generates `expense_reports/overall_expense_analysis.pdf` with:

- Financial summary.
- Monthly expense table.
- Budget and variance information.
- Category-wise summary.
- Average monthly category expense.
- Percentage contribution.

---

# 9. Application Menu

```text
=============================================
        PERSONAL EXPENSE ANALYZER
=============================================

1.  Monthly Summary
2.  Category Analysis
3.  Budget Analysis
4.  Expense Ranking
5.  Statistical Analysis
6.  Monthly Trend Chart
7.  Category Expense Chart
8.  Expense Distribution
9.  Budget Comparison Chart
10. Export Expense Analysis PDF
11. Add New Expense
12. View Current Expenses
13. Save Changes
0.  Exit
```

---

# 10. Program Workflow

```text
Start Application
       |
       v
Load expenses.csv
       |
       v
Create NumPy arrays
       |
       v
Display Main Menu
       |
       +--------------------------+
       |                          |
       v                          v
   Analysis                  Manage Expenses
       |                          |
       |                          v
       |                    Validate Input
       |                          |
       |                          v
       |                     Modify Array
       +------------+-------------+
                    |
                    v
             Save Changes
                    |
                    v
              Update CSV
                    |
                    v
              Generate PDF
                    |
                    v
                  Exit
```

---

# 11. Installation

## Step 1: Create a virtual environment

Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 2: Install dependencies

```bash
pip install numpy matplotlib reportlab
```

---

# 12. Running the Application

```bash
python main.py
```

The application will display the interactive menu.

---

# 13. Example Usage

### Adding an expense

```text
11

===== ADD EXPENSE =====

Enter month: August

Available categories:
- Food
- Transport
- Shopping
- Bills
- Entertainment

Enter category: Food
Enter amount: ₹750

₹750.00 added to Food for August.
```

### Saving changes

```text
13

Changes saved successfully!
```

### Exporting a PDF

```text
10

Expense analysis PDF generated successfully!

File saved at:
expense_reports/overall_expense_analysis.pdf
```

---

# 14. Validation and Exception Handling

The project handles common errors such as:

- Invalid amount.
- Negative amount.
- Invalid month.
- Invalid category.
- Missing CSV file.
- CSV save errors.

Examples:

```text
Enter amount: ₹abc
Please enter a valid positive amount.
```

```text
Enter amount: ₹-500
Please enter a valid positive amount.
```

```text
Enter month: Januarry
Invalid month. Example: January
```

---

# 15. Why This Is an Intermediate NumPy Project

The project goes beyond basic array examples by combining multiple NumPy concepts inside a real-world application.

The overall pipeline is:

```text
Raw CSV Data
     ↓
NumPy Arrays
     ↓
Vectorized Operations
     ↓
Statistical Analysis
     ↓
Filtering / Ranking
     ↓
Visualization
     ↓
Reporting
```

The key focus is learning to think in arrays and vectorized operations rather than performing every calculation with explicit Python loops.

---

# 16. Key Learning Outcomes

After completing this project, you should understand:

- NumPy arrays.
- 1D vs 2D arrays.
- `axis=0` and `axis=1`.
- Array slicing and indexing.
- Broadcasting.
- Boolean masking.
- Vectorized calculations.
- Statistical functions.
- Sorting and ranking with NumPy.
- CSV loading and saving.
- Modular Python applications.
- Input validation.
- Exception handling.
- Data visualization.
- PDF report generation.

---

# 17. Future Improvements

A stronger next version could replace the fixed month/category matrix with an individual transaction model:

```text
Date        Category       Description       Amount
12-08-2026  Food            Lunch             250
12-08-2026  Transport       Auto              180
13-08-2026  Shopping        T-shirt           899
```

Potential upgrades:

- Daily expense tracking.
- Multiple transactions per category.
- Date filtering.
- Custom date ranges.
- Transaction search.
- Transaction editing/deletion.
- Monthly and yearly reports.
- SQLite database.
- Pandas integration.
- Web interface using Flask or Django.
- Interactive dashboard.
- Excel export.
- Automated monthly reports.
- Expense forecasting.
- Anomaly detection.
- Machine-learning-based spending predictions.

---

# 18. Project Status

```text
✅ NumPy-based data processing
✅ CSV data loading
✅ CSV data saving
✅ Interactive CLI
✅ Expense validation
✅ Exception handling
✅ Monthly analysis
✅ Category analysis
✅ Budget analysis
✅ Statistical analysis
✅ Expense rankings
✅ NumPy broadcasting
✅ Boolean masking
✅ Vectorized operations
✅ Matplotlib visualizations
✅ PDF report generation
✅ Expense management
```

---

# 19. Author

**Personal Expense Analyzer**

Built as an intermediate Python + NumPy mini project focused on practical data analysis, numerical computing, visualization, and reporting.

---

## License

This project is intended for educational and portfolio purposes.
