/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {
      colors: {
        // Define your custom colors here
        'custom-dark': '#25262f',
        'custom-2': '#282c34',
        // Add more custom colors as needed
    },
  },
},
  plugins: [],
}

