"""psy-simple: The psyplot plugin for simple visualizations

This package contains the basic plotters for simple interactive visualization
tasks with the psyplot visualization framework.
"""

# Disclaimer
# ----------
#
# Copyright (C) 2021 Helmholtz-Zentrum Hereon
# Copyright (C) 2020-2021 Helmholtz-Zentrum Geesthacht
# Copyright (C) 2016-2021 University of Lausanne
#
# This file is part of psy-simple and is released under the GNU LGPL-3.O license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3.0 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU LGPL-3.0 license for more details.
#
# You should have received a copy of the GNU LGPL-3.0 license
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Philipp S. Sommer"
__copyright__ = """
Copyright (C) 2021 Helmholtz-Zentrum Hereon
Copyright (C) 2020-2021 Helmholtz-Zentrum Geesthacht
Copyright (C) 2016-2021 University of Lausanne
"""
__credits__ = ["Philipp S. Sommer"]
__license__ = "LGPL-3.0-only"

__maintainer__ = "Philipp S. Sommer"
__email__ = "psyplot@hereon.de"

__status__ = "Production"

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
