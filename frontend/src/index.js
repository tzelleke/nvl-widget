export default {

  initialize({ model }) {
    // Set up shared state or event handlers.
    return () => {
      // Optional: Called when the widget is destroyed.
    }
  },

  render({ model, el }) {
    // Render the widget's view into the el HTMLElement.
    let button = document.createElement("button");

    button.innerHTML = `count: ${model.get("count")}`;
    button.addEventListener("click", () => {
      model.set("count", model.get("count") + 1);
      model.save_changes();
    });

    model.on("change:count", () => {
      button.innerHTML = `count: ${model.get("count")}`;
    });

    el.classList.add("counter-widget");
    el.appendChild(button);

    return () => {
      // Optional: Called when the view is destroyed.
    }
  }

}
