# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 14:48:37  10月 10, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
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
					"Value:="		, self.parementer[0]
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
					"Value:="		, self.parementer[1]
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
					"Value:="		, self.parementer[2]
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
					"Value:="		, self.parementer[3]
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
					"Value:="		, self.parementer[4]
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
					"Value:="		, "1mm"
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
					"Value:="		, "0.96"
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
					"Value:="		, "12"
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
					"Value:="		, "0.75mm"
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
					"Value:="		, "6.63mm"
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
					"Value:="		, "5.2mm"
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
					"Value:="		, "1.64mm"
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
					"WindingType:="		, "Wave"
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
					"Value:="		, "2"
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
					"Value:="		, "2"
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
					"NAME:Virtual Slots",
					"Value:="		, "2"
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
					"NAME:Virtual Slots",
					"Value:="		, "2"
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
					"Value:="		, "2"
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
					"NAME:Multiplex Number",
					"Value:="		, "2"
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
					"NAME:Multiplex Number",
					"Value:="		, "2"
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
					"Value:="		, "82"
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
					"WireSizeWireDiameter:=", "0.31mm",
					"WireSizeGauge:="	, "0",
					"WireSizeWireWidth:="	, "0mm",
					"WireSizeWireThickness:=", "0mm",
					"WireSizeMixedWireRectType:=", True,
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
					"Value:="		, "58mm"
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
					"Value:="		, "1mm"
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
					"Value:="		, "0.1mm"
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
					"Value:="		, "0.1mm"
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
					"NAME:Commutator Type",
					"CommutatorType:="	, "PanCake"
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
					"NAME:Commutator Type",
					"CommutatorType:="	, "Cylinder"
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
					"Value:="		, "2.8mm"
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
					"Value:="		, "0.1deg"
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
					"Value:="		, True
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
