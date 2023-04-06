/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        'starlite_sphinx_theme/**/*.{html,svg}',
    ],
    darkMode: ['class', '[data-theme="dark"]'],
    theme: {
        extend: {
            colors: {
                "starlite-gold": "#EDB641"
            }
        }
    }
}
