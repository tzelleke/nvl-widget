import pathlib

import anywidget
import traitlets

from .models import GraphData


def _graph_data_to_json(value: GraphData | None, widget) -> dict | None:
    """Serialize GraphData to JSON for frontend sync."""
    if value is None:
        return None
    return value.to_dict()


def _graph_data_from_json(value: dict | None, widget) -> GraphData | None:
    """Deserialize JSON to GraphData from frontend sync."""
    if value is None:
        return None
    return GraphData.from_dict(value)


_bundler_output_dir = pathlib.Path(__file__).parent.parent / "static"


class GraphWidget(anywidget.AnyWidget):
    # _esm = _bundler_output_dir / "index.js"
    _esm = "http://localhost:5173/src/index.jsx?anywidget"

    graph_data = traitlets.Instance(GraphData, allow_none=True).tag(
        sync=True,
        to_json=_graph_data_to_json,
        from_json=_graph_data_from_json,
    )

    def __init__(self, graph_data: GraphData | None = None, **kwargs):
        kwargs.setdefault("graph_data", graph_data)
        super().__init__(**kwargs)
