import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import random
from scipy.stats import f_oneway

pd.set_option("display.max_columns", 100)
sns.set_palette("Set2")
sns.set_style("darkgrid")

def show_values_on_bars(axs, h_v="v", space=0.4):
    def _show_on_single_plot(ax):
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)

# April is from 4/1/20 - 4/16/20
month_label = ["January", "February", "March", "April"]
cost_per_month = [54375.41029999991, 50731.389899999915, 27821.30009999995, 5235.9601]
costs = sum(cost_per_month)
cost_avg_3_months = sum([54375.41029999991, 50731.389899999915, 27821.30009999995]) / 3
revenue_per_month = [9347110.84, 7684929.0, 3989494.69, 1528162.59]
revenue_per_month_avg = [301519.704516129, 274461.75, 173456.29086956521, 95510.16187500002]
total_revenue_avg_3 = sum([9347110.84, 7684929.0, 3989494.69]) / 3
revenue = sum(revenue_per_month)
personal_purchase_per_month = [22218, 19375, 10157, 4405]
personal_purchase_per_month_avg = [716.7096774193549, 691.9642857142856, 441.60869565217394, 275.3125]
personal_purchased = sum(personal_purchase_per_month)
print(f"{personal_purchased} amount of people have purchased items from WebstarauntStore from an ad.The amount of revenue made from January to April is ${round(revenue, 2)}.")

ax1 = plt.subplot(121)
plt.suptitle('Facebook Ads: Cost vs. Revenue')
ax1.plot(month_label, cost_per_month, marker='o')
ax1.set_title('Cost')
ax1.set_xticks(range(len(month_label)))
ax1.set_xlabel("Months")
ax1.set_ylabel("USD (Tens of Thousands)")
ax1.set_xticklabels(month_label)

ax2 = plt.subplot(122)
ax2.plot(month_label, revenue_per_month, marker='o')
ax2.set_title('Revenue')
ax2.set_xticks(range(len(month_label)))
ax2.set_xlabel("Months")
ax2.set_ylabel("USD (Millions)")
ax2.set_xticklabels(month_label)
# plt.tight_layout()
# plt.show()

campaign_objectives = ["Conversions", "Product Catalog Sales", "Lead Generation", "Reach", "Post Engagement", "Link Clicks"]
campaign_clicks_sum = [23377, 525761, 22048, 1679, 4793, 3249]
campaign_outbound_clicks_sum = [9831, 472590, 3073, 730, 770, 2558]
campaign_links_click_sum = [9444, 473933, 8545, 730, 770, 2558]
campaign_conversion_sum = [116008, 2265440, 25401, 16242, 13659, 6778]
campaign_reach_sum = [1010051, 10887169, 665946, 1728317, 230735, 390310]
campaign_impression_sum = [1182913, 14420154, 684334, 1742168, 240415, 784218]
campaign_cost_sum = [8070.270000000185, 116857.50069999375, 7692.589800000252, 1899.8099999999883, 3460.8098999999993, 1977.7399999999973]
campaign_revenue_sum = [1089243.6700000002, 21098616.130000155, 154279.30000000005, 173243.21000000014, 161952.35999999993, 38376.63999999998]
campaign_lead_sum = [871, 5029, 135, 44, 17, 52]
campaign_post_engagement = [34044, 495168, 10628, 11245, 6597, 2733]
campaign_personal_purchase = [2865, 52212, 379, 557, 461, 127]
campaign_objectives_results = [7490, 44266, 6876, 4427, 307, 644]
campaign_df = pd.DataFrame(data=(campaign_objectives_results, campaign_clicks_sum, campaign_outbound_clicks_sum, campaign_links_click_sum, campaign_conversion_sum, campaign_impression_sum, campaign_reach_sum, campaign_personal_purchase, campaign_cost_sum, campaign_revenue_sum), columns=campaign_objectives)

