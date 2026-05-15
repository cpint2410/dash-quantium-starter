import dash
from dash import html, dcc
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample DataFrame (you can replace with your messy dataset later)
df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Value": [10, 20, 30]
})

# Layout of the app
app.layout = html.Div([
    html.H1("Quantium Dash Starter"),
    html.P("This is your starter Dash environment."),

    html.H2("Sample Data Table"),
    dcc.Graph(
        figure={
            "data": [
                {"x": df["Category"], "y": df["Value"], "type": "bar", "name": "Values"},
            ],
            "layout": {
                "title": "Sample Bar Chart"
            }
        }
    )
])

# Run the server
if __name__ == "__main__":
    app.run(debug=True)