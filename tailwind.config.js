/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./assets/js/*.js"],
  theme: {
      extend: {
          fontFamily: {
              sans: ['Inter', 'sans-serif'],
              display: ['Poppins', 'sans-serif'],
          },
          colors: {
              dark: '#050505',
              light: '#ffffff',
          }
      }
  },
  plugins: [],
}