fig, ((ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=2, ncols=2)
fig.suptitle("Campaign Objectives")
ax3.set_title("Post Engagement via Advertisement")
ax3.barh(campaign_objectives, campaign_objectives_results)
ax3.set_xlabel("Engagement")

ax4.set_title("Purchases via Advertisement")
ax4.barh(campaign_objectives, campaign_personal_purchase)
ax4.set_xlabel("Amount of Personal Purchases")

ax5.set_title("Costs via Advertisement")
ax5.barh(campaign_objectives, campaign_cost_sum)
ax5.set_xlabel("Costs USD ")

ax6.set_title("Revenue via Advertisement")
ax6.barh(campaign_objectives, campaign_revenue_sum)
ax6.set_xlabel("Revenue USD (Tens of Millions)")
# plt.tight_layout()
# plt.show()

fig, ((ax7, ax8), (ax9, ax10)) = plt.subplots(nrows=2, ncols=2)
fig.suptitle("Campaign Objectives")
ax7.set_title("Conversion via Advertisement")
ax7.barh(campaign_objectives, campaign_conversion_sum)
ax7.set_xlabel("Conversion (Millions)")

ax8.set_title("Reach via Advertisement")
ax8.barh(campaign_objectives, campaign_reach_sum)
ax8.set_xlabel("Reach (Tens of Millions)")

ax9.set_title(" Link Clicks via Advertisement")
ax9.barh(campaign_objectives, campaign_links_click_sum)
ax9.set_xlabel("Link Clicks")
# ax9.set_xticklabels(['0','100K', '200K', '300K', '400K', '500K'])

ax10.set_title("Leads via Advertisement")
ax10.barh(campaign_objectives, campaign_lead_sum)
ax10.set_xlabel("Leads Clicks")
# plt.tight_layout()
# plt.show()

link_type = ["Link", "Video", "Photo"]
link_total = [60745, 2212, 307]
click_links = [573273, 185, 4793, 2656]
outbound_clicks_links = [488270, 115, 770, 397]
conversion_links = [2389083, 10644, 13659, 30142]
link_cost_sum = [135342.6204999934, 309.8599999999998, 3460.8098999999993, 845.429999999997]
link_revenue_sum = [21969737.790000178, 125501.62000000001, 458519.54, 161952.35999999993]
link_personal_purchase_sum = [54373, 380, 1387, 461]

plt.clf()
ax11 = sns.barplot(x=link_type, y=link_total)
ax11.set_title('Link Variation')
ax11.set_ylabel('Total')
show_values_on_bars(ax11)
# plt.tight_layout()
# plt.show()

# ["CONVERSIONS", "PRODUCT_CATALOG_SALES", "LEAD_GENERATION", "REACH", "POST_ENGAGEMENT", "LINK_CLICKS"]
social_media = ["Facebook", "Instagram", "Audience Network", "Messenger"]
social_media_total = [43246, 14687, 5277, 795]
facebook_objectives = [4948, 30799, 4278, 2670, 205, 346]
instagram_objectives = [2480, 8036, 2598, 1292, 102, 179]
audience_network_objectives = [59, 4635, 0, 465, 0, 118]
messenger_objectives = [3, 792, 0, 0, 0, 0]
social_media_costs = [130267.45949999607, 9065.031000000234, 390.11990000000054, 5.749999999999962]
social_media_revenue = [20768312.130000155, 1798793.4099999957, 85192.37999999998, 10653.67]
social_media_personal_purchase = [51820, 4373, 204, 12, 192]
social_media_conversions = [2280494, 152050, 6106,432]
social_media_impressions = [17489312, 1308502, 188906, 1824]

plt.clf()
ax12 = sns.barplot(x=social_media, y=social_media_total)
ax12.set_title("Social Media: Advertisement Locations")
ax12.set_xlabel("Social Media")
ax12.set_ylabel("Amount")
show_values_on_bars(ax12)
# plt.tight_layout()
# plt.show()

# Ad location totals, costs for ad locations and revenue from ad location.
ad_location = ['Feed', 'Search', 'Instagram Stories', 'Marketplace', 'Messenger Stories', 'Audience Network Classic', 'Instant Article', 'Right Hand Column', 'Facebook Stories', 'In Stream Video',' Instagram Explore', 'Messenger Inbox', 'Video Feeds']
ad_location_data = [40714, 2241, 2019, 5649, 3, 5251, 3962, 2834, 113, 157, 266, 792, 41]
ad_location_personal_purchase = [49479, 113, 834, 405, 0, 204, 148, 5099, 67, 10, 38, 12, 0]
ad_location_impressions = [14882693, 113473, 582446, 158854, 3, 188876, 24647, 2985709, 15935, 27813, 6269, 1821, 5]
ad_location_reach = [12591120, 103611, 566587, 140696, 3, 86555, 21154, 1306050, 15295, 25805, 5764, 1575, 3]
ad_location_conversion = [2210559, 7486, 37243, 21782, 1, 6106, 4825, 145886, 3581, 287, 892, 431, 3]

plt.clf()
ax10 = sns.barplot(x=ad_location_data, y=ad_location)
ax10.set_title("Advertisement Location Breakdown")
ax10.set_xlabel("Total")
ax10.set_ylabel("Location")
show_values_on_bars(ax7, 'h', 0.1)
# plt.tight_layout()
# plt.show()

# Which social media platform are the ads coming from.
#Labels for public platform
facebook_ad_labels = ['Feed', 'Marketplace', 'Instant Article', 'Right Hand Column', 'Search', 'In Stream Video', 'Facebook Stories', 'Video Feeds']
facebook_ad_location_data = [28312, 5649, 3962, 2834, 2241, 131, 113, 4]
instagram_ad_labels = ['Feed', 'Instagram Stories', 'Instagram Explore']
instagram_ad_location_data = [12402, 2019, 266]
audience_network_ad_labels = ['Audience Network Classic', 'In Stream Video']
audience_network_location_data = [5251, 26]
messenger_ad_labels = ['Messenger Inbox', 'Messenger Stories']
messenger_location_data = [792, 3]

plt.clf()
ax11 = sns.barplot(x=facebook_ad_labels, y=facebook_ad_location_data)
ax11.set_title("Facebook")
ax11.set_xlabel("Ad Location")
ax11.set_ylabel("Total")
show_values_on_bars(ax11)
# plt.tight_layout()
# plt.show()

ax12 = sns.barplot(x=instagram_ad_labels, y=instagram_ad_location_data)
ax12.set_title("Instagram")
ax12.set_xlabel("Ad Location")
ax12.set_ylabel("Total")
show_values_on_bars(ax12)
# plt.tight_layout()
# plt.show()

ax13 = sns.barplot(x=audience_network_ad_labels, y=audience_network_location_data)
ax13.set_title("Audience Network")
ax13.set_xlabel("Ad Location")
ax13.set_ylabel("Total")
show_values_on_bars(ax13)
# plt.show()

ax14 = sns.barplot(x=messenger_ad_labels, y=messenger_location_data)
ax14.set_title("Messenger")
ax14.set_xlabel("Ad Location")
ax14.set_ylabel("Total")
show_values_on_bars(ax14)
# plt.show()

# Reach is the number of people who saw the ad at least once. Impression is how many times the ad was on screen.
reach_total = [13515287, 1260768, 86585, 1578]
impression_total = [17489312, 1308502, 188906, 1824]
offsite_conversion_total = [2280494, 152050, 6106, 432]

reach_per_month_sum = [5717365, 5022888, 2987610, 1029695]
reach_per_month_avg = [184431.12903225806, 179388.8571428571, 129896.08695652173, 64355.9375]
reach_df = pd.DataFrame(data=(reach_per_month_sum, reach_per_month_avg), columns=month_label)

impression_per_month_sum = [7329798, 6297334, 3738367, 1501694]
impression_per_month_avg = [236445.09677419352, 224904.78571428568, 162537.6956521739, 93855.875]
impression_per_month_avg_minus_april = [236445.09677419352, 224904.78571428568, 162537.6956521739]
impressions_minus_april_sum = [7329798, 6297334, 3738367]
forecast_binomial_model_impression = sum(impressions_minus_april_sum) / len(impressions_minus_april_sum)
impression_df = pd.DataFrame(data=(impression_per_month_sum, impression_per_month_avg), columns=month_label)
impression_monthly_average = sum(impression_per_month_avg_minus_april) / len(impression_per_month_avg_minus_april)


offsite_conversion_per_month_sum = [1001769, 850017, 417929, 149567]
offsite_conversion_per_month_avg = [32315.12903225806, 30357.750000000007, 18170.826086956524, 9347.9375]
offsite_conversion_per_month_minus_april_avg = [32315.12903225806, 30357.750000000007, 18170.826086956524]
offsite_conversion_minus_april_sum = [1001769, 850017, 417929]
forecast_binomial_model_conversion = sum(offsite_conversion_minus_april_sum) / len(offsite_conversion_minus_april_sum)
conversion_monthly_average = sum(offsite_conversion_per_month_minus_april_avg) / len(offsite_conversion_per_month_minus_april_avg)
offsite_df = pd.DataFrame(data=(offsite_conversion_per_month_sum, offsite_conversion_per_month_avg), columns=month_label)
offsite_monthly_range = offsite_conversion_per_month_minus_april_avg[0] - offsite_conversion_per_month_minus_april_avg[-1]

plt.clf()
forecasting_months = np.random.binomial(n=int(forecast_binomial_model_conversion), p=0.043, size=int(forecast_binomial_model_impression))
plt.hist(forecasting_months, bins=30, density=True)
plt.title('Forecasting Model: Peak Click Through Rate')
plt.xlabel("Conversions")
plt.ylabel("Density")
# plt.show()

plt.clf()
forecasting_months = np.random.binomial(n=int(forecast_binomial_model_conversion), p=0.027, size=int(forecast_binomial_model_impression))
plt.hist(forecasting_months, bins=30, density=True)
plt.title('Forecasting Model: Actual Click Through Rate')
plt.xlabel("Conversions")
plt.ylabel("Density")
# plt.show()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
forecasted_sample = random.randint(36750, 38750)
offsite_conversion_per_month_actual = [32315, 30357, 18170, 9347, 0, 0, 0, 0, 0, 0, 0, 0]
offsite_forecast_per_month = [random.randint(31750, 33500) for i in range(12)]
offsite_forecast_per_month_2 = [random.randint(12800, 41000) for i in range(12)]

# Projected
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = range(len(months)) # Number of sets of bars
w = 0.5 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(len(d))]

