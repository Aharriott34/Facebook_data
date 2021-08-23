# Facebook_data

Description:

A performance project was created for WebstaurantStore to see advertisement performance on all the Facebook platforms. The performance of the advertisements was sample data from January to April of 2020, and the instruction provided from WebstaurantStore was open for interpretation. This project analyzes, visualizes, and forecasts the performance of those ads to create a PowerPoint report.

Built With:
- Google Cloud BigQuery
- Microsoft Excel
- Python 3 

Prerequisites:
- Python packages used for analyzation:
  - Numpy
  - Pandas
  - Scipy.stats

- Python packages for visualization:
  - Matplotlib
  - Seaborn
- Python package for forecasting:
  - Random
  - Numpy
- Python package for hypothesis testing:
  - f_oneway in scipy.stats

Usage:

Google Cloud BigQuery was used to aggeregate the sample data provided from WebstaurantStore to figure out the performance of certain Facebook ads. There was roughly 64,000 ads saved in the table. There were some tables aggregated to find the cost and revenue of the ads over the 3 and a half month span. There were some tables aggregated to show the types of links shown and the campaing objectives of those links.

Microsoft Excel was used to create pivot tables of the ads and to see which types of ads are being displayed and clicked on the most. It was also used to visualize certain Key Performance Indicators such as Leads per advertisement.

Python 3 was used to store the data from BigQuery, and to analyze even further. It was used to find other Key Performance Indicators such as cost per click, as well as to forecast performance for the remainder of the year. Python 3 was finally used to visualize the analyzed data, and for hypothesis testing.

Visualizations:
- Forecast Models
![Forecasting Model Peak](https://user-images.githubusercontent.com/78121835/130523218-78b82293-55f0-464f-a462-f70df3283b76.png)
![Conversions Peak Forecast](https://user-images.githubusercontent.com/78121835/130523265-49eb9f31-32d5-44f4-b31d-b7722b510684.png)
![Forecasting Model Actual Click Through Rate](https://user-images.githubusercontent.com/78121835/130523483-06773b35-3190-4be9-b05e-b18bcf3a8714.png)
![Conversion Projected](https://user-images.githubusercontent.com/78121835/130523661-0b4e8a7c-c472-4598-a2ee-1793105fd066.png)


- Facebook Advertisements
![Location Breakdown](https://user-images.githubusercontent.com/78121835/130523438-0f1c35ce-89d6-4378-a128-df8ed39f8d17.png)
![Link Variation](https://user-images.githubusercontent.com/78121835/130523696-ee6ba7dc-e892-47e6-8c06-6e47b29a1b13.png)












