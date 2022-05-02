
import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
df = pd.read_csv(".//Data//reviews.csv", parse_dates=["Timestamp"])

df['Month'] = df['Timestamp'].dt.strftime('%Y-%m')
df_month_course = pd.DataFrame(df.groupby(["Month", "Course Name"])[
                               "Rating"].count()).unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Number of Ratings by Course by Month'
    },
    

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [ {
        name: "Latvia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 2, 4
        ]
    }, {
        name: "Estonia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 3, 3, 1, 0
        ]
    }, {
        name: "Uzbekistan",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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
