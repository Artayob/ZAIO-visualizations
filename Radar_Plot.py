import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

pio.renderers.default = "vscode"  # works in Interactive Window

index = ['People', 'Technology Use', 'Innovation', 'Nimble', 'Profitability', 'Compliance', 'Benefits']
Microsoft = [7, 8, 7, 9, 7, 9, 7]
Google = [8, 9, 7, 8, 8, 7, 9]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(r=Microsoft, theta=index, fill='toself', name='Microsoft'))
fig.add_trace(go.Scatterpolar(r=Google, theta=index, fill='toself', name='Google'))

fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True)
fig.show()