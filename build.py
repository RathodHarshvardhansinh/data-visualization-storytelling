import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

NAVY, ORANGE, GREY, LIGHT = "#0B1F4B", "#F97316", "#6B7280", "#E5E7EB"
rng = np.random.default_rng(42)
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
cats = {"Furniture": (0.18, 90000), "Technology": (0.22, 120000), "Office Supplies": (0.20, 80000)}

rows = []
for m_i, m in enumerate(months):
    q = m_i // 3 + 1
    for c, (margin, base) in cats.items():
        sales = base * (1 + 0.04 * m_i) * rng.uniform(0.93, 1.07)
        disc = rng.uniform(0.08, 0.14)
        if q == 3 and c == "Furniture":
            disc = rng.uniform(0.28, 0.34)   # heavy discounting
        profit = sales * (margin - 0.85 * (disc - 0.10)) 
        rows.append(dict(Month=m, MonthNo=m_i + 1, Quarter=f"Q{q}", Category=c,
                         Sales=round(sales, 2), Discount=round(disc, 3), Profit=round(profit, 2)))
df = pd.DataFrame(rows)
df.to_csv("/tmp/veda_task4/sample_sales.csv", index=False)

def style(ax):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.grid(False)
    ax.tick_params(colors=GREY)

monthly = df.groupby(["MonthNo", "Month"])[["Sales", "Profit"]].sum().reset_index()
monthly["Margin"] = monthly.Profit / monthly.Sales * 100
qcat = df.groupby(["Quarter", "Category"])["Profit"].sum().unstack()
fur = df[df.Category == "Furniture"]
fur_m = fur.assign(Margin=fur.Profit / fur.Sales * 100)

def header(fig, title, takeaway):
    fig.text(0.06, 0.92, title, fontsize=22, fontweight="bold", color=NAVY)
    fig.text(0.06, 0.855, takeaway, fontsize=13, color=ORANGE)

def chart_margin(ax):
    ax.plot(monthly.Month, monthly.Margin, color=NAVY, lw=3, marker="o")
    ax.axvspan(5.5, 8.5, color=ORANGE, alpha=0.15)
    ax.set_ylabel("Profit margin (%)", color=GREY); style(ax)

def chart_quarter(ax):
    x = np.arange(4); w = 0.26
    for i, (c, col) in enumerate(zip(qcat.columns, [ORANGE, NAVY, "#94A3B8"])):
        ax.bar(x + (i - 1) * w, qcat[c] / 1000, w, label=c, color=col)
    ax.set_xticks(x); ax.set_xticklabels(qcat.index)
    ax.set_ylabel("Profit ($K)", color=GREY); ax.legend(frameon=False); style(ax)

def chart_scatter(ax):
    q3 = fur_m.Quarter == "Q3"
    ax.scatter(fur_m[~q3].Discount * 100, fur_m[~q3].Margin, s=140, color=NAVY, label="Other months")
    ax.scatter(fur_m[q3].Discount * 100, fur_m[q3].Margin, s=140, color=ORANGE, label="Q3")
    ax.set_xlabel("Average discount (%)", color=GREY); ax.set_ylabel("Furniture margin (%)", color=GREY)
    ax.legend(frameon=False); style(ax)

with PdfPages("/tmp/veda_task4/Data_Visualization_Storytelling.pdf") as pdf:
    # 1 title
    fig = plt.figure(figsize=(11, 6.2)); fig.patch.set_facecolor(NAVY)
    fig.text(0.07, 0.62, "Why did Q3 profit dip?", fontsize=40, fontweight="bold", color="white")
    fig.text(0.07, 0.50, "A data story on discounting and margin", fontsize=18, color=ORANGE)
    fig.text(0.07, 0.15, "Rathod Harshvardhansinh J  |  Data Analytics Intern, Veda Technology  |  Task 4",
             fontsize=12, color="white")
    pdf.savefig(fig); plt.close(fig)

    # 2 context
    fig = plt.figure(figsize=(11, 6.2)); header(fig, "1. Context", "Sales kept growing, but profit margin fell in Q3.")
    ax = fig.add_axes([0.08, 0.12, 0.85, 0.65]); chart_margin(ax)
    pdf.savefig(fig); plt.close(fig)

    # 3 problem
    fig = plt.figure(figsize=(11, 6.2)); header(fig, "2. Problem", "Furniture profit dropped sharply in Q3 while other categories held.")
    ax = fig.add_axes([0.08, 0.12, 0.85, 0.65]); chart_quarter(ax)
    pdf.savefig(fig); plt.close(fig)

    # 4 evidence
    fig = plt.figure(figsize=(11, 6.2)); header(fig, "3. Evidence", "Higher discounts lined up with lower Furniture margins.")
    ax = fig.add_axes([0.08, 0.12, 0.85, 0.65]); chart_scatter(ax)
    pdf.savefig(fig); plt.close(fig)

    # 5 recommendation
    fig = plt.figure(figsize=(11, 6.2)); header(fig, "4. Recommendation", "Cap discounts and protect margin on Furniture.")
    pts = ["Set a maximum discount of about 15% on Furniture.",
           "Run promotions on high-margin Technology bundles instead.",
           "Track margin by category monthly, not just total sales."]
    for i, p in enumerate(pts):
        fig.text(0.08, 0.65 - i * 0.14, f"{i+1}.  {p}", fontsize=16, color=NAVY)
    fig.text(0.06, 0.08, "Note: illustrative sample data modeled on a retail (Superstore-style) dataset.",
             fontsize=9, color=GREY)
    pdf.savefig(fig); plt.close(fig)

# LinkedIn image 1200x627
fig = plt.figure(figsize=(12, 6.27), dpi=100); fig.patch.set_facecolor("white")
fig.text(0.05, 0.90, "Why did Q3 profit dip?", fontsize=30, fontweight="bold", color=NAVY)
fig.text(0.05, 0.82, "Heavy Furniture discounting cut margin even as sales grew.", fontsize=15, color=ORANGE)
ax = fig.add_axes([0.07, 0.14, 0.88, 0.58]); chart_margin(ax)
fig.text(0.05, 0.04, "Task 4: Data Visualization & Storytelling  |  Veda Technology", fontsize=10, color=GREY)
fig.savefig("/tmp/veda_task4/linkedin_post_image.png"); plt.close(fig)
print("done")
