import { createRender } from "@anywidget/react";
import { Counter } from "./components/Counter";

function App() {
    return (
        <div className="counter-widget">
            <Counter />
        </div>
    );
}

export default {
    render: createRender(App),
};
