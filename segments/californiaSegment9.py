import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class CaliforniaSegment9(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Victim Sequence Number", "length": 3},
		{"name": "Senior Citizen Indicator", "length": 1},
		[10,
			{"name": "Victim Connected to UCR Offense Code", "length": 3},
			{"name": "Victim by Association Indicator", "length": 1},
			{"name": "Victim by Association Type", "length": 2},
			{"name": "Victim by Association Relation", "length": 2}
		],
		{"name": "Homicide Victim First Name", "length": 20},
		{"name": "Homicide Victim Middle Name", "length": 20},
		{"name": "Homicide Victim Last Name", "length": 25}
	]

	def getSegmentName(self):
		return "California Segment 9"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING