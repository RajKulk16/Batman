# Dynamic Customer Segmentation: An RFM Modeling Approach with K-Means Clustering

The primary objective of this project is to implement customer segmentation, leveraging RFM modeling and K-Means clustering. The ultimate goal is to enhance targeted marketing efforts and establish personalized customer relationship management strategies.

## Dataset Overview

1. **Description:**
   - The dataset encompasses all transactions from a UK-based and registered, non-store online retail entity, spanning the period from 01/12/2009 to 09/12/2011. The company specializes in unique all-occasion gift-ware, with a considerable portion of its clientele consisting of wholesalers.

   - The dataset has been meticulously curated to facilitate customer segmentation. The segmentation is achieved through RFM modeling, allowing businesses to categorize customers based on their transaction behavior. Further refinement is achieved using K-Means clustering, enabling more precise targeting and personalized marketing strategies.
  
   - The dataset contains over 1.05 million records with 8 features.

2. **Attributes:**
    - InvoiceNo: Nominal. A 6-digit integral number uniquely assigned to each transaction. If starting with 'c', indicates a cancellation.
    - StockCode: Nominal. A 5-digit integral number uniquely assigned to each distinct product.
    - Description: Nominal. Product name.
    - Quantity: Numeric. The quantities of each product per transaction.
    - InvoiceDate: Numeric. Date and time when a transaction was generated.
    - UnitPrice: Numeric. Product price per unit in sterling (£).
    - CustomerID: Nominal. A 5-digit integral number uniquely assigned to each customer.
    - Country: Nominal. The name of the country where a customer resides.

## Flow of the Project

1. **Data Analysis, Preprocessing, Engineering:**
    - Addressed duplicates, missing values, null values, etc., ensuring its impact on business analysis.
    - Conducted in-depth analysis, including understanding country-wise import/export patterns, customer distribution by continent, and comparisons between cancelled and non-cancelled orders.
    - Analyzed the top 10 products in each country/continent for strategic business insights.
    - Performed logical data cleaning and transformation.

2. **RFM Modeling:**
    - RFM stands for Recency, Frequency, and Monetary Value. It's a marketing model that segments customers based on their purchasing patterns.
         - Recency: How recently a customer has made a purchase
         - Frequency: How often a customer makes a purchase
         - Monetary value: How much money a customer spends on purchases
    - Calculated RFM values for each customer.
    - Assigned RFM segments to customers.
    - Assigned loyalty levels to customers based on RFM analysis for targeted marketing.

3. **K-Means Clustering:**
    - Applied the K-Means clustering algorithm to further refine customer segments.
    - Determined the optimal number of clusters based on the RFM data.

## Observations

1. Based on data analysis, gift-ware exports to continents like Asia, Africa, and the Middle East are relatively lower, potentially influenced by cultural differences and preferences.

2. Europe emerged as the leader in customer distribution by continent, with countries like the United Kingdom, Germany, France, and others prominently involved in gift-ware imports.

3. The best-selling product was identified as the "WHITE HANGING HEART T-LIGHT HOLDER."

4. The dataset revealed a higher number of Bronze-level customers (lower RFM scores), followed by Gold, Silver, and Platinum.

## Results

1. Customer segmentation based on behavioral patterns and subsequent categorization into loyalty levels have paved the way for more focused and personalized marketing efforts.

## Supporting Screenshots

![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/051a52b8-d3e2-426b-85d5-d896a0a55421)


![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/930e535f-e560-4a4d-a85b-ecdbc6b6b665)


![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/d97652ed-a991-4a88-b0ef-761c086d5f8b)


![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/c4329efb-4299-49ac-bd7b-31633b7b6fd8)


![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/b163cdd2-ab38-4c7e-9d75-8f7c51bfe129)


![image](https://github.com/RajKulk16/Customer-Clusters-Revealed/assets/74099005/cbc23055-eff4-48cd-8613-60a1fd24ee5f)

