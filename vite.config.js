import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "build"
  },
  server: {
    proxy: {
      "/api": {
        target: "http://174.138.189.44:3000/",
        changeOrigin: true,
      },
    }
  },
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "./test/setup.js",
    passWithNoTests: true
  },
});
