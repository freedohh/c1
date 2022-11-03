from win32com import client
oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
oDesktop = oAnsoftApp.getAppDesktop()
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("c")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oModule = oDesign.GetModule("ReportSetup")

oModule.ExportToFile("Torque", r'{}/{}'.format('E:/Desktop/c', 'Torque.csv'), False)