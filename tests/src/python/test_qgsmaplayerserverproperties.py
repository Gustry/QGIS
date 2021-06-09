"""QGIS Unit tests for QgsMapLayerServerProperties

From build dir, run:
ctest -R PyQgsMapLayerServerProperties -V

.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

__author__ = 'Etienne Trimaille'
__date__ = '21/05/2021'
__copyright__ = 'Copyright 2021, The QGIS Project'

from qgis.core import (
    QgsMapLayerServerProperties,
    QgsVectorLayer,
)
from qgis.testing import start_app, unittest

app = start_app()


class TestQgsMapLayerServerConfig(unittest.TestCase):

    def test_read_write(self):
        """ Test read write the structure about metadata url. """
        layer = QgsVectorLayer('Point?field=fldtxt:string', 'layer_1', 'memory')
        server_properties = QgsMapLayerServerProperties(layer)
        self.assertListEqual([], server_properties.metadataUrl())
