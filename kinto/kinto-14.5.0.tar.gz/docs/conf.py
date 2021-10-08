#
# Kinto documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  2 15:08:06 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import datetime
import os
import sys

import pkg_resources

# abspath because this could be __main__, in which case it may not
# have an absolute __file__
__HERE__ = os.path.dirname(os.path.abspath(__file__))

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.io uses their theme by default, so no need to specify
# it

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinxcontrib.httpdomain",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
html_additional_pages = {"index": "indexcontent.html"}


# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Kinto"
copyright = "2015-%s — Mozilla Services" % datetime.datetime.now().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# The full version, including alpha/beta/rc tags.
version = pkg_resources.get_distribution("kinto").version
release = ".".join(version.split(".")[:2])

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = "Kintodoc"


# -- Options for autodoc --------------------------------------------------

autodoc_member_order = "bysource"
# Enable nitpicky mode - which ensures that all references in the docs
# resolve.
# See: http://stackoverflow.com/a/30624034/186202
nitpicky = True
nitpick_ignore = [
    ("py:class", "bool"),
    ("py:class", "dict"),
    ("py:class", "float"),
    ("py:class", "int"),
    ("py:class", "list"),
    ("py:class", "str"),
    ("py:class", "tuple"),
    ("py:class", "Exception"),
    ("py:class", "cornice.Service"),
    # Member autodoc fails with those:
    # kinto.core.resource.schema
    ("py:class", "Integer"),
    ("py:class", "String"),
    # kinto.core.resource
    ("py:class", "Model"),
    ("py:class", "ResourceSchema"),
    ("py:class", "ViewSet"),
    ("py:class", "Sequence"),
    # kinto.core.resource.schema
    ("py:attr", "colander.null"),
]


# -- Options of extlinks --------------------------------------------------

extlinks = {
    "github": ("https://github.com/%s/", ""),
    "rtd": ("https://%s.readthedocs.io", ""),
    "blog": ("https://mozilla-services.github.io/servicedenuages.fr/en/%s", ""),
}


# -- Substitutions

rst_epilog = """
.. |status-200| replace:: ``200 OK``
.. |status-201| replace:: ``201 Created``
.. |status-304| replace:: ``304 Not Modified``
.. |status-400| replace:: ``400 Bad Request``
.. |status-401| replace:: ``401 Unauthorized``
.. |status-403| replace:: ``403 Forbidden``
.. |status-404| replace:: ``404 Not Found``
.. |status-405| replace:: ``405 Method Not Allowed``
.. |status-406| replace:: ``406 Not Acceptable``
.. |status-409| replace:: ``409 Conflict``
.. |status-410| replace:: ``410 Gone``
.. |status-412| replace:: ``412 Precondition Failed``
.. |status-415| replace:: ``415 Unsupported Media Type``
.. |status-503| replace:: ``503 Service Unavailable``
"""


# --
def setup(app):
    # path relative to _static
    app.add_css_file("theme_overrides.css")
    app.add_js_file("piwik.js")


# -- Options for intersphinx --------------------------------------------------

intersphinx_mapping = {
    "colander": ("https://colander.readthedocs.io/en/latest/", None),
    "cornice": ("https://cornice.readthedocs.io/en/latest/", None),
    "pyramid": ("https://pyramid.readthedocs.io/en/latest/", None),
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Kinto.tex", "Kinto Documentation", "Mozilla Services — Da French Team", "manual")
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "kinto", "Kinto Documentation", ["Mozilla Services — Da French Team"], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Kinto",
        "Kinto Documentation",
        "Mozilla Services — Da French Team",
        "Kinto",
        "A remote storage service with syncing and sharing abilities.",
        "Miscellaneous",
    )
]
