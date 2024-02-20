# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'vrtool_docs'
copyright = '2023, Deltares'
author = 'Carles S. Soriano Perez'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel'
]
source_suffix = ['.rst', '.md']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
# html_css_files = ['css/custom.css']


html_context = {
    "github_url": "https://github.com",  # or your GitHub Enterprise interprise
    "github_user": "Deltares",
    "github_repo": "VrtoolDocumentation",
    "github_version": "main",  # FIXME
    "doc_path": "docs",
    "default_mode": "light",
}

html_css_files = ["css/theme-deltares.css"]
html_theme_options = {
    "show_nav_level": 2,
    "navbar_align": "content",
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deltares/hydromt",  # required
            "icon": "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
            "type": "url",
        },
        {
            "name": "Deltares",
            "url": "https://www.deltares.nl/en/",
            "icon": "_static/deltares-blue.svg",
            "type": "local",
        },
    ],
    "logo": {
        "text": "Veiligheidsrendement",
    },
    "navbar_end": ["navbar-icon-links", "version-switcher"],  # remove dark mode switch
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/Deltares/hydromt/gh-pages/switcher.json",
        "version_match": "0.0",
    },
}