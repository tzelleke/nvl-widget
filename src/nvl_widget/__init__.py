import pathlib
from dataclasses import dataclass, field, asdict

import anywidget
import traitlets

_bundler_output_dir = pathlib.Path(__file__).parent.parent / "static"


@dataclass
class Node:
    id: str
    caption: str | None = None
    color: str | None = None
    size: int | None = None


@dataclass
class Relationship:
    id: str
    from_: str
    to: str
    caption: str | None = None
    color: str | None = None

    def to_dict(self):
        """Convert to dict with 'from' key (since 'from' is a Python keyword)."""
        d = asdict(self)
        d["from"] = d.pop("from_")
        return d


@dataclass
class GraphData:
    nodes: list[Node] = field(default_factory=list)
    rels: list[Relationship] = field(default_factory=list)

    def to_dict(self):
        return {
            "nodes": [asdict(n) for n in self.nodes],
            "rels": [r.to_dict() for r in self.rels],
        }


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
