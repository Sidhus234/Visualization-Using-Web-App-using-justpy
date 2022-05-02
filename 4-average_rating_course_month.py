
import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
df = pd.read_csv(".//Data//reviews.csv", parse_dates=["Timestamp"])

df['Month'] = df['Timestamp'].dt.strftime('%Y-%m')
df_month_course = pd.DataFrame(df.groupby(["Month", "Course Name"])[
                               "Rating"].mean()).unstack()
df_month_course = df_month_course.round(decimals=1)

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Ratings per Course by Month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
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
    # Overwrite categoires in xaxis
    hc.options.xAxis.categories = list(df_month_course.index)
    # Overwrite series (y variable)
    hc_data = [{"name": v1, "data": [v2 for v2 in df_month_course[v1]]}
               for v1 in df_month_course.columns]

    hc.options.series = hc_data

    return wp


jp.justpy(app)
