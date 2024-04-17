import plotly.express as px
import plotly.graph_objects as go


def plot_main_causes(df, records):
    main_cause_df = df.groupby("main_cause").agg({"Fatalities": ["sum", "count"]})
    main_cause_df.columns = [
        "_".join(col).rstrip("_") for col in main_cause_df.columns.values
    ]
    main_cause_df = main_cause_df.sort_values(by="Fatalities_sum", ascending=True)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=main_cause_df.index,
            x=main_cause_df["Fatalities_count"],
            name="Number of accidents",
            orientation="h",
            text=main_cause_df["Fatalities_count"],
            textposition="outside",
        )
    )

    # Bar for Total Fatalities
    fig.add_trace(
        go.Bar(
            y=main_cause_df.index,
            x=main_cause_df["Fatalities_sum"],
            name="Total Fatalities",
            orientation="h",
            text=main_cause_df["Fatalities_sum"],
            textposition="outside",
        )
    )

    # Update layout for readability
    fig.update_layout(
        title=records + " - Number of accidents and Total fatalities",
        barmode="group",
        bargap=0.10,  # Gap between bars of adjacent location coordinates,
        width=1200,
        height=700,
    )

    return fig
