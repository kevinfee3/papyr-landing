/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        'canvas-white': '#F9FAFB',
        'ink-black': '#111827',
        'paper-plane-blue': '#3B82F6',
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
      },
      fontSize: {
        'headline-lg': '44px',
        'headline-sm': '36px',
        'body-lg': '18px',
        'body-sm': '16px',
      }
    },
  },
  plugins: [],
}
