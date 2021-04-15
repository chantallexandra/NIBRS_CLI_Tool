import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class PennsylvaniaSegment10(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Arrest Transaction Number", "length": 12},
		{"name": "Arrest Sequence Number", "length": 2},
		{"name": "Latitude", "length": 9},
		{"name": "Longitude", "length": 10},
		{"name": "Municipality Code", "length": 5},
		{"name": "UCR Arrest Offense Code", "length": 3},
		{"name": "PA Statute Code", "length": 14}
	]

	def getSegmentName(self):
		return "Pennsylvania Segment 10 (Level A)"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING