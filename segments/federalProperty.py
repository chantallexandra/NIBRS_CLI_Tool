import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalPropertySegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Type Property Loss/Etc.", "length": 1},
		[10,
			{"name": "Property Description", "length": 2},
			{"name": "Value of Property", "length": 9},
			{"name": "Date Recovered", "length": 8},
		],
		{"name": "Number of Stolen Motor Vehicles", "length": 2},
		{"name": "Number of Recovered Motor Vehicles", "length": 2},
		[3, 
			{"name": "Suspected Drug Type", "length": 1},
			{"name": "Estimated Drug Quantity", "length": 12},
			{"name": "Type Drug Measurement", "length": 12},
		]
	]

	def getSegmentName(self):
		return "Property Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING