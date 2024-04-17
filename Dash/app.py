import pandas as pd
import dash
import dash_html_components as html
import dash_pivottable
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from dash import dcc
from utils.plot_bars import plot_main_causes
import dash_bootstrap_components as dbc
from constants import column_defs, column_defs_reasons

# Update pivot table after further
# position of the button
app = dash.Dash(__name__)
server = app.server

df_commercial = pd.read_csv("Airplane_Crashes\Dash\commercial_crashes.csv")

df_commercial = df_commercial.sort_values(by="Date")[
    [
        "year",
        "Date",
        "Location",
        "Operator",
        "Type",
        "Aboard",
        "Fatalities",
        "Summary",
        "main_cause",
    ]
]


bar_fig = plot_main_causes(df_commercial, "Commercial records")
main_causes_commercial = df_commercial["main_cause"].unique()
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.Div(html.H2(children="Commercial crashes records")),
                        ]
                    ),
                    width=2,
                ),
                dbc.Col(
                    html.Div(
                        [
                            dag.AgGrid(
                                id="my-table",
                                style={"height": 1200, "width": 2000},
                                columnDefs=column_defs,
                                rowData=df_commercial.to_dict("records"),
                                defaultColDef={
                                    "filter": True,
                                    "sortable": True,
                                },
                                columnSize="sizeToFit",
                                dashGridOptions={
                                    "pagination": True,
                                    "paginationPageSize": 50,
                                    "enableCellTextSelection": True,
                                },
                            ),
                            html.Div(
                                [
                                    html.Button(
                                        "Show Pivot Table",
                                        id="pivot-table-button",
                                        n_clicks=0,
                                        className="btn btn-primary",
                                    )
                                ],
                                style={"margin-top": "40px"},
                            ),
                        ],
                        className="ag-theme-alpine",
                    )
                ),
            ]
        ),
        dbc.Row([dbc.Col([html.Div(id="pivot-table-container")])]),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="bar-chart-commerical", figure=bar_fig)),
                dbc.Row(html.Div(style={"height": "20px"})),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(html.H2(children="Select reason")),
                                ]
                            ),
                            width=2,
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="main-cause-dropdown",
                                options=[
                                    {"label": cause, "value": cause}
                                    for cause in main_causes_commercial
                                ],
                                value=main_causes_commercial[0],  # Default value
                                clearable=False,
                                style={"width": "300px"},
                            ),
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(html.Div(style={"height": "20px"})),
        dbc.Row([dbc.Col([html.Div(id="ag-grid")])]),
    ],
    fluid=True,
)


@app.callback(Output("ag-grid", "children"), [Input("main-cause-dropdown", "value")])
def update_grid(selected_main_cause):
    # Filter the DataFrame based on the selected main cause
    filtered_df = df_commercial[df_commercial["main_cause"] == selected_main_cause]
    filtered_df = filtered_df.drop(columns=["main_cause"], axis=1)

    # Create the AG Grid component to display the filtered DataFrame
    grid = dag.AgGrid(
        style={"height": 1200, "width": 2000},
        id="selected-table",
        columnDefs=column_defs_reasons,
        defaultColDef={
            "filter": True,
            "sortable": True,
        },
        rowData=filtered_df.to_dict("records"),
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 50,
            "enableCellTextSelection": True,
        },
        className="ag-theme-alpine",
    )

    return grid


@app.callback(
    Output("pivot-table-container", "children"),
    [Input("pivot-table-button", "n_clicks")],
    [State("my-table", "virtualRowData")],
)
def update_pivot_table(n_clicks, filtered_data):
    if n_clicks:
        if filtered_data:
            df_filtered = pd.DataFrame(filtered_data)

            # Create the pivot table based on the filtered data
            pivot_table = dash_pivottable.PivotTable(
                data=df_filtered.to_dict("records"),
                rows=["Type"],  # Define rows for the pivot table
                vals=["Fatalities"],  # Define values for the pivot table
                aggregatorName="Sum",
            )

            return pivot_table
    return None


if __name__ == "__main__":
    app.run_server(debug=True)
