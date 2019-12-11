import plotly.graph_objects as go
animals=['Social Networking', 'News', 'Shopping']

fig = go.Figure(data=[
    go.Bar(name='Android App', x=animals, y=[2.6, 8.2, 3.7]),
    go.Bar(name='Mobile Browser', x=animals, y=[2.4, 11, 10.4]),
    go.Bar(name='Desktop Browser',x=animals,y=[4,12.4,9.4])
])

# Change the bar mode
fig.update_layout(barmode='group',
xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Websites divided into different domains",
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="black"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Average no of trackers",
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="black"
            )
        )
    )
)
fig.show()