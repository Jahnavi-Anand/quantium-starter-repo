import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

PRICE_INCREASE_DATE = pd.Timestamp("2021-01-15")
REGION_OPTIONS = ["all", "north", "east", "south", "west"]


def load_data(path: str = "formatted_output.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["sales"] = pd.to_numeric(
        df["sales"].astype(str).str.replace("$", "", regex=False),
        errors="coerce",
    )
    df["region"] = df["region"].astype(str).str.strip().str.lower()
    df = df.dropna(subset=["date", "sales", "region"])
    return df


def build_figure(data: pd.DataFrame, selected_region: str):
    filtered = data.copy()
    if selected_region != "all":
        filtered = filtered[filtered["region"] == selected_region]

    daily_sales = (
        filtered.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    region_label = selected_region.title() if selected_region != "all" else "All Regions"

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        markers=True,
        labels={"date": "Date", "sales": "Total Sales ($)"},
        title=f"Daily Pink Morsel Sales — {region_label}",
    )

    fig.update_traces(
        line=dict(color="#01696f", width=4),
        marker=dict(size=7, color="#da7101", line=dict(color="#f7f6f2", width=1.5)),
        hovertemplate="Date=%{x|%d %b %Y}<br>Sales=$%{y:,.2f}<extra></extra>",
    )

    fig.add_vline(
        x=PRICE_INCREASE_DATE,
        line_width=2,
        line_dash="dash",
        line_color="#a13544",
    )

    peak_y = daily_sales["sales"].max() if not daily_sales.empty else 0
    fig.add_annotation(
        x=PRICE_INCREASE_DATE,
        y=peak_y,
        text="Price increase • 15 Jan 2021",
        showarrow=True,
        arrowhead=2,
        ax=90,
        ay=-50,
        font=dict(size=12, color="#28251d"),
        bgcolor="rgba(249,248,245,0.92)",
        bordercolor="#d4d1ca",
        borderwidth=1,
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#fbfbf9",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=80, b=20),
        title_x=0.03,
        title_font=dict(size=22, color="#28251d"),
        font=dict(family="Arial, sans-serif", color="#28251d"),
        xaxis=dict(
            showgrid=False,
            linecolor="#d4d1ca",
            tickfont=dict(size=12),
        ),
        yaxis=dict(
            gridcolor="#e6e4df",
            zeroline=False,
            tickprefix="$",
            tickfont=dict(size=12),
        ),
    )
    return fig


df = load_data()
app = Dash(__name__)
app.title = "Soul Foods Sales Visualiser"

app.layout = html.Div(
    className="app-shell",
    children=[
        html.Div(className="bg-orb bg-orb-one"),
        html.Div(className="bg-orb bg-orb-two"),
        html.Main(
            className="page",
            children=[
                html.Section(
                    className="hero-card",
                    children=[
                        html.Div(
                            className="eyebrow",
                            children="Soul Foods • Pink Morsel sales explorer",
                        ),
                        html.H1("Sales before and after the January 2021 price change"),
                        html.P(
                            "Use the region filter to compare how Pink Morsel sales changed over time and spot whether performance was stronger before or after the 15 January 2021 price increase."
                        ),
                    ],
                ),
                html.Section(
                    className="controls-card",
                    children=[
                        html.Div(
                            className="controls-header",
                            children=[
                                html.H2("Filter by region"),
                                html.Span("Five quick views", className="chip"),
                            ],
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": label.title(), "value": label}
                                for label in REGION_OPTIONS
                            ],
                            value="all",
                            inline=True,
                            className="region-radio-group",
                            inputClassName="region-radio-input",
                            labelClassName="region-radio-label",
                        ),
                    ],
                ),
                html.Section(
                    className="chart-card",
                    children=[
                        dcc.Graph(
                            id="sales-line-chart",
                            figure=build_figure(df, "all"),
                            config={"displayModeBar": False},
                        )
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(Output("sales-line-chart", "figure"), Input("region-filter", "value"))
def update_chart(selected_region: str):
    return build_figure(df, selected_region)


if __name__ == "__main__":
    app.run(debug=True)