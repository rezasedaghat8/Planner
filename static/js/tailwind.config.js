/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "gray-SecondaryColor": "#7A7B7C",
        "orange-Secondary": "#F97C35",
        "black-Secondary": "#222325",
        "blue-Secondary": "#359BF9",
      },
      spacing: {
        "30%": "30%",
        "28%": "28%",
        "65%": "65%",
        "93%": "93%",
        "150%": "150%",
        70: "17rem",
        36.5: "9.5rem",
      },
    },
    borderWidth: {
      DEFAULT: "1px",
      0: "0",
      1: "1px",
      2: "2px",
      3: "3px",
      4: "4px",
      6: "6px",
      8: "8px",
    },
  },
  plugins: [],
};
