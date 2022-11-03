# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# coding: utf-8
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("CeShi")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oModule = oDesign.GetModule("UserDefinedSolutionModule")
oModule.CreateUserDefinedSolution("FFT2D3", "SysLib", "FFT2D",
	[
		"Order of time domain:=", "98",
		"Order of space domain:=", "2",
		"Export FFT2D datatable ?:=", "No",
		"Maximum time order:="	, "0",
		"Maximum space order:="	, "0"
	], 
	[
		[
"Fields",
"FieldReport",
"Setup1 : Transient",
			[
				"Context:="		, "Circle2_ObjectFromEdge1",
				"PointCount:="		, 512
			],
			[
				"Distance:="		, ["All"],
				"Time:="		, ["All"]
			],
			[
				"Probe Component:="	, ["Fr"]
			]
		]
	], [])
