from __future__ import annotations

import pathlib
from typing import Self

import anywidget
import pandas as pd
import traitlets

from .models import (
    GraphData,
    Node,
    Relationship,
)


def _graph_data_to_json(value: GraphData | None, widget) -> dict | None:
    """Serialize GraphData to JSON for frontend sync."""
    if value is None:
        return None
    return value.model_dump(by_alias=True)


def _graph_data_from_json(value: dict | None, widget) -> GraphData | None:
    """Deserialize JSON to GraphData from frontend sync."""
    if value is None:
        return None
    return GraphData.model_validate(value)


_bundler_output_dir = pathlib.Path(__file__).parent.parent / "static"


class GraphWidget(anywidget.AnyWidget):
    """Widget for visualizing graph data using Neo4j NVL."""

    # _esm = _bundler_output_dir / "index.js"
    _esm = "http://localhost:5173/src/index.jsx?anywidget"

    graph_data: GraphData | None = traitlets.Instance(GraphData, allow_none=True).tag(  # type: ignore[assignment]
        sync=True,
        to_json=_graph_data_to_json,
        from_json=_graph_data_from_json,
    )

    def __init__(self, graph_data: GraphData | None = None, **kwargs):
        """Initialize the widget.

        Args:
            graph_data: The graph data to visualize.
            **kwargs: Additional keyword arguments passed to the parent class.
        """
        kwargs.setdefault("graph_data", graph_data)
        super().__init__(**kwargs)

    @classmethod
    def from_dataframes(
        cls,
        nodes_df: pd.DataFrame,
        rels_df: pd.DataFrame,
        *,
        node_id: str = "id",
        node_caption: str | None = "caption",
        node_color: str | None = "color",
        node_size: str | None = "size",
        rel_id: str | None = "id",
        rel_from: str = "from",
        rel_to: str = "to",
        rel_caption: str | None = "caption",
        rel_color: str | None = "color",
    ) -> Self:
        """Create a GraphWidget from pandas DataFrames.

        Args:
            nodes_df: DataFrame containing node data.
            rels_df: DataFrame containing relationship data.
            node_id: Column name for node IDs.
            node_caption: Column name for node captions, or None to skip.
            node_color: Column name for node colors, or None to skip.
            node_size: Column name for node sizes, or None to skip.
            rel_id: Column name for relationship IDs, or None to auto-generate.
            rel_from: Column name for source node IDs.
            rel_to: Column name for target node IDs.
            rel_caption: Column name for relationship captions, or None to skip.
            rel_color: Column name for relationship colors, or None to skip.

        Returns:
            A new widget instance with the graph data.
        """
        nodes = [
            Node(
                id=str(row[node_id]),
                caption=row.get(node_caption) if node_caption else None,
                color=row.get(node_color) if node_color else None,
                size=row.get(node_size) if node_size else None,
            )
            for row in nodes_df.to_dict("records")
        ]

        rels = [
            Relationship(
                id=str(row[rel_id]) if rel_id and rel_id in row else f"r{idx}",
                from_=str(row[rel_from]),
                to=str(row[rel_to]),
                caption=row.get(rel_caption) if rel_caption else None,
                color=row.get(rel_color) if rel_color else None,
            )
            for idx, row in enumerate(rels_df.to_dict("records"))
        ]

        return cls(graph_data=GraphData(nodes=nodes, rels=rels))

    def to_dataframes(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Export graph data to pandas DataFrames.

        Returns:
            A tuple of (nodes_df, rels_df).

        Raises:
            ValueError: If graph_data is None.
        """
        if self.graph_data is None:
            raise ValueError("graph_data is None")

        nodes_df = pd.DataFrame.from_records(
            [node.model_dump() for node in self.graph_data.nodes]
        )
        rels_df = pd.DataFrame.from_records(
            [rel.model_dump(by_alias=True) for rel in self.graph_data.rels]
        )

        return nodes_df, rels_df
