# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gns3server.version import __version__


async def test_version_output(compute_api, config):

    config.set("Server", "local", "true")
    response = await compute_api.get('/version')
    assert response.status == 200
    assert response.json == {'local': True, 'version': __version__}


async def test_debug_output(compute_api):

    response = await compute_api.get('/debug')
    assert response.status == 200


async def test_statistics_output(compute_api):

    response = await compute_api.get('/statistics')
    assert response.status == 200
