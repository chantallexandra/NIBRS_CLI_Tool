import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalGroupBSegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Arrest Transaction Number", "length": 12},
		{"name": "Arrestee Sequence Number", "length": 2},
		{"name": "Arrest Date", "length": 8},
		{"name": "Type of Arrest", "length": 1},
		{"name": "UCR Arrest Offense Code", "length": 3},
		[2, 
			{"name": "Arrestee Was Armed With", "length": 2},
			{"name": "Automatic Weapon Indicator", "length": 1}
		],
		{"name": "Age of Arrestee", "length": 4},
		{"name": "Sex of Arrestee", "length": 1},
		{"name": "Race of Arrestee", "length": 1},
		{"name": "Ethnicity of Arrestee", "length": 1},
		{"name": "Resident Status of Arrestee", "length": 1},
		{"name": "Disposition of Arrestee Under 18", "length": 1},
		{"name": "Federal Judicial District Code (Federal Reporting Only)", "length": 3}
	]

	def getSegmentName(self):
		return "Group B Arrest Report Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING