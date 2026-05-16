import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed CSV
df = pd.read_csv('data/pink_morsels_sales.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                'textAlign': 'center',
                'color': '#ff69b4',
                'font-family': 'Arial, sans-serif',
                'margin-bottom': '20px'
            }
        ),

        html.Div(
            children=[
                html.Label("Select Region:", style={'fontWeight': 'bold', 'margin-right': '10px'}),
                dcc.RadioItems(
                    id='region-radio',
                    options=[
                        {'label': 'All', 'value': 'all'},
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'}
                    ],
                    value='all',
                    inline=True,
                    inputStyle={'margin-right': '5px', 'margin-left': '10px'}
                )
            ],
            style={'textAlign': 'center', 'margin-bottom': '30px'}
        ),

        dcc.Graph(id='sales-line-chart'),

        html.P(
            "Observe the chart to see how sales changed before and after the price increase on 15th January 2021.",
            style={'textAlign': 'center', 'margin-top': '20px', 'font-style': 'italic'}
        )
    ],
    style={'max-width': '900px', 'margin': 'auto', 'padding': '20px', 'backgroundColor': '#fff0f5',
           'border-radius': '10px', 'box-shadow': '2px 2px 12px rgba(0,0,0,0.2)'}
)


# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    # Clean region names: strip whitespace, lowercase
    df_clean = df.copy()
    df_clean['region'] = df_clean['region'].str.strip().str.lower()

    if selected_region == 'all':
        filtered = df_clean
    else:
        filtered = df_clean[df_clean['region'] == selected_region.lower()]

    # Aggregate daily sales
    daily_sales = filtered.groupby('date')['sales'].sum().reset_index()

    # Handle empty filtered data
    if daily_sales.empty:
        fig = px.line(
            title=f"No data available for {selected_region.capitalize()} region"
        )
        return fig

    # Line chart
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales Over Time ({selected_region.capitalize()})',
        labels={'date': 'Date', 'sales': 'Total Sales'},
        template='plotly_white'
    )

    # Highlight price increase
    fig.add_vline(
        x=pd.to_datetime('2021-01-15'),
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top left"
    )

    fig.update_layout(title_x=0.5)
    return fig


# Run app
if __name__ == '__main__':
    app.run(debug=True)