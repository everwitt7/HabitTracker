import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                   z=data,
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                   y=[str(i) for i in range(52)],
                   hoverongaps = False))
fig.show()