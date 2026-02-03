import { useModelState } from "@anywidget/react";
import { InteractiveNvlWrapper } from "@neo4j-nvl/react";

export function Graph() {
    const [graphData] = useModelState("graph_data");
    const [selectedNodes, setSelectedNodes] = useModelState("selected_nodes");
    const [selectedRels, setSelectedRels] = useModelState("selected_rels");

    const { nodes = [], rels = [] } = graphData ?? {};

    // Apply selection styling
    const styledNodes = nodes.map((node) => ({
        ...node,
        selected: selectedNodes.includes(node.id),
    }));

    const styledRels = rels.map((rel) => ({
        ...rel,
        selected: selectedRels.includes(rel.id),
    }));

    const mouseEventCallbacks = {
        onNodeClick: (node, hitTargets, evt) => {
            console.log("Node clicked:", node, hitTargets, evt);
            if (evt.shiftKey || evt.metaKey) {
                // Multi-select: toggle
                setSelectedNodes(
                    selectedNodes.includes(node.id)
                        ? selectedNodes.filter((id) => id !== node.id)
                        : [...selectedNodes, node.id]
                );
            } else {
                // Single select: replace
                setSelectedNodes([node.id]);
                setSelectedRels([]);
            }
        },
        onRelationshipClick: (rel, hitTargets, evt) => {
            console.log("Relationship clicked:", rel, hitTargets, evt);
            if (evt.shiftKey || evt.metaKey) {
                // Multi-select: toggle
                setSelectedRels(
                    selectedRels.includes(rel.id)
                        ? selectedRels.filter((id) => id !== rel.id)
                        : [...selectedRels, rel.id]
                );
            } else {
                // Single select: replace
                setSelectedRels([rel.id]);
                setSelectedNodes([]);
            }
        },
        onCanvasClick: () => {
            console.log("Canvas clicked");
            setSelectedNodes([]);
            setSelectedRels([]);
        },
    };

    return (
        <InteractiveNvlWrapper
            nodes={styledNodes}
            rels={styledRels}
            nvlOptions={{ initialZoom: 2 }}
            mouseEventCallbacks={mouseEventCallbacks}
        />
    );
}
