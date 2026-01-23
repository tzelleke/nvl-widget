import { createRender } from "@anywidget/react";
import { Graph } from "./components/Graph";

function Widget() {
    return (
        <div style={{ width: '100%', height: 500 }}>
            <Graph />
        </div>
    );
}

export default {
    render: createRender(Widget),
};
