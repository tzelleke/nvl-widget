import { useModelState } from "@anywidget/react";
import { BasicNvlWrapper } from "@neo4j-nvl/react";

export function Graph() {
    const [nodes] = useModelState("nodes");
    const [rels] = useModelState("rels");

    return (
        <BasicNvlWrapper
            nodes={nodes}
            rels={rels}
            nvlOptions={{ initialZoom: 2 }}
            nvlCallbacks={{ onLayoutDone: () => console.log('layout done') }}
        />
    );
}
