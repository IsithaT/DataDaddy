/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'excel': {
          50: '#f0faf4',
          100: '#d8f3e3',
          200: '#b3e6ca',
          300: '#7ed3aa',
          400: '#4ab785',
          500: '#2b9d6a',
          600: '#217f55',
          700: '#1d6646',
          800: '#1b523a',
          900: '#184432',
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

