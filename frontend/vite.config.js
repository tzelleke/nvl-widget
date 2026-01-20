import { defineConfig } from "vite";
import anywidget from "@anywidget/vite";

export default defineConfig({
    build: {
        outDir: "../src/static/",
        emptyOutDir: true,
        lib: {
            entry: ["src/index.js"],
            formats: ["es"],
        },
        plugins: [anywidget()],
    },
});
