import os
import sys
from pathlib import Path

from package import __version__

# Insert package root to path
_src_dir = Path(os.path.realpath(__file__)).parent
_package_root = _src_dir.parent.parent / "src"
sys.path.insert(0, str(_package_root))
sys.path.insert(0, str(_src_dir))

project = "package"
author = "Felix Hildén"
copyright = "2019-2024, Felix Hildén"
version = __version__
release = version

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_rtd_theme"]

html_theme = "sphinx_rtd_theme"
python_use_unqualified_type_names = True
autodoc_default_options = {"members": True, "undoc-members": True}
autodoc_typehints = "description"
