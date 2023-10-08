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
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: document,
) -> None:
    theme_options = _get_theme_options(app)
    if not theme_options:
        return

    context["extra_navbar_items"] = theme_options.get("extra_navbar_items")
    context["use_page_nav"] = theme_options.get("use_page_nav", True)
    context["github_repo_link"] = f"https://github.com/litestar-org/{theme_options['github_repo_name']}"
    context["discord_link"] = theme_options.get(
        "discord_link",
        "https://discord.gg/X3FJqy8d2j",
    )
    context["twitter_link"] = theme_options.get(
        "twitter_link",
        "https://twitter.com/LitestarAPI",
    )
    context["reddit_link"] = theme_options.get(
        "reddit_link",
        "https://www.reddit.com/r/litestarapi",
    )


def update_global_config(app: Sphinx) -> None:
    if not app.config["html_logo"]:
        app.config["html_logo"] = "_static/logo.svg"

    if not app.config["html_favicon"]:
        app.config["html_favicon"] = "_static/favicon.png"

    theme_options = _get_theme_options(app)
    if not theme_options:
        return

    github_repo_name = theme_options.get("github_repo_name")
    if not github_repo_name:
        msg = "GitHub URL not provided. Set 'github_repo_name=...' in html_theme_options"
        raise ValueError(msg)
    icon_links = theme_options.setdefault("icon_links", [])
    icon_links.extend(
        [
            {
                "name": "GitHub",
                "url": f"https://github.com/litestar-org/{github_repo_name}",
                "icon": "fa-brands fa-github",
                "type": "fontawesome",
            },
            {
                "name": "Discord",
                "url": "https://discord.gg/X3FJqy8d2j",
                "icon": "fa-brands fa-discord",
                "type": "fontawesome",
            },
        ],
    )


def setup(app: Sphinx) -> dict[str, bool]:
    theme_path = Path(__file__).parent / "theme"

    app.add_html_theme("litestar_sphinx_theme", str(theme_path))
    app.connect("html-page-context", update_html_context)
    app.connect("builder-inited", update_global_config)

    app.add_css_file("litestar-sphinx-theme.css", priority=1000)
    app.add_js_file("litestar-theme.js")

    return {"parallel_read_safe": True, "parallel_write_safe": True}
