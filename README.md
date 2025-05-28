# 🛍️ Web Scraping & Analysis

This project involves **scraping**, **cleaning**, and **analyzing** cosmetic product data from the website. It focuses on extracting key product information and performing basic data analysis and visualization to gain insights into product pricing, ratings, and customer reviews.

## 📌 Project Objective

To collect and analyze cosmetic product data from Sociolla’s website to identify trends, patterns, and insights using Python-based tools.

---

## 📦 Collected Data Fields

- **Brand** – the brand name  
- **Name** – the name of the makeup product  
- **Price** – the listed price  
- **Rating** – customer rating score (out of 5)  
- **Review** – number of customer reviews  

---

## 🧰 Tools & Libraries

### Web Scraping:
- `selenium` – to automate the browser and handle JavaScript-rendered pages  
- `BeautifulSoup` – for HTML parsing and data extraction  
- `pandas` – for tabular data structuring and storage  
- `time` – to manage scraping intervals and prevent server blocking

### Data Analysis & Visualization:
- `pandasql` – to run SQL-like queries on DataFrames  
- `seaborn` – for statistical data visualization  
- `matplotlib.pyplot` – for building various plots and charts

---

## 📁 Project Structure

📦 **sociolla-web-scraping-analysis**
- `chromedriver.exe`                    # ChromeDriver for Selenium
- `sociolla_makeup_data.csv`            # Raw scraped data
- `sociolla_data_cleaning.ipynb`        # Data cleaning notebook
- `sociolla_clean.csv`                  # Cleaned dataset
- `analisis_visualization.ipynb`        # Data analysis & visualization
- `Web Scraping and Analysis of Cosmetic Products from Sociolla.pdf` # PDF report for the analysis
- `README.md`                          # Project documentation

## 📊 Key Insights

The main objective of this project is to identify which cosmetic brands are most suitable to prioritize in promotional or marketing campaigns. Based on data analysis of product variety, customer engagement, and product quality, the following insights were obtained:

| **Category**                          | **Top Brands**                                      | **Insight**                                              |
|--------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
| Most Product Variety                 | Make Over, Focallure, BLP Beauty                    | Active in launching products, wide market coverage       |
| Highest Total Reviews                | Wardah, Emina, Maybelline                           | High brand awareness and customer engagement             |
| Highest Review-to-Product Ratio      | Emina, Maybelline, Wardah                           | Each product gets significant customer feedback          |
| High Avg. Rating + High Engagement   | Wardah, Emina, Maybelline, Make Over, Mother of Pearl | Quality and popularity combined                          |
| Most Products Rated Above 4.7        | Elise, Jacqueline Beaute, Lavie Lash                 | Consistently excellent product performance               |

> Detailed charts and visualizations are available in the `analisis_visualization.ipynb` notebook.
> For a more complete summary of the analysis, you can also refer to the PDF report `Web Scraping and Analysis of Cosmetic Products from Sociolla.pdf` in this repository.

---

⚠️ **Disclaimer**  
- This project was created only for **learning and practice purposes**.  
- The data collected from Sociolla is used just to **learning web scraping and data analysis techniques**.  
- I do not intend to use the data for anything commercial or harmful.  
- If there are any issues or concerns, feel free to contact me and I’ll be happy to take action.


## 🙌 Final Words
Thanks for scrolling this far! Got ideas, thoughts, or feedback? I’m all ears 👂✨



