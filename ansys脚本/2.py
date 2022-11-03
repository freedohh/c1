# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 19:53:48  10月 10, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("22")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Chamfer(
	[
		"NAME:Selections",
		"Selections:="		, "Mag_3,Mag_0,Mag_1,Mag_2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [80,81],
			"LeftDistance:="	, "0.6mm",
			"RightDistance:="	, "0.6mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [47,46],
			"LeftDistance:="	, "0.6mm",
			"RightDistance:="	, "0.6mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [59,58],
			"LeftDistance:="	, "0.6mm",
			"RightDistance:="	, "0.6mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [70,69],
			"LeftDistance:="	, "0.6mm",
			"RightDistance:="	, "0.6mm",
			"ChamferType:="		, "Symmetric"
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Mag_2,Mag_1,Mag_0,Mag_3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [67,68],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [57,56],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [45,44],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [79,78],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Rotor",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [380,381,361,362,359,360,341,340,339,338,572,571,569,570,550,551,549,548,529,530,528,527,508,509,507,506,487,488,486,485,466,467,465,464,445,446,444,443,424,425,403,422,423,404,402,401,382,383],
			"Radius:="		, "0.2mm",
			"Setback:="		, "0mm"
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Rotor",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [442,447,426,421,405,400,384,379,363,358,342,589,573,568,552,547,531,526,510,489,484,468,463],
			"Radius:="		, "0.3mm",
			"Setback:="		, "0mm"
		]
	])
oModule = oDesign.GetModule("MeshSetup")
oModule.AssignLengthOp(
	[
		"NAME:Length1",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Edges:="		, [53,1166,1187,52,66,1174,1181,63,64,1180,77,1202,1173,1153,75,1152,1201,74,43,1195,40,1160,41,1159,1194,1188,55,1167],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.1mm"
	])
oModule.AssignLengthOp(
	[
		"NAME:Length2",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Edges:="		, [8],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.1mm"
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "12.777202686987mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Rotor"
	])
oEditor.Paste()
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Rotor1",
		"Tool Parts:="		, "Circle1"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Rotor",
		"Tool Parts:="		, "Rotor1"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, True
	])
