/** Tailwind config for San Cipriano — mirrors the former CDN inline config.
 *  Build:  npx tailwindcss@3 -c tailwind.config.js -i tailwind.input.css -o static/css/tailwind.css --minify
 */
module.exports = {
  darkMode: 'class',
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      colors: {
        selva: {
          50: '#f0fdf4', 100: '#dcfce7', 200: '#bbf7d0', 300: '#86efac', 400: '#4ade80',
          500: '#22c55e', 600: '#16a34a', 700: '#15803d', 800: '#166534', 900: '#14532d',
        },
        rio: {
          50: '#f0f9ff', 100: '#e0f2fe', 200: '#bae6fd', 300: '#7dd3fc', 400: '#38bdf8',
          500: '#0ea5e9', 600: '#0284c7', 700: '#0369a1', 800: '#075985', 900: '#0c4a6e',
        },
        tierra: {
          50: '#faf5f0', 100: '#f5ebe0', 200: '#e6d5c3', 300: '#d4b896', 400: '#c49a6c',
          500: '#b8834d', 600: '#a67042', 700: '#8a5a38', 800: '#704a33', 900: '#5c3e2c',
        },
      },
      fontFamily: {
        display: ['Georgia', 'serif'],
        body: ['system-ui', '-apple-system', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
