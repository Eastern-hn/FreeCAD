# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2022 Yorik van Havre <yorik@uncreated.net>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

# add import/export types

FreeCAD.addExportType("Industry Foundation Classes (*.ifc)","importers.exportIFC")
# FreeCAD.addImportType("Industry Foundation Classes (*.ifc)","importIFC")
FreeCAD.addImportType("Industry Foundation Classes (*.ifc)", "nativeifc.ifc_import")
FreeCAD.addExportType("Industry Foundation Classes - IFCJSON (*.ifcJSON)","importers.exportIFC")
FreeCAD.addImportType("Wavefront OBJ - Arch module (*.obj *.OBJ)","importers.importOBJ")
FreeCAD.addExportType("Wavefront OBJ - Arch module (*.obj)","importers.importOBJ")
FreeCAD.addExportType("WebGL file (*.html)","importers.importWebGL")
FreeCAD.addExportType("JavaScript Object Notation (*.json)","importers.importJSON")
FreeCAD.addImportType("Collada (*.dae *.DAE)","importers.importDAE")
FreeCAD.addExportType("Collada (*.dae)","importers.importDAE")
FreeCAD.addImportType("3D Studio mesh (*.3ds *.3DS)","importers.import3DS")
FreeCAD.addImportType("SweetHome3D (*.sh3d)","importers.importSH3D")
FreeCAD.addImportType("Shapefile (*.shp *.SHP)","importers.importSHP")

FreeCAD.__unit_test__ += ["TestArch"]