# -- Project information -----------------------------------------------------

project = 'Fubo TV Connect Guide'
copyright = '2025, Fubo TV'
author = 'Fubo TV Team'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # you can change to 'sphinx_rtd_theme' if installed
html_static_path = ['_static']

# Custom brand styling (Fubo color)
html_theme_options = {
    'logo': 'fubo_logo.png',        # place your logo inside _static folder
    'logo_name': True,
    'description': 'How to Connect Fubo on Your TV',
    'fixed_sidebar': True,
    'page_width': '90%',
    'sidebar_width': '220px',
    'body_text_align': 'justify',
}

# Optional: add your CSS to style the HTML button or adjust brand color
def setup(app):
    app.add_css_file('custom.css')
