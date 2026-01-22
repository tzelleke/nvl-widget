import { defineConfig } from "vite";
import anywidget from "@anywidget/vite";

export default defineConfig(({ command }) => {
    let define = {};
    if (command === "build") {
        define["process.env.NODE_ENV"] = JSON.stringify("production");
    }
    return {
        esbuild: {
            jsxInject: `import React from 'react'`,
        },
        build: {
            outDir: "../src/static/",
            emptyOutDir: true,
            lib: {
                entry: ["src/index.jsx"],
                formats: ["es"],
            },
        },
        plugins: [anywidget()],
        define,
    };
});
