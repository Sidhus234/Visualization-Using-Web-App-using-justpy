import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv(".//Data//reviews.csv", parse_dates=['Timestamp'])
# Average ratings by weekday
df['Weekday'] = df['Timestamp'].dt.strftime('%A')
df['Daynumber'] = df['Timestamp'].dt.strftime('%w').astype(int)
weekday_average = pd.DataFrame(df.groupby(['Weekday']).mean())
weekday_average = weekday_average.sort_values(by='Daynumber')
weekday_average['Rating'] = weekday_average['Rating'].round(decimals=2)


# highchart docs: https://www.highcharts.com/docs/index
# This code is copied from https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/spline-inverted
# Select any chart that you need and copy paste the code
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Day of the Week'
    },
    subtitle: {
        text: 'Udemy Courses'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 2018 to 2021.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5 stars.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Ratings',
        data: [[3,4], [5,6], [7,8]]
    }]
}
"""


def app():
    # Initiate a webpage
    wp = jp.QuasarPage()
    # Formmating : https://quasar.dev/style/shadows (refer this link)
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(weekday_average.index)
    hc.options.series[0].data = list(weekday_average['Rating'])
    return wp


jp.justpy(app)