oModule.AssignLengthOp(
	[
		"NAME:Length3",
		"RefineInside:="	, True,
		"Enabled:="		, True,
		"Objects:="		, ["Rotor1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.2mm"
	])
oProject.Save()
oDesign.GenerateMesh(["Setup1"])
oModule.AssignTrueSurfOp(
	[
		"NAME:SurfApprox1",
		"Objects:="		, ["Rotor","Rotor1","Mag_0","Mag_2","Mag_1","Mag_3","Band","InnerRegion"],
		"CurvedSurfaceApproxChoice:=", "ManualSettings",
		"SurfDevChoice:="	, 2,
		"SurfDev:="		, "0.001mm",
		"NormalDevChoice:="	, 2,
		"NormalDev:="		, "3deg",
		"AspectRatioChoice:="	, 1
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Coil_0,CoilRe_11"
	])
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Coil_0,Coil_1,Coil_2,Coil_3,Coil_4,Coil_5,Coil_6,Coil_7,Coil_8,Coil_9,Coil_10,Coil_11,CoilRe_0,CoilRe_1,CoilRe_2,CoilRe_3,CoilRe_4,CoilRe_5,CoilRe_6,CoilRe_7,CoilRe_8,CoilRe_9,CoilRe_10,CoilRe_11,Rotor,Rotor1,Band,InnerRegion,Shaft",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0.02mm",
		"TranslateVectorZ:="	, "0mm"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"Mode:="		, "Euler Angle ZYZ",
		"OriginX:="		, "0mm",
		"OriginY:="		, "0.02mm",
		"OriginZ:="		, "0mm",
		"Psi:="			, "0deg",
		"Theta:="		, "0deg",
		"Phi:="			, "0deg"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oModule = oDesign.GetModule("ModelSetup")
oModule.EditMotionSetup("MotionSetup1", 
	[
		"NAME:Data",
		"Move Type:="		, "Rotate",
		"Coordinate System:="	, "RelativeCS1",
		"Axis:="		, "Z",
		"Is Positive:="		, True,
		"InitPos:="		, "-15deg",
		"HasRotateLimit:="	, False,
		"NonCylindrical:="	, False,
		"Consider Mechanical Transient:=", False,
		"Angular Velocity:="	, "3000rpm"
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "14.59mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	],
	[
		"NAME:Attributes",
		"Name:="		, "Circle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.CreateObjectFromEdges(
	[
		"NAME:Selections",
		"Selections:="		, "Circle2",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [2546]
		]
	],
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Circle2_ObjectFromEdge1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Model",
					"Value:="		, False
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Circle2"
	])
oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("B")
oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
oModule.CalcOp("ScalarX")
oModule.AddNamedExpression("Br", "Fields")
oModule.EnterQty("B")
oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
oModule.CalcOp("ScalarY")
oModule.AddNamedExpression("Bt", "Fields")
oModule.CopyNamedExprToStack("Br")
oModule.CopyNamedExprToStack("Br")
oModule.CalcOp("*")
oModule.CopyNamedExprToStack("Bt")
oModule.CopyNamedExprToStack("Bt")
oModule.CalcOp("*")
oModule.CalcOp("-")
oModule.EnterScalar(1.25663706143592E-06)
oModule.EnterScalar(2)
oModule.CalcOp("*")
oModule.CalcOp("/")
oModule.AddNamedExpression("Fr", "Fields")
oModule.CopyNamedExprToStack("Br")
oModule.CopyNamedExprToStack("Bt")
oModule.CalcOp("*")
oModule.EnterScalar(1.25663706143592E-06)
oModule.CalcOp("/")
oModule.AddNamedExpression("Ft", "Fields")
oDesign.SetDesignSettings(
	[
		"NAME:Design Settings Data",
		"Perform Minimal validation:=", False,
		"EnabledObjects:="	, [],
		"PreserveTranSolnAfterDatasetEdit:=", False,
		"ComputeTransientInductance:=", False,
		"ComputeIncrementalMatrix:=", False,
		"PerfectConductorThreshold:=", 1E+30,
		"InsulatorThreshold:="	, 1,
		"ModelDepth:="		, "40mm",
		"UseSkewModel:="	, False,
		"EnableTranTranLinkWithSimplorer:=", False,
		"BackgroundMaterialName:=", "vacuum",
		"SolveFraction:="	, False,
		"Multiplier:="		, "fractions"
	], 
	[
		"NAME:Model Validation Settings",
		"EntityCheckLevel:="	, "Strict",
		"IgnoreUnclassifiedObjects:=", True,
		"SkipIntersectionChecks:=", False
	])
oDesign.EnableHarmonicForceCalculation(
	[
		"EnabledObjects:="	, ["Mag_0","Mag_1","Mag_2","Mag_3"],
		"ForceType:="		, 1,
		"WindowFunctionType:="	, "Rectangular",
		"NumberOfRepeatedSamples:=", "1",
		"UseNumberOfLastCycles:=", True,
		"NumberOfLastCycles:="	, 1,
		"StartTime:="		, "0s",
		"UseNumberOfCyclesForStopTime:=", True,
		"NumberOfCyclesForStopTime:=", 1,
		"StopTime:="		, "0.01s",
		"OutputFreqRangeType:="	, "Use All"
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"NonlinearSolverResidual:=", "0.0001",
		"TimeIntegrationMethod:=", "BackwardEuler",
		"SmoothBHCurve:="	, False,
		"StopTime:="		, "0.025s",
		"TimeStep:="		, "(60/3000/240) s",
		"OutputError:="		, False,
		"OutputPerObjectCoreLoss:=", False,
		"OutputPerObjectSolidLoss:=", False,
		"UseControlProgram:="	, False,
		"ControlProgramName:="	, " ",
		"ControlProgramArg:="	, " ",
		"CallCtrlProgAfterLastStep:=", False,
		"FastReachSteadyState:=", False,
		"AutoDetectSteadyState:=", False,
		"IsGeneralTransient:="	, True,
		"IsHalfPeriodicTransient:=", False,
		"SaveFieldsType:="	, "Every N Steps",
		"N Steps:="		, "1",
		"Steps From:="		, "0.005s",
		"Steps To:="		, "0.025s",
		"UseNonLinearIterNum:="	, False,
		"CacheSaveKind:="	, "Count",
		"NumberSolveSteps:="	, 1,
		"RangeStart:="		, "0s",
		"RangeEnd:="		, "0.1s",
		"UseAdaptiveTimeStep:="	, False,
		"InitialTimeStep:="	, "0.002s",
		"MinTimeStep:="		, "0.001s",
		"MaxTimeStep:="		, "0.003s",
		"TimeStepErrTolerance:=", 0.0001
	])
oProject.Save()
oDesign.Analyze("Setup1")
