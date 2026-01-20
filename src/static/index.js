const c = {
  initialize({ model: t }) {
    return () => {
    };
  },
  render({ model: t, el: e }) {
    let n = document.createElement("button");
    return n.innerHTML = `count: ${t.get("count")}`, n.addEventListener("click", () => {
      t.set("count", t.get("count") + 1), t.save_changes();
    }), t.on("change:count", () => {
      n.innerHTML = `count: ${t.get("count")}`;
    }), e.classList.add("counter-widget"), e.appendChild(n), () => {
    };
  }
};
export {
  c as default
};
