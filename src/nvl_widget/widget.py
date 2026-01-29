import pathlib

import anywidget
import traitlets

from .models import GraphData

_bundler_output_dir = pathlib.Path(__file__).parent.parent / "static"


class GraphWidget(anywidget.AnyWidget):
    # _esm = _bundler_output_dir / "index.js"
    _esm = "http://localhost:5173/src/index.jsx?anywidget"

    nodes = traitlets.List([]).tag(sync=True)
    rels = traitlets.List([]).tag(sync=True)

    def __init__(self, graph_data: GraphData | None = None, **kwargs):
        if graph_data is not None:
            data = graph_data.to_dict()
            kwargs.setdefault("nodes", data["nodes"])
            kwargs.setdefault("rels", data["rels"])
        super().__init__(**kwargs)
