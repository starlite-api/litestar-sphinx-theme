.PHONY: INSTALL
install:
	poetry install
	npm install

.PHONY: build-assets
build-assets:
	npx tailwindcss -i litestar_sphinx_theme/style.css -o litestar_sphinx_theme/theme/static/litestar-sphinx-theme.css -m
