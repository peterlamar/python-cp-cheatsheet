"""
Summarize a column total cases column and total deaths column 
Country by country data in columns, sum up and match global totals
"""
import csv 
import pandas

pandas.set_option("display.max_rows", None, "display.max_columns", None)
col_list = ["Total Cases", "Country/ Other", "Total Deaths", "# 9/27/2020"]
df = pandas.read_csv("covidmilliondead.csv", usecols=col_list, thousands=',')

totalCases, totalDeaths = 0,0

for idx,  cases,deaths in zip(df["# 9/27/2020"], df["Total Cases"], df["Total Deaths"]):
    if idx > 0:
        totalCases += cases 
        if deaths > 0:
            totalDeaths += deaths

for idx, country, cases, deaths in zip(df["# 9/27/2020"], df["Country/ Other"], df["Total Cases"], df["Total Deaths"]):
    if idx > 0:
        print("\n",country)
        print("Cases : ", cases, "/", totalCases, " %", "{:.5%}".format(cases/totalCases))
        if deaths > 0:
            print("Deaths : ", int(deaths), "/", totalDeaths, " %", "{:.5%}".format(deaths/totalDeaths))

print("")
print("Total Cases")
print(totalCases)

print("Total Deaths")
print(totalDeaths)