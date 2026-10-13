# Data Visualization and Storytelling

**Veda Technology | Data Analytics Internship | Task 4 (Level 1, Day 4)**
**Author:** Rathod Harshvardhansinh J

## Central Question
**Why did Q3 profit dip even though sales kept growing?**

## Approach
1. **Context**: Plotted monthly profit margin to show the Q3 dip.
2. **Problem**: Compared quarterly profit by category and found Furniture was the one that dropped.
3. **Evidence**: Plotted discount vs margin for Furniture; heavy discounts matched low margins.
4. **Recommendation**: Cap Furniture discounts, push high-margin Technology bundles, and track margin by category monthly.

Every chart was built to answer the single question above, with gridlines, 3D effects and extra legends removed.

## Deliverables
| File | Description |
|------|-------------|
| `Data_Visualization_Storytelling.pdf` | 5-page visual story, one takeaway per chart |
| `linkedin_post_image.png` | Image for the LinkedIn post |
| `sample_sales.csv` | Dataset used |
| `build.py` | Python script that reproduces all charts |

## Tools
Python (pandas, matplotlib). The same story can be rebuilt in Power BI or Tableau using `sample_sales.csv`.

## Dataset
Illustrative sample data modeled on a retail (Superstore-style) dataset: 12 months x 3 categories (Furniture, Technology, Office Supplies) with sales, discount and profit. Replace it with the Sample Superstore dataset for real figures.

## How to Run
```bash
pip install pandas matplotlib numpy
python build.py
```

## Key Takeaways
- Total sales grew steadily, but margin fell in Q3.
- Furniture discounts roughly tripled in Q3, and its margin dropped sharply.
- Protecting margin matters more than chasing sales volume.

## Interview Prep
- **Dashboard vs data story:** A dashboard lets you explore many metrics; a data story guides the audience through one question to a conclusion.
- **Choosing a chart:** Match the chart to the insight: line for trend, bar for comparison, scatter for relationship.
- **Non-technical stakeholders:** Start with the business question, show one visual per point, state the takeaway in one sentence, end with an action.

## Connect
#DataAnalytics #DataVisualization #Storytelling #VedaTechnology
