import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class TexasSegment9(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Incident Date", "length": 8},
		{"name": "Victim Sequence Number", "length": 3},
		{"name": "Offender Sequence Number", "length": 2},
		{"name": "Offense Penal Code 21.02", "length": 1},
		{"name": "Offense Penal Code 21.11(a)(1)", "length": 1},
		{"name": "Offense Penal Code 21.11(a)(2)", "length": 1},
		{"name": "Offense Penal Code 22.011", "length": 1},
		{"name": "Offense Penal Code 22.021", "length": 1},
		{"name": "Offense Penal Code 43.25", "length": 1},
		{"name": "Arrest Transaction Number (ATN)", "length": 12},
		{"name": "Arrest Sequence Number", "length": 2},
		{"name": "Victim Age", "length": 2},
		{"name": "Victim Sex", "length": 1},
		{"name": "Victim Race", "length": 1},
		{"name": "Victim Ethnicity", "length": 1},
		{"name": "Offender Age", "length": 2},
		{"name": "Offender Sex", "length": 1},
		{"name": "Offender Race", "length": 1},
		{"name": "Offender Ethnicity", "length": 1},
		{"name": "Offense Relationship (Victim to Offender)", "length": 2},
		[3, {"name": "Offense Weapon", "length": 1}],
		{"name": "Offense Injury", "length": 1},
		{"name": "Incident Hour", "length": 2},
		{"name": "Offense Location", "length": 2},
		{"name": "Offender Under the Influence of", "length": 2},
	]

	def getSegmentName(self):
		return "Texas Segment 9"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING