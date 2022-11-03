# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 18:22:51  10月 11, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("CeShi")
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
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [47,46],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [59,58],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [70,69],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Mag_3,Mag_0,Mag_1,Mag_2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [78,79],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [44,45],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [56,57],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [67,68],
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
			"Vertices:="		, [612,611,592,593,591,590,571,572,570,569,550,551,549,548,529,530,528,527,508,509,507,506,487,488,486,485,466,467,465,464,446,445,444,443,424,425,423,422,403,404,402,401,382,383,381,380,655,656,654,653,634,635,633,632,614,613],
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
			"Vertices:="		, [615,610,594,589,573,568,552,547,531,526,510,505,489,484,468,463,447,442,426,421,405,400,384,673,657,652,636,631],
			"Radius:="		, "0.3mm",
			"Setback:="		, "0mm"
		]
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "12.8654184441361mm",
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
oModule = oDesign.GetModule("MeshSetup")
oModule.AssignLengthOp(
	[
		"NAME:Length1",
		"RefineInside:="	, True,
		"Enabled:="		, True,
		"Objects:="		, ["Rotor1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.2mm"
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
oModule.AssignLengthOp(
	[
		"NAME:Length3",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Edges:="		, [1317,77,1345,74,1337,64,1365,63,1344,75,1316,1324,43,1352,40,1351,41,1323,55,1331,1359,52,53,1330,1358,66,1338,1366],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.1mm"
	])
oModule.AssignTrueSurfOp(
	[
		"NAME:SurfApprox1",
		"Objects:="		, ["Rotor1","Mag_0","Mag_2","Mag_1","Mag_3","Band","InnerRegion"],
		"CurvedSurfaceApproxChoice:=", "ManualSettings",
		"SurfDevChoice:="	, 2,
		"SurfDev:="		, "0.001mm",
		"NormalDevChoice:="	, 2,
		"NormalDev:="		, "3deg",
		"AspectRatioChoice:="	, 1
	])
oProject.Save()
oDesign.GenerateMesh(["Setup1"])
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Coil_0,Coil_1,Coil_2,Coil_3,Coil_4,Coil_5,Coil_6,Coil_7,Coil_8,Coil_9,Coil_10,Coil_11,Coil_12,Coil_13,CoilRe_0,CoilRe_1,CoilRe_2,CoilRe_3,CoilRe_4,CoilRe_5,CoilRe_6,CoilRe_7,CoilRe_8,CoilRe_9,CoilRe_10,CoilRe_11,CoilRe_12,CoilRe_13,Rotor,Rotor1,Band,InnerRegion,Shaft",
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
		"InitPos:="		, "-6.42857deg",
		"HasRotateLimit:="	, False,
		"NonCylindrical:="	, False,
		"Consider Mechanical Transient:=", False,
		"Angular Velocity:="	, "3000rpm"
	])
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
			"Edges:="		, [2930]
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
					"Value:="		, "1.5W"
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
					"NAME:Steel Type",
					"ExtraText:="		, "",
					"Material:="		, "steel_1008"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Pole",
			[
				"NAME:PropServers", 
				"Stator:Pole"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Embrace",
					"Value:="		, "0.867"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Pole",
			[
				"NAME:PropServers", 
				"Stator:Pole"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Offset",
					"Value:="		, "0mm"
				]
			]
		]
	])
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.EditMaterial("TDK_FB6B_20cel", 
	[
		"NAME:TDK_FB6B_20cel",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		[
			"NAME:permeability",
			"property_type:="	, "nonlinear",
			"BTypeForSingleCurve:="	, "normal",
			"HUnit:="		, "A_per_meter",
			"BUnit:="		, "tesla",
			"IsTemperatureDependent:=", False,
			[
				"NAME:BHCoordinates",
				[
					"NAME:DimUnits", 
					"", 
					""
				],
				[
					"NAME:Point", 
					-302394.391874601, 
					0
				],
				[
					"NAME:Point", 
					-151197.195937301, 
					0.19
				],
				[
					"NAME:Point", 
					0, 
					0.38
				]
			],
			[
				"NAME:Temperatures"
			]
		],
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "-302394.391874601A_per_meter",
			"DirComp1:="		, "1",
			"DirComp2:="		, "0",
			"DirComp3:="		, "0"
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Pole",
			[
				"NAME:PropServers", 
				"Stator:Pole"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Magnet Type",
					"ExtraText:="		, "",
					"Material:="		, "TDK_FB6B_20cel"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Pole",
			[
				"NAME:PropServers", 
				"Stator:Pole"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Magnet Length",
					"Value:="		, "48mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Pole",
			[
				"NAME:PropServers", 
				"Stator:Pole"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Magnet Thickness",
					"Value:="		, "2.9mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Stacking Factor",
					"Value:="		, "0.95"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Number of Slots",
					"Value:="		, "14"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Slot Type",
					"ExtraText:="		, "",
					"SlotType:="		, "2"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Outer Diameter",
					"Value:="		, "28.3mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Inner Diameter",
					"Value:="		, "6mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Length",
					"Value:="		, "40mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Steel Type",
					"ExtraText:="		, "",
					"Material:="		, "JFE_Steel_50JN1300"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Rotor",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Skew Width",
					"Value:="		, "1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Auto Design",
					"Value:="		, False
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Hs0",
					"Value:="		, "0.6mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Hs1",
					"Value:="		, "0.6mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Hs2",
					"Value:="		, "6.82mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Bs0",
					"Value:="		, "1.3mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Bs1",
					"Value:="		, "4.46mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Slot",
			[
				"NAME:PropServers", 
				"Rotor:Slot"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Bs2",
					"Value:="		, "1.36mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Winding Type",
					"ExtraText:="		, "",
					"WindingType:="		, "Lap"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Multiplex Number",
					"Value:="		, "1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Virtual Slots",
					"Value:="		, "1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Conductors per Slot",
					"Value:="		, "70"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Coil Pitch",
					"Value:="		, "3"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Number of Strands",
					"Value:="		, "1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Wire Wrap",
					"Value:="		, "0.04mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Winding",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Wire Size",
					"ExtraText:="		, "",
					"WireSizeWireDiameter:=", "0.31mm",
					"WireSizeGauge:="	, "0",
					"WireSizeWireWidth:="	, "0mm",
					"WireSizeWireThickness:=", "0mm",
					"WireSizeMixedWireRectType:=", False,
					[
						"NAME:WireSizeMixedDiameter"
					],
					[
						"NAME:WireSizeMixedWidth"
					],
					[
						"NAME:WireSizeMixedThickness"
					],
					[
						"NAME:WireSizeMixedThicknessMixedFillet"
					],
					[
						"NAME:WireSizeMixedThicknessMixedNumber"
					]
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Input Half-turn Length",
					"Value:="		, True
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Half Turn Length",
					"Value:="		, "60mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Base Inner Radius",
					"Value:="		, "10mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Tip Inner Diameter",
					"Value:="		, "5mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:End Clearance",
					"Value:="		, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Slot Liner",
					"Value:="		, "0.25mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Wedge Thickness",
					"Value:="		, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Layer Insulation",
					"Value:="		, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:End/Insulation",
			[
				"NAME:PropServers", 
				"Rotor:Winding"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Limited Fill Factor",
					"Value:="		, "0.53"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Commutator",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Commutator Diameter",
					"Value:="		, "14.85mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Commutator",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Commutator Length",
					"Value:="		, "12mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Commutator",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Commutator Insulation",
					"Value:="		, "0.4mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Brush",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Brush Width",
					"Value:="		, "3.5mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Brush",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Brush Length",
					"Value:="		, "4.5mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Brush",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Brush Pairs",
					"Value:="		, "2"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Brush",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Brush Displacement",
					"Value:="		, "0deg"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Brush",
			[
				"NAME:PropServers", 
				"Commutator"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Brush Drop",
					"Value:="		, "0.6V"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Shaft",
			[
				"NAME:PropServers", 
				"Shaft"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Magnetic Shaft",
					"Value:="		, False
				]
			]
		]
	])
oDesign.SetDesignSettings(
	[
		"NAME:Design Settings Data",
		"Steel Threshold:="	, 100,
		"Conductor Threshold:="	, 100000,
		"Excel Template Path:="	, "",
		"UDDEnabled:="		, True,
		"UDD:="			, ["Fractions 1"]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("PMDC", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"RatedOutputPower:="	, "25W",
		"RatedVoltage:="	, "13V",
		"RatedSpeed:="		, "3000rpm",
		"OperatingTemperature:=", "75cel",
		"OperationType:="	, "Motor",
		"LoadType:="		, "ConstSpeed"
	])
oProject.SaveAs("E:/Desktop/c/CeShi.aedt", True)
oDesign.Solve(["Setup1"])
oModule.CreateMaxwellDesign(0, "Setup1", "")
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
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [47,46],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [59,58],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		],
		[
			"NAME:ChamferParameters",
			"Edges:="		, [],
			"Vertices:="		, [70,69],
			"LeftDistance:="	, "0.5mm",
			"RightDistance:="	, "0.5mm",
			"ChamferType:="		, "Symmetric"
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Mag_3,Mag_0,Mag_1,Mag_2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [78,79],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [44,45],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [56,57],
			"Radius:="		, "0.6mm",
			"Setback:="		, "0mm"
		],
		[
			"NAME:FilletParameters",
			"Edges:="		, [],
			"Vertices:="		, [67,68],
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
			"Vertices:="		, [612,611,592,593,591,590,571,572,570,569,550,551,549,548,529,530,528,527,508,509,507,506,487,488,486,485,466,467,465,464,446,445,444,443,424,425,423,422,403,404,402,401,382,383,381,380,655,656,654,653,634,635,633,632,614,613],
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
			"Vertices:="		, [615,610,594,589,573,568,552,547,531,526,510,505,489,484,468,463,447,442,426,421,405,400,384,673,657,652,636,631],
			"Radius:="		, "0.3mm",
			"Setback:="		, "0mm"
		]
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "12.8654184441361mm",
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
oModule = oDesign.GetModule("MeshSetup")
oModule.AssignLengthOp(
	[
		"NAME:Length1",
		"RefineInside:="	, True,
		"Enabled:="		, True,
		"Objects:="		, ["Rotor1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "5mm"
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
		"MaxLength:="		, "5mm"
	])
oModule.AssignLengthOp(
	[
		"NAME:Length3",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Edges:="		, [1317,77,1345,74,1337,64,1365,63,1344,75,1316,1324,43,1352,40,1351,41,1323,55,1331,1359,52,53,1330,1358,66,1338,1366],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "5mm"
	])
oModule.AssignTrueSurfOp(
	[
		"NAME:SurfApprox1",
		"Objects:="		, ["Rotor1","Mag_0","Mag_2","Mag_1","Mag_3","Band","InnerRegion"],
		"CurvedSurfaceApproxChoice:=", "ManualSettings",
		"SurfDevChoice:="	, 2,
		"SurfDev:="		, "0.001mm",
		"NormalDevChoice:="	, 2,
		"NormalDev:="		, "3deg",
		"AspectRatioChoice:="	, 1
	])
oProject.Save()
oDesign.GenerateMesh(["Setup1"])
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Coil_0,Coil_1,Coil_2,Coil_3,Coil_4,Coil_5,Coil_6,Coil_7,Coil_8,Coil_9,Coil_10,Coil_11,Coil_12,Coil_13,CoilRe_0,CoilRe_1,CoilRe_2,CoilRe_3,CoilRe_4,CoilRe_5,CoilRe_6,CoilRe_7,CoilRe_8,CoilRe_9,CoilRe_10,CoilRe_11,CoilRe_12,CoilRe_13,Rotor,Rotor1,Band,InnerRegion,Shaft",
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
		"InitPos:="		, "-6.42857deg",
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
			"Edges:="		, [2930]
		]
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
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
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Circle2"
	])
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
oProject.Save()
