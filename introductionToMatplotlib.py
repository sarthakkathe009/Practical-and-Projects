import pandas as pd
import matplotlib.pyplot as plt

sample = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 135, 150, 160, 180, 210],
    "Expenses": [90, 95, 100, 105, 115, 130]
})
sample.to_csv("sales_data.csv", index=False)
print("CSV saved as sales_data.csv")

df = pd.read_csv("sales_data.csv").set_index("Month")
print(df.head())

fig_line, ax_line = plt.subplots(figsize=(6,3))
df[["Sales","Expenses"]].plot(ax=ax_line, marker="o", linewidth=2)
ax_line.set_title("Monthly Sales Vs Expenses")
ax_line.set_ylabel("Amount(₹)")
ax_line.grid(True, linestyle="--",alpha=0.4)
fig_line.tight_layout()
fig_line.savefig("sales_vs_expense.png",dpi=300)
print(plt.show())

df["Profit"] = df["Sales"] - df["Expenses"]
print(df.head())

fig_bar, ax_bar = plt.subplots(figsize=(6,3))
df["Profit"].plot(kind="bar",ax=ax_bar,color="cornflowerblue",edgecolor="black")
ax_bar.set_title("Monthly Profit")
ax_bar.set_xlabel("Month")
ax_bar.set_ylabel("Profit(₹)")
ax_bar.set_xticklabels(df.index, rotation=0)
fig_bar.tight_layout()
fig_bar.savefig("monthly profit.png",dpi=180)
print(plt.show())