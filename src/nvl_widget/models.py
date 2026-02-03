from __future__ import annotations

from pydantic import (
    BaseModel,
    Field,
)


class Node(BaseModel):
    """A node in the graph."""

    id: str
    caption: str | None = None
    color: str | None = None
    size: int | None = None


class Relationship(BaseModel):
    """A relationship (edge) in the graph."""

    id: str
    from_: str = Field(serialization_alias="from")
    to: str
    caption: str | None = None
    color: str | None = None


class GraphData(BaseModel):
    """Container for graph nodes and relationships."""

    nodes: list[Node] = Field(default_factory=list)
    rels: list[Relationship] = Field(default_factory=list)
