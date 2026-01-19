import anywidget
import traitlets


class CounterWidget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
      let button = document.createElement("button");
      button.innerHTML = `count is ${model.get("count")}`;
      button.addEventListener("click", () => {
        model.set("count", model.get("count") + 1);
        model.save_changes();
      });
      model.on("change:count", () => {
        button.innerHTML = `count is ${model.get("count")}`;
      });
      el.classList.add("counter-widget");
      el.appendChild(button);
    }
    export default { render };
    """
    _css = """
    .counter-widget button { color: white; font-size: 1.75rem; background-color: #ea580c; padding: 0.5rem 1rem; border: none; border-radius: 0.25rem; }
    .counter-widget button:hover { background-color: #9a3412; }
    """
    count = traitlets.Int(0).tag(sync=True)
