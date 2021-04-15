import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class FederalAdminSegment(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Incident Date", "length": 8},
		{"name": "Report Date Indicator", "length": 1},
		{"name": "Incident Hour", "length": 2},
		{"name": "Cleared Exceptionally", "length": 1},
		{"name": "Exceptional Clearance Date", "length": 8},
		{"name": "Exceptional Clearance Offense Code-Place Holder (Deprecated)", "length": 30},
		{"name": "Cargo Theft", "length": 1},
		{"name": "Judicial District (federal and tribal agency reporting only)", "length": 3},
	]

	def getSegmentName(self):
		return "Administrative Segment"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING
