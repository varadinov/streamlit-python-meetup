import { defineConfig } from 'vite'

export default defineConfig({
  base: process.env.SLIDEV_BASE_PATH || '/', // Default to root if no env var is provided
})