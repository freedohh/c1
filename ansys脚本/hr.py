'''注意：由于记录功能正在研发中，因此不会记录所有工作流程。'''


#region Context Menu Action
geometry_import_12 = DataModel.GetObjectById(12)
geometry_import_12.Import(r"E:\Desktop\Structure-CAD.scdoc") # Primary Source!
#endregion

#region Context Menu Action
geometry_13 = Model.Geometry
point_mass_70 = geometry_13.AddPointMass()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1816, 1631]
point_mass_70.Location = selection
#endregion

#region Details View Action
point_mass_70.XCoordinate = Quantity(0, "m")
#endregion

#region Details View Action
point_mass_70.YCoordinate = Quantity(0, "m")
#endregion

#region Details View Action
point_mass_70.ZCoordinate = Quantity(0.0018, "m")
#endregion

#region Details View Action
point_mass_70.Mass = Quantity(0.12612, "kg")
#endregion

#region Context Menu Action
connection_group_75 = connections_45.AddConnectionGroup()
#endregion

#region Context Menu Action
contact_region_76 = connection_group_75.AddContactRegion()
#endregion

#region Context Menu Action
contact_region_76.RenameBasedOnDefinition()
connection_group_75.RenameBasedOnChildren()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1637, 1636, 1639, 1638]
contact_region_76.TargetLocation = selection
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1109]
contact_region_76.SourceLocation = selection
#endregion

#region Context Menu Action
connection_group_79 = connections_45.AddConnectionGroup()
#endregion

#region Context Menu Action
contact_region_80 = connection_group_79.AddContactRegion()
#endregion

#region Context Menu Action
contact_region_80.RenameBasedOnDefinition()
connection_group_79.RenameBasedOnChildren()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1109]
contact_region_80.SourceLocation = selection
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1848, 1828, 1824, 1823, 1818, 1839, 1835, 1831]
contact_region_80.TargetLocation = selection
#endregion

#region Details View Action
named_selection_84 = DataModel.GetObjectById(84)
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1401, 1402, 1404, 1407, 1408, 1365, 1370, 1371, 1366, 1367, 1438, 1445, 1444, 1440, 1439, 1129, 1130, 1134, 1128, 1133]
named_selection_84.Location = selection
#endregion

#region Context Menu Action
mesh_14 = Model.Mesh
automatic_method_86 = mesh_14.AddAutomaticMethod()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [1219, 1228, 1224, 1217]
automatic_method_86.Location = selection
#endregion

#region Context Menu Action
face_meshing_88 = mesh_14.AddFaceMeshing()
#endregion

#region Details View Action
face_meshing_88.ScopingMethod = GeometryDefineByType.Component
#endregion

#region Details View Action
mesh_14.ElementSize = Quantity(0.001, "m")
#endregion

#region Context Menu Action
mesh_14.GenerateMesh()
#endregion

#region Context Menu Action
imported_load_group_26 = DataModel.GetObjectById(26)
imported_surface_force_density_92 = imported_load_group_26.AddImportedSurfaceForceDensity()
#endregion

#region Context Menu Action
imported_load_id_list = [92]
with Transaction(True):
    for imported_load_id in imported_load_id_list:
        imported_load = DataModel.GetObjectById(imported_load_id)
        imported_load.ImportLoad()
#endregion

#region Details View Action
ansys_analysis_settings_24 = DataModel.GetObjectById(24)
ansys_analysis_settings_24.RangeMaximum = Quantity(50, "Hz")
#endregion

#region Details View Action
ansys_analysis_settings_24 = DataModel.GetObjectById(24)
ansys_analysis_settings_24.ConstantDampingRatio = 0.06
#endregion