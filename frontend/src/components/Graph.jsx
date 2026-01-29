import { useModelState } from "@anywidget/react";
import { BasicNvlWrapper } from "@neo4j-nvl/react";

export function Graph() {
    const [graphData] = useModelState("graph_data");
    const { nodes = [], rels = [] } = graphData ?? {};

    return (
        <BasicNvlWrapper
            nodes={nodes}
            rels={rels}
            nvlOptions={{ initialZoom: 2 }}
            nvlCallbacks={{ onLayoutDone: () => console.log('layout done') }}
        />
    );
}
