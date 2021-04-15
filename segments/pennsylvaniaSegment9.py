import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class PennsylvaniaSegment9(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		[30,
			{"name": "Property Description", "length": 2},
			{"name": "Entry Point Code", "length": 1},
			{"name": "Value of Damage", "length": 9}
		]
	]

	def getSegmentName(self):
		return "Pennsylvania Segment 9"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING