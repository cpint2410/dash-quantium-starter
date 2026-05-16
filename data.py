import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed CSV from last task
df = pd.read_csv('data/pink_morsels_sales.csv')

# Make sure 'date' is a datetime type
df['date'] = pd.to_datetime(df['date'])

# Optional: sort by date
df = df.sort_values('date')

# Aggregate total sales by date (sum over regions)
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create a line chart using Plotly Express
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Total Sales'}
)

# Initialize Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div(children=[
    html.H1('Pink Morsel Sales Visualiser', style={'textAlign': 'center'}),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    ),
    html.P(
        "Observe the chart to see how sales changed before and after the price increase on 15th January 2021.",
        style={'textAlign': 'center'}
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)