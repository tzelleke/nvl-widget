import pathlib

import anywidget
import traitlets

_bundler_output_dir = pathlib.Path(__file__).parent / "static"


class CounterWidget(anywidget.AnyWidget):
    # _esm = _bundler_output_dir / "index.js"
    _esm = "http://localhost:5173/src/index.js?anywidget"
    _css = _bundler_output_dir / "style.css"

    count = traitlets.Int(0).tag(sync=True)