# Actual
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = range(len(months)) # Number of sets of bars
w = 0.5 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(len(d))]

plt.clf()
middle_x = [(a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Projected Conversion", "Actual Conversion"]

plt.bar(bars1_x, offsite_forecast_per_month)
plt.bar(bars2_x, offsite_conversion_per_month_actual)
plt.xticks(middle_x, months)
plt.xlabel("Months")
plt.ylabel("Offsite Conversions")
plt.legend(labels)
plt.title("Conversions: Peak Forecast")
# plt.tight_layout()
# plt.show()

plt.clf()
middle_x = [(a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Projected Conversion", "Actual Conversion"]

plt.bar(bars1_x, offsite_forecast_per_month_2)
plt.bar(bars2_x, offsite_conversion_per_month_actual)
plt.xticks(middle_x, months)
plt.xlabel("Months")
plt.ylabel("Offsite Conversions")
plt.legend(labels)
plt.title("Conversions: Actual Forecast")
# plt.tight_layout()
# plt.show()

# Clicks are when a person clicks on ad leading them on or off Facebook owned properties.
# Outbound clicks are clicks that lead a person off Facebook owned properties.
# Link clicks are the number of clicks on links to select destinations or experiences, on or off Facebook-owned properties.
outbound_clicks_total = [476263, 11741, 981, 28]
clicks_total = [564195, 14879, 981, 30]
link_clicks_total = [482036, 12389, 981, 28]
overall_clicks_df = pd.DataFrame(data=(clicks_total, outbound_clicks_total, link_clicks_total), columns=social_media)


outbound_clicks_per_month_sum = [204247, 177868, 93104, 8259]
outbound_clicks_per_month_avg = [6588.612903225807, 6352.428571428572, 4048.000000000001, 516.1875000000001]
outbound_clicks_minus_april = [204247, 177868, 93104]
outbound_clicks_monthly_avg = sum(outbound_clicks_minus_april) / 3
outbound_clicks_df = pd.DataFrame(data=(outbound_clicks_per_month_sum, outbound_clicks_per_month_avg), columns=month_label)


clicks_per_month_sum = [238914, 209996, 112466, 12426]
clicks_per_month_avg = [7706.903225806452, 7499.857142857143, 4889.826086956522, 776.625]
clicks_df = pd.DataFrame(data=(clicks_per_month_sum, clicks_per_month_avg), columns=month_label)


link_clicks_per_month_sum = [207048, 179893, 94407, 8515]
link_clicks_per_month_avg = [6678.967741935484, 6424.750000000001, 4104.652173913043, 532.1875]
link_clicks_df = pd.DataFrame(data=(link_clicks_per_month_sum, link_clicks_per_month_avg), columns=month_label)


# Performance analysis
cpi_per_month = (sum(offsite_conversion_minus_april_sum) / sum(impressions_minus_april_sum)) * 100
cpi_apps = (sum(offsite_conversion_total) / sum(impression_total)) * 100
ctr_per_app = (sum(outbound_clicks_total))/ sum(impression_total) * 100
ctr_per_month = (sum(outbound_clicks_per_month_sum) / sum(impressions_minus_april_sum)) * 100
cpc = costs / sum(clicks_total)
cpc_per_campaign = costs / sum(campaign_clicks_sum)
cpc_conversions = costs / sum(offsite_conversion_total)
roas = sum(offsite_conversion_total) / costs
cpm = costs / sum(impression_total) * 1000

# ANOVA Test
def sig_test(pval):
    if pval < 0.05:
        return(f"The p-value is {round(pval, 2)}. There is a significant difference.")
    else:
        return(f"The p-value is {round(pval, 2)}. There is not a significant difference.")

# Anova test for a difference between total of campaign ads, and purchases.
fstat, pval = f_oneway(campaign_conversion_sum, campaign_personal_purchase)
print(sig_test(pval))

# Anova test for a difference between Facebook sites conversion, and purchases.
fstat2, pval2 = f_oneway(social_media_conversions, social_media_personal_purchase)
print(sig_test(pval2))

print(f"The overall Conversion Per Impression (CPI) by social media is {round(cpi_apps, 2)}%.")
print(f"The monthly Conversion Per Impression (CPI) is {round(cpi_per_month, 2)}%.")
print(f"The overall Click Through Rate (CTR) by social media {round(ctr_per_app, 2)}%.")
print(f"The monthly Click Through Rate (CTR) is {round(ctr_per_month, 2)}%.")
print(f"The overall Cost Per Click (CPC) is ${round(cpc, 2)}.")
print(f"The overall Cost Per Action (CPA) is ${round(cpc_conversions, 2)}.")
print(f"The overall Return on Ad Spend (ROAS) is ${round(roas, 2)}.")
print(f"The overall Cost Per Mile (CPM), or Cost Per Thousand (CPT), is ${round(cpm, 2)}.")
print(f"The range of offsite conversion is {round(offsite_monthly_range)}.")
print(f"The average conversion per month is {round(conversion_monthly_average)}.")

# Get average of total clicks per month, the average of impressions per month, and the average of ads to calculate the remaining months for the year. np.random.binomial(N, p, size) n = offsite_conversion, p= cpi, size= impressions
#
# ALL SQL CODE
#
# FINDING TOTALS VIA ADS OBJECTIVE
# SELECT campaign_objective,
# SUM(clicks) AS total_clicks,
# SUM(outbound_clicks) AS total_outbound_clicks,
# SUM(action_link_click) AS total_link_clicks,
# SUM(offsite_conversions) AS total_conversions,
# SUM(reach) AS total_reach,
# SUM(impressions) AS total_impressions,
# SUM(cost) AS total_cost,
# SUM(offsite_conversion_value_fb_pixel_purchase) as total_revenue,
# SUM(offsite_conversions_fb_pixel_purchase) as total_items
# FROM `sampledataprojectv2.Facebook.Facebook_data`
# GROUP BY 1;
#
# FINDINGS OF COSTS PER MONTH
# WITH january_price AS(SELECT date, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-01-01' AND '2020-01-31'
# GROUP BY 1
# ORDER BY 1),
# february_price AS(SELECT date, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-02-01' AND '2020-02-28'
# GROUP BY 1
# ORDER BY 1),
# march_price AS(SELECT date, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-03-01' AND '2020-03-31'
# GROUP BY 1
# ORDER BY 1),
# april_price AS(SELECT date, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-04-01' AND '2020-04-16'
# GROUP BY 1
# ORDER BY 1)
# SELECT SUM(april_price.total) FROM april_price
# WHERE april_price IS NOT NULL;
#
#
# FINDING COSTS PER MONTH BY PLATFORMS
# WITH january_price AS(SELECT date, platform_position, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-01-01' AND '2020-01-31'
# GROUP BY 1, 2
# ORDER BY 1),
# february_price AS(SELECT date, platform_position, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-02-01' AND '2020-02-28'
# GROUP BY 1, 2
# ORDER BY 1),
# march_price AS(SELECT date, coalesce(platform_position, 'Unknown') as platform, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-03-01' AND '2020-03-31'
# GROUP BY 1, 2
# ORDER BY 1),
# april_price AS(SELECT date, SUM(cost) AS total FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-04-01' AND '2020-04-16'
# GROUP BY 1
# ORDER BY 1)
# SELECT  platform,SUM(march_price.total) FROM march_price
# GROUP BY 1;
#
#
# FINDING TOTAL AMOUNT OF ADS PER MONTH
# WITH january_price AS(SELECT date, ad_group_name, cost, ad_group_daily_budget FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-01-01' AND '2020-01-31'
# AND 5 IS NOT NULL
# ORDER BY 1),
# february_price AS(SELECT date, ad_group_name, COUNT(ad_group_name) AS total, cost, ad_group_daily_budget FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-02-01' AND '2020-02-28'
# AND 5 IS NOT NULL
# GROUP BY 1, 2, 4, 5
# ORDER BY 1),
# march_price AS(SELECT date, ad_group_name, COUNT(ad_group_name) AS total, cost, ad_group_daily_budget FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-03-01' AND '2020-03-31'
# AND 5 IS NOT NULL
# GROUP BY 1, 2, 4, 5
# ORDER BY 1),
# april_price AS(SELECT date, ad_group_name, COUNT(ad_group_name) AS total, cost, ad_group_daily_budget FROM `sampledataprojectv2.Facebook.Facebook_data`
# WHERE date BETWEEN '2020-04-01' AND '2020-04-16'
# AND 5 IS NOT NULL
# GROUP BY 1,2,4,5
# ORDER BY 1)
# SELECT ad_group_name, SUM(cost) FROM january_price
# WHERE ad_group_name = 'All Placements | FB & IG Engagers'
# GROUP BY 1;
#
