import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")

with app.setup:
    import pandas as pd

    from nvl_widget import GraphWidget


@app.cell
def _():
    nodes_df = pd.DataFrame(
        {
            "id": ["1", "2", "3", "4"],
            "caption": ["Alice", "Bob", "Charlie", "Diana"],
            "color": ["#ffdf81", "#81caff", "#a1ff81", "#ff81bf"],
            "size": [20, 20, 20, 20],
        }
    )

    rels_df = pd.DataFrame(
        {
            "id": ["r1", "r2", "r3", "r4", "r5", "r6"],
            "from": ["1", "1", "2", "2", "3", "4"],
            "to": ["2", "3", "3", "4", "4", "1"],
            "caption": [
                "KNOWS",
                "KNOWS",
                "WORKS_WITH",
                "KNOWS",
                "FRIENDS",
                "FOLLOWS",
            ],
        }
    )
    return nodes_df, rels_df


@app.cell
def _(nodes_df, rels_df):
    widget = GraphWidget.from_dataframes(nodes_df, rels_df)
    widget
    return (widget,)


@app.cell
def _(widget):
    # Selection state is reactive - click nodes/rels in the graph to see changes
    f"Selected nodes: {widget.selected_nodes}, Selected rels: {widget.selected_rels}"
    return


if __name__ == "__main__":
    app.run()
