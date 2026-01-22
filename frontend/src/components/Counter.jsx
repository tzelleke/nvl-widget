import { useModelState } from "@anywidget/react";

export function Counter() {
    const [count, setCount] = useModelState("count");

    return (
        <button onClick={() => setCount(count + 1)}>
            count is {count}
        </button>
    );
}
