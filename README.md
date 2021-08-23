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
- Campaign Objectives
![Campaign Objectives 4](https://user-images.githubusercontent.com/78121835/130523975-dc0b028d-e26b-436a-866d-fe6f0fa31102.png)
![Campaign Objectives 5](https://user-images.githubusercontent.com/78121835/130523987-baa4f744-0d35-4c8d-85e8-6a03d9daecac.png)


- Forecast Models
![Forecasting Model Peak](https://user-images.githubusercontent.com/78121835/130523218-78b82293-55f0-464f-a462-f70df3283b76.png)
![Conversions Peak Forecast](https://user-images.githubusercontent.com/78121835/130523265-49eb9f31-32d5-44f4-b31d-b7722b510684.png)
![Forecasting Model Actual Click Through Rate](https://user-images.githubusercontent.com/78121835/130523483-06773b35-3190-4be9-b05e-b18bcf3a8714.png)
![Conversion Forecast](https://user-images.githubusercontent.com/78121835/130523808-fd589ccd-3522-462d-887c-ed1a7dd66759.png)

- Facebook Advertisements
![Ad Locations](https://user-images.githubusercontent.com/78121835/130523848-162abffe-960f-4a2a-915a-3d5c32d4bce8.png)
![Location Breakdown](https://user-images.githubusercontent.com/78121835/130523438-0f1c35ce-89d6-4378-a128-df8ed39f8d17.png)
![Link Variation](https://user-images.githubusercontent.com/78121835/130523696-ee6ba7dc-e892-47e6-8c06-6e47b29a1b13.png)

- Cost vs. Revenue
![Facebook Cost vs Revenue](https://user-images.githubusercontent.com/78121835/130523928-6b869ad6-27a0-4ad1-a28f-92d9cc3ceb04.png)













