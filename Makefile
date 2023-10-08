install:
	poetry install
	npm install

build-assets:
	npx tailwindcss -i litestar_sphinx_theme/style.css -o litestar_sphinx_theme/theme/static/litestar-sphinx-theme.css -m

.PHONY: refresh-lockfiles
refresh-lockfiles:                                 ## Sync lockfiles with requirements files.
	pdm update --update-reuse --group :all

.PHONY: lock
lock:                                             ## Rebuild lockfiles from scratch, updating all dependencies
	pdm update --update-eager --group :all