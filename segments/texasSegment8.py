import sys
sys.path.append("../NIBRS_CLI_Tool/segments")
from segments.segment import Segment

class TexasSegment8(Segment):
	
	DATA_ELEMENT_ORDERING = [{"name": "Segment Length", "length": 4}, 
		{"name": "Segment Level", "length": 1}, 
		{"name": "Segment Action Type", "length": 1}, 
		{"name": "Month of Submission", "length": 2},
		{"name": "Year of Submission", "length": 4},
		{"name": "City Indicator", "length": 4},
		{"name": "ORI", "length": 9},
		{"name": "Incident Number", "length": 12},
		{"name": "Incident Date", "length": 8},
		{"name": "Family Violence Indicator", "length": 1},
		[17, 
			{"name": "Suspected Drug Type", "length": 1},
			{"name": "Estimated Drug Quantity", "length": 9},
			{"name": "Estimated Drug Quantity Fraction", "length": 1},
			{"name": "Type Drug Measurement", "length": 3},
		],
		{"name": "Type Marijuana Fields and Gardens", "length": 1},
		{"name": "Marijuana Items", "length": 1},
		{"name": "Number of Meth Labs", "length": 1},
		{"name": "Number of Amphetamine Labs", "length": 1},
		{"name": "Number of P2P Labs", "length": 1},
		{"name": "Number of PCP Labs", "length": 1},
		{"name": "Number of Crack Labs", "length": 1},
		{"name": "Number of Other Controlled Substance Labs", "length": 1},
		[6,
			{"name": "Quantity of Precursor Chemical Seized", "length": 7},
			{"name": "Type Measurement for Precursor Chemical", "length": 2},
		]
	]

	def getSegmentName(self):
		return "Texas Segment 8"

	def getDataElements(self):
		return self.DATA_ELEMENT_ORDERING