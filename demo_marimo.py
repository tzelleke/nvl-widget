import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")

with app.setup:
    import nvl_widget


@app.cell
def _():
    nvl_widget.GraphWidget()
    return


if __name__ == "__main__":
    app.run()
