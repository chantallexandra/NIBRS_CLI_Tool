import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class CaliforniaSegment8(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Zip Code", "length": 5},
		{"name": "ARRC Indicator", "length": 1},
		{"name": "Identity Theft Indicator", "length": 1},
		{"name": "Gang Activity Indicator", "length": 1},
		{"name": "Gang Type", "length": 2},
		[10,
			{"name": "UCR Offense Code", "length": 3},
			{"name": "Hate Crime Offensive Act", "length": 2}
		],
		[10,
			{"name": "UCR Offense Code for CA Offense Details", "length": 3},
			{"name": "CJIS Code", "length": 5},
			{"name": "CA Code Type", "length": 2},
			{"name": "CA Offense Code Section", "length": 25},
			{"name": "CA Offense Level", "length": 1}
		]
	]

	def getSegmentName(self):
		return "California Segment 8"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING
