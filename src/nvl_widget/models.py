from dataclasses import (
    asdict,
    dataclass,
    field,
)


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

    @classmethod
    def from_dict(cls, data: dict) -> "GraphData":
        """Reconstruct GraphData from a dict (e.g., from JSON)."""
        nodes = [Node(**n) for n in data.get("nodes", [])]
        rels = [
            Relationship(
                id=r["id"],
                from_=r["from"],
                to=r["to"],
                caption=r.get("caption"),
                color=r.get("color"),
            )
            for r in data.get("rels", [])
        ]
        return cls(nodes=nodes, rels=rels)
