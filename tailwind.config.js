/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        'litestar_sphinx_theme/**/*.{html,svg}',
    ],
    darkMode: ['class', '[data-theme="dark"]'],
    theme: {
        extend: {
            colors: {
                "litestar-blue": "#202235",
                "litestar-gold": "#EDB641",
                "litestar-yellow": "#FFD480",
                "litestar-gray": "#DCDFE4",
                "litestar-light": "#ffffff",
                "litestar-dark": "#202020",
            }
        }
    }
}
