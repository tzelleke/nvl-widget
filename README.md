# NVL Widget

A Python widget for visualizing graph data using [Neo4j NVL (Network Visualization Library)](https://neo4j.com/docs/nvl/current/) in Marimo notebooks via [anywidget](https://anywidget.dev/).

## Overview

This project provides a bridge between Python and Neo4j's graph visualization library, allowing you to render interactive graph visualizations directly in Marimo notebooks.

## Project Structure

```plain
neo4j-nvl-anywidget/
├── demo_marimo.py           # Demo Marimo notebook
├── pyproject.toml           # Python project configuration
├── frontend/                # Frontend widget code
│   ├── package.json         # Node.js dependencies
│   ├── vite.config.js       # Vite build configuration
│   └── src/
│       ├── index.jsx        # Widget entry point
│       └── components/
│           └── Graph.jsx    # Neo4j NVL React component
└── src/
    └── nvl_widget/
        ├── __init__.py      # Package exports
        ├── models.py        # Data classes (Node, Relationship, GraphData)
        └── widget.py        # GraphWidget class
```

## Dependencies

### Python Dependencies

- `anywidget` - Framework for creating custom Jupyter/Marimo widgets
- `traitlets` - Configuration system for Python applications

### Frontend Dependencies

- `@neo4j-nvl/react` - Neo4j Network Visualization Library React wrapper
- `@anywidget/react` - React bindings for anywidget
- `@anywidget/vite` - Vite plugin for anywidget

## Development Setup

### Prerequisites

- Python 3.14+
- Node.js (for frontend development)
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1. **Clone the repository**:

   ```bash
   git clone tzelleke/nvl-widget
   cd nvl-widget
   ```

2. **Install Python dependencies**:

   ```bash
   uv sync
   ```

3. **Install frontend dependencies**:

   ```bash
   cd frontend
   npm install
   ```

## Running in Development Mode

Development mode uses Vite's hot module replacement for rapid frontend iteration.

1. **Start the Vite dev server** (in one terminal):

   ```bash
   cd frontend
   npm run dev
   ```

   This serves the frontend at `http://localhost:5173`.

2. **Run the Marimo demo** (in another terminal):

   ```bash
   uv run marimo edit demo_marimo.py
   ```

The widget is configured to load from the Vite dev server during development (see `_esm` in `src/nvl_widget/__init__.py`).

## Running the Demo Notebook

```bash
uv run marimo edit demo_marimo.py
```

The demo creates a simple graph with 4 nodes (Alice, Bob, Charlie, Diana) and 6 relationships between them.

## Building for Production

To build the frontend bundle for production:

```bash
cd frontend
npm run build
```

This outputs the bundled JavaScript to `src/static/`. To use the production bundle, update `GraphWidget` in `src/nvl_widget/__init__.py`:

```python
_esm = _bundler_output_dir / "index.js"  # Use this for production
# _esm = "http://localhost:5173/src/index.jsx?anywidget"  # Comment out dev URL
```

## Usage Example

```python
from nvl_widget import (
   GraphData,
   GraphWidget,
   Node,
   Relationship,
)

graph_data = GraphData(
    nodes=[
        Node(id="1", caption="Alice", color="#ffdf81", size=20),
        Node(id="2", caption="Bob", color="#81caff", size=20),
    ],
    rels=[
        Relationship(id="r1", from_="1", to="2", caption="KNOWS"),
    ],
)

widget = GraphWidget(graph_data=graph_data)
widget
```

## API Reference

### `Node`

- `id` (str): Unique identifier
- `caption` (str, optional): Display label
- `color` (str, optional): Hex color code
- `size` (int, optional): Node size

### `Relationship`

- `id` (str): Unique identifier
- `from_` (str): Source node ID (note the underscore to avoid Python keyword conflict)
- `to` (str): Target node ID
- `caption` (str, optional): Relationship label
- `color` (str, optional): Hex color code

### `GraphData`

- `nodes` (list[Node]): List of nodes
- `rels` (list[Relationship]): List of relationships

### `GraphWidget`

- `graph_data` (GraphData, optional): Graph data to visualize
