import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalVictimSegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Victim Sequence Number", "length": 3},
		[10, {"name": "Victim Connected to UCR Offense Code", "length": 3}],
		{"name": "Type of Victim", "length": 1},
		{"name": "Age of Victim", "length": 4},
		{"name": "Sex of Victim", "length": 1},
		{"name": "Race of Victim", "length": 1},
		{"name": "Ethnicity of Victim", "length": 1},
		{"name": "Resident Status of Victim", "length": 1},
		[2, {"name": "Aggravated Assault/Homicide Circumstances", "length": 2}],
		{"name": "Additional Justifiable Homicide Circumstances", "length": 1},
		[5, {"name": "Type Injury", "length": 1}],
		[10, 
			{"name": "Offender Number to be Related", "length": 2},
			{"name": "Relationship of Victim to Offender", "length": 2},
		],
		{"name": "Type of Officer Activity/Circumstance", "length": 2},
		{"name": "Officer Assignment Type", "length": 1},
		{"name": "Officer–ORI Other Jurisdiction", "length": 9},
	]

	def getSegmentName(self):
		return "Victim Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING