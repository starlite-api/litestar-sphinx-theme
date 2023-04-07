/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        'litestar_sphinx_theme/**/*.{html,svg}',
    ],
    darkMode: ['class', '[data-theme="dark"]'],
    theme: {
        extend: {
            colors: {
                "litestar-gold": "#EDB641"
            }
        }
    }
}
