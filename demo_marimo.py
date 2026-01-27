import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")

with app.setup:
    from nvl_widget import (
        GraphData,
        GraphWidget,
        Node,
        Relationship,
    )


@app.cell
def _():
    graph_data = GraphData(
        nodes=[
            Node(id="1", caption="Alice", color="#ffdf81", size=20),
            Node(id="2", caption="Bob", color="#81caff", size=20),
            Node(id="3", caption="Charlie", color="#a1ff81", size=20),
            Node(id="4", caption="Diana", color="#ff81bf", size=20),
        ],
        rels=[
            Relationship(id="r1", from_="1", to="2", caption="KNOWS"),
            Relationship(id="r2", from_="1", to="3", caption="KNOWS"),
            Relationship(id="r3", from_="2", to="3", caption="WORKS_WITH"),
            Relationship(id="r4", from_="2", to="4", caption="KNOWS"),
            Relationship(id="r5", from_="3", to="4", caption="FRIENDS"),
            Relationship(id="r6", from_="4", to="1", caption="FOLLOWS"),
        ],
    )
    return (graph_data,)


@app.cell
def _(graph_data):
    widget = GraphWidget(graph_data=graph_data)
    widget
    return


if __name__ == "__main__":
    app.run()
