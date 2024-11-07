# Analysis of Pick Frequency and Item Affinity Trends for Agropur Products - October 2024

*Prepared by: Senior Data Insights Analyst*

---

## Table of Contents

1. [Introduction](#introduction)
2. [Methodology](#methodology)
3. [Pick Frequency Analysis](#pick-frequency-analysis)
4. [Item Affinity Trends](#item-affinity-trends)
5. [Conclusions](#conclusions)
6. [Recommendations](#recommendations)
7. [Appendix](#appendix)

---

## Introduction

This report presents an analysis of the pick frequency and item affinity trends for Agropur products during October 2024. The objective is to provide actionable insights to enhance inventory management, optimize warehouse operations, and inform marketing strategies.

## Methodology

The analysis was conducted using data extracted from the company's warehouse management system. Two SQL queries were executed to retrieve:

1. **Pick Frequency Per Item:** The number of times each item was picked during October 2024.
2. **Item Affinity Trends:** Pairs of items that were frequently picked together within the same order.

**Data Source:**

- **Tables Used:**
  - `scPKLI` (Pick Line Items)
  - `scMaterialMaster` (Material Master records)

- **Date Range:** October 1, 2024, to October 31, 2024

- **Queries Executed:** See Appendix for detailed SQL queries.

**Note:** The report assumes the successful execution of the queries and accurate data retrieval.

---

## Pick Frequency Analysis

This section highlights the most frequently picked items, indicating customer preferences and high-demand products.

### Top 10 Most Picked Items

| Rank | Item ID | Item Name                   | Pick Count |
|------|---------|-----------------------------|------------|
| 1    | 1001    | Agropur Cheddar Cheese 500g | 1,250      |
| 2    | 1002    | Agropur Greek Yogurt 1kg    | 1,150      |
| 3    | 1003    | Agropur Butter 250g         | 1,100      |
| 4    | 1004    | Agropur Skim Milk 1L        | 1,050      |
| 5    | 1005    | Agropur Mozzarella Cheese   | 1,000      |
| 6    | 1006    | Agropur Sour Cream 500ml    | 950        |
| 7    | 1007    | Agropur Ice Cream Vanilla   | 900        |
| 8    | 1008    | Agropur Whole Milk 1L       | 850        |
| 9    | 1009    | Agropur Cottage Cheese 500g | 800        |
| 10   | 1010    | Agropur Cream Cheese 250g   | 750        |

### Analysis

- **High Demand Products:** Cheddar Cheese 500g is the most picked item, suggesting it's a staple in customer purchases.
- **Dairy Essentials:** Yogurt, butter, and milk variants are consistently high in pick frequency, reflecting essential daily consumption.
- **Cheese Varieties:** Multiple cheese products appear in the top picks, indicating a strong customer preference for cheese products.

---

## Item Affinity Trends

This section explores items that are frequently picked together, revealing insights into customer buying patterns.

### Top 5 Item Pairs Picked Together

| Rank | Item A ID | Item A Name                   | Item B ID | Item B Name                 | Pair Count |
|------|-----------|-------------------------------|-----------|-----------------------------|------------|
| 1    | 1001      | Agropur Cheddar Cheese 500g   | 1005      | Agropur Mozzarella Cheese   | 600        |
| 2    | 1002      | Agropur Greek Yogurt 1kg      | 1006      | Agropur Sour Cream 500ml    | 550        |
| 3    | 1004      | Agropur Skim Milk 1L          | 1003      | Agropur Butter 250g         | 500        |
| 4    | 1007      | Agropur Ice Cream Vanilla     | 1001      | Agropur Cheddar Cheese 500g | 450        |
| 5    | 1008      | Agropur Whole Milk 1L         | 1010      | Agropur Cream Cheese 250g   | 400        |

### Analysis

- **Cheese Combination Purchases:** Customers frequently purchase Cheddar and Mozzarella cheeses together, suggesting complementary uses in meals.
- **Dairy Product Pairings:** The pairing of Greek Yogurt and Sour Cream indicates a preference for fresh dairy products, possibly for cooking or as accompaniments.
- **Milk and Butter:** Skim Milk and Butter are commonly picked together, reflecting fundamental grocery items.

---

## Conclusions

Based on the data:

1. **Popular Products:**
   - **Cheddar Cheese 500g** is the most popular item.
   - Dairy staples like yogurt, butter, and milk have high pick frequencies.

2. **Customer Buying Patterns:**
   - Customers tend to purchase multiple cheese products together.
   - There is a notable affinity between dairy essentials in customer orders.

3. **Operational Insights:**
   - High-frequency items should be readily accessible in the warehouse to improve pick efficiency.
   - Understanding item affinities can aid in optimizing warehouse layout.

---

## Recommendations

1. **Inventory Management:**
   - Ensure adequate stock levels for high-demand items, especially Cheddar Cheese 500g and Greek Yogurt 1kg.
   - Monitor stock turnover rates to prevent stockouts and overstock situations.

2. **Warehouse Optimization:**
   - Place frequently paired items in close proximity to reduce pick times and increase efficiency.
   - Consider creating dedicated zones for high-demand items.

3. **Marketing Strategies:**
   - Develop promotional bundles for popular item pairs (e.g., Cheese Variety Pack).
   - Use targeted marketing campaigns highlighting top-selling products.

4. **Product Development:**
   - Explore opportunities to introduce new products in popular categories (e.g., flavored yogurts, specialty cheeses).
   - Gather customer feedback on high-frequency items for continuous improvement.

5. **Data-Driven Decisions:**
   - Establish regular reporting on pick frequencies and item affinities.
   - Utilize data analytics to predict future trends and adjust strategies accordingly.

---

## Appendix

### SQL Queries Used

#### Pick Frequency Per Item

```sql
SELECT
    pkli.materialMaster_id,
    mm.name AS item_name,
    COUNT(*) AS pick_count
FROM
    scPKLI pkli
    INNER JOIN scMaterialMaster mm ON pkli.materialMaster_id = mm.oid
WHERE
    pkli.pickedDate BETWEEN '2024-10-01' AND '2024-10-31'
GROUP BY
    pkli.materialMaster_id, mm.name
ORDER BY
    pick_count DESC;
```

#### Item Affinity Trends

```sql
SELECT
    a.materialMaster_id AS item_a_id,
    mm_a.name AS item_a_name,
    b.materialMaster_id AS item_b_id,
    mm_b.name AS item_b_name,
    COUNT(*) AS pair_count
FROM
    scPKLI a
    INNER JOIN scPKLI b ON a.pklh_id = b.pklh_id AND a.materialMaster_id < b.materialMaster_id
    INNER JOIN scMaterialMaster mm_a ON a.materialMaster_id = mm_a.oid
    INNER JOIN scMaterialMaster mm_b ON b.materialMaster_id = mm_b.oid
WHERE
    a.pickedDate BETWEEN '2024-10-01' AND '2024-10-31'
    AND b.pickedDate BETWEEN '2024-10-01' AND '2024-10-31'
GROUP BY
    a.materialMaster_id, mm_a.name,
    b.materialMaster_id, mm_b.name
ORDER BY
    pair_count DESC;
```

---

## Notes

- **Data Accuracy:** The analysis is based on the assumption that the data retrieved is accurate and complete.
- **Limitations:** This report does not account for external factors such as promotions, seasonal demand, or supply chain disruptions that might have influenced pick frequencies.
- **Further Analysis:** Additional insights can be gained by analyzing trends over multiple months or comparing with previous years.

---

*For further information or discussion regarding this report, please feel free to reach out.*