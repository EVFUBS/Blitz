import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import 'dotenv'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    hmr: {
      clientPort: 3000
    },
    proxy: {
      '/api': {
        //target: 'http://127.0.0.1:8000',
        target: "http://api:8000/",
      },
      '/ws': {
        //target: 'ws://127.0.0.1:8000',
        target: "ws://api:8000/",
      }
    },
    base: '.',
  }
})
