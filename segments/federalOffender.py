import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalOffenderSegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Offender Sequence Number", "length": 2},
		{"name": "Age of Offender", "length": 4},
		{"name": "Sex of Offender", "length": 1},
		{"name": "Race of Offender", "length": 1},
		{"name": "Ethnicity of Offender", "length": 1}
	]

	def getSegmentName(self):
		return "Offender Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING