import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class CaliforniaSegmentA(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Arrest Transaction Number ", "length": 12},
		{"name": "Arrestee Sequence Number", "length": 2},
		{"name": "UCR Offense Code for CA Offense Details", "length": 3},
		{"name": "CJIS Code", "length": 5},
		{"name": "CA Code Type", "length": 2},
		{"name": "CA Offense Code Section", "length": 25},
		{"name": "CA Offense Level", "length": 1},
		[3, {"name": "Arrestee Suspected of Using", "length": 1}],
		{"name": "Disposition of Arrestee 18 and Over", "length": 1}
	]

	def getSegmentName(self):
		return "California Segment A"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING