from win32com import client
from pywinauto.application import Application
import time
oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
oDesktop = oAnsoftApp.getAppDesktop()
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("RMxprt", "RMxprtDesign1", "Permanent-Magnet DC Motor", "")
oDesign = oProject.SetActiveDesign("RMxprtDesign1")
oEditor = oDesign.SetActiveEditor("Machine")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Machine",
			[
				"NAME:PropServers",
				"Machine"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Number of Poles",
					"Value:="		, "4"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Machine",
			[
				"NAME:PropServers",
				"Machine"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Frictional Loss",
					"Value:="		, "2.5W"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Machine",
			[
				"NAME:PropServers",
				"Machine"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Windage Loss",
					"Value:="		, "0.5W"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Machine",
			[
				"NAME:PropServers",
				"Machine"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Reference Speed",
					"Value:="		, "3000rpm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Stator",
			[
				"NAME:PropServers",
				"Stator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Outer Diameter",
					"Value:="		, "38.2mm"
				]
			]
		]
	])

mainwindow = Application(backend='uia').connect(title="Ansys Electronics Desktop 2022 R1 - Project1 - RMxprtDesign1 - Machine - [Project1 - RMxprtDesign1 - Machine]")
dig = mainwindow.window(title="Ansys Electronics Desktop 2022 R1 - Project1 - RMxprtDesign1 - Machine - [Project1 - RMxprtDesign1 - Machine]")
dig.maximize()
time.sleep(1)
dig.restore()
too = dig.child_window(title="Window", control_type='MenuItem').wrapper_object()
too.click_input()

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Stator",
			[
				"NAME:PropServers",
				"Stator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Inner Diameter",
					"Value:="		, "29.2mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Stator",
			[
				"NAME:PropServers",
				"Stator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Length",
					"Value:="		, "68mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Stator",
			[
				"NAME:PropServers",
				"Stator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Stacking Factor",
					"Value:="		, "1"
				]
			]
		]
	])