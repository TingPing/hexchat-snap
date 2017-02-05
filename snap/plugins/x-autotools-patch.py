# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2017 Patrick Griffis <tingping@tingping.se>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import path
from snapcraft.plugins.autotools import AutotoolsPlugin


class AutotoolsPlugin(AutotoolsPlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
 
        schema['properties']['patches'] = dict(
            type='array', minitems=1, uniqueItems=True,
            items=dict(type='string'), default=[],
        )

        return schema

    def build(self):
        for patch in self.options.patches:
            patch_path = path.join('../../../patches', patch)
            patch_cmd = ['patch', '-p1', '--input', patch_path]
            self.run(patch_cmd)

        super().build()

