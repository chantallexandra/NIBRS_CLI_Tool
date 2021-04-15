import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalOffenseSegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "UCR Offense Code", "length": 3},
		{"name": "Offense Attempted/Completed", "length": 1},
		[3, {"name": "Offender Suspected of Using", "length": 1}],
		{"name": "Location Type", "length": 2},
		{"name": "Number of Premises Entered", "length": 2},
		{"name": "Method of Entry", "length": 1},
		[3, {"name": "Type Criminal Activity/Gang Information", "length": 1}],
		[3, 
			{"name": "Type Weapon/Force Involved", "length": 2},
			{"name": "Automatic Weapon Indicator", "length": 1},
		],
		[5, {"name": "Bias Motivation", "length": 2}],
	]

	def getSegmentName(self):
		return "Offense Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING