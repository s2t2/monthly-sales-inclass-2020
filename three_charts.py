import plotly
import plotly.graph_objs as go

# INITIAL EXAMPLE

#labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
#values = [4500, 2500, 1053, 500]

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = [d["company"] for d in pie_data]
values = [d["market_share"] for d in pie_data]

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)
