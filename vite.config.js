import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

//https://vitejs.dev/config/#using-environment-variables-in-config
const env = loadEnv('','');
const api_url = JSON.stringify(env.VITE_API_URL);


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "build"
  },
  server: {
    proxy: {
      "/api": {
        target: api_url,
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

// import { defineConfig, loadEnv } from 'vite';
// import react from '@vitejs/plugin-react';
// import compressionPlugin from 'vite-plugin-compression';
//
// export default defineConfig(({ mode }) => {
//   const env = loadEnv(mode, process.cwd());
//   const api_url = env.VITE_API_URL;
//
//   return {
//     plugins: [
//       react(),
//       compressionPlugin({
//         disable: true,  // Disable or configure appropriately
//       })
//     ],
//     build: {
//       outDir: 'build',
//       sourcemap: true,
//     },
//     server: {
//       proxy: {
//         '/api/': {
//           target: api_url,
//           changeOrigin: true,
//           rewrite: path => path.replace(/^\/api/, ''),
//         },
//       }
//     },
//     test: {
//       globals: true,
//       environment: 'jsdom',
//       setupFiles: './test/setup.js',
//       passWithNoTests: true
//     },
//   };
// });
