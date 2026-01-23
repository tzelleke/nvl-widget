import pathlib

import anywidget

_bundler_output_dir = pathlib.Path(__file__).parent.parent / "static"


class GraphWidget(anywidget.AnyWidget):
    # _esm = _bundler_output_dir / "index.js"
    _esm = "http://localhost:5173/src/index.jsx?anywidget"
