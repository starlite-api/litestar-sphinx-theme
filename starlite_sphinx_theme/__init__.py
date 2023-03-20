from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.addnodes import document
    from sphinx.application import Sphinx


def _get_theme_options(app: Sphinx) -> dict[str, Any] | None:
    if hasattr(app.builder, "theme_options"):
        return app.builder.theme_options  # type: ignore[attr-defined]

    if hasattr(app.config, "html_theme_options"):
        return app.config.html_theme_options
    return None


def update_html_context(
    app: Sphinx, pagename: str, templatename: str, context: dict[str, Any], doctree: document
) -> None:
    theme_options = _get_theme_options(app)
    if not theme_options:
        return

    context["navbar_items"] = theme_options.get("navbar_items")


def setup(app: Sphinx) -> None:
    theme_path = Path(__file__).parent / "theme"

    app.setup_extension("sphinx_design")
    app.setup_extension("sphinx_copybutton")
    app.add_html_theme("starlite_sphinx_theme", str(theme_path))
    app.connect("html-page-context", update_html_context)

    app.add_css_file("style.css")
