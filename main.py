import csv

with open("campaign_data.csv", "r") as file:
    reader = csv.DictReader(file)
    campaigns = list(reader)

with open("campaign_report.csv", "w", newline="") as file:
    fieldnames = [
        "Campaign",
        "CTR",
        "Conversion Rate",
        "Cost Per Conversion"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for campaign in campaigns:
        spend = float(campaign["Spend"])
        impressions = int(campaign["Impressions"])
        clicks = int(campaign["Clicks"])
        conversions = int(campaign["Conversions"])

        ctr = clicks / impressions * 100
        conversion_rate = conversions / clicks * 100

        if conversions > 0:
            cost_per_conversion = spend / conversions
        else:
            cost_per_conversion = 0

        writer.writerow({
            "Campaign": campaign["Campaign"],
            "CTR": round(ctr, 2),
            "Conversion Rate": round(conversion_rate, 2),
            "Cost Per Conversion": round(cost_per_conversion, 2)
        })

print("Campaign report saved successfully!")