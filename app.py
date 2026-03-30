import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

PRICE_INCREASE_DATE = "2021-01-15"

df = pd.read_csv("data/formatted_output.csv")

df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
df["sales"] = (
    df["sales"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

daily_sales = (
    df.groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Daily Pink Morsel Sales",
    labels={
        "date": "Date",
        "sales": "Total Sales ($)"
    }
)

fig.add_vline(
    x=PRICE_INCREASE_DATE,
    line_width=2,
    line_dash="dash",
    line_color="red"
)

fig.add_annotation(
    x=PRICE_INCREASE_DATE,
    y=daily_sales["sales"].max(),
    text="Price increase: 15 Jan 2021",
    showarrow=True,
    arrowhead=2,
    ax=80,
    ay=-40
)

fig.update_layout(
    template="plotly_white",
    hovermode="x unified",
    title_x=0.5
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Soul Foods Sales Visualiser"),
        dcc.Graph(figure=fig)
    ],
    style={"padding": "20px"}
)

if __name__ == "__main__":
    app.run(debug=True)
