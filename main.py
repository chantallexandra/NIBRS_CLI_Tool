from segmentLayouts import segment_layouts 
from segments.segment import Segment 

def run():
	segment_str = input("Enter segment: ")

	printLineStructure(segment_str)
	parseSegmentLayout(segment_str)

'''
	Print text for an unrecognized segment layout
'''
def unknownSegment():
	print("\n\033[1m\033[91mUnknown Segment\033[0m")


'''
	Print the flat file with the character count underneath
'''
def printLineStructure(segment_str):
	output_str = ""
	output_counter = ""
	counter = 1

	print("\n\033[1mSegment Layout:\033[0m")

	while counter <= len(segment_str):
		output_str += "|" + (" " * (len(str(counter))))  + segment_str[counter - 1]
		output_counter += "| " + str(counter)
		counter += 1
		# Wrap line at 30 characters
		if (counter - 1) % 30 == 0:
			print()
			print("Data Elements:   " + output_str)
			print("Position Number: " + output_counter)
			output_str = ""
			output_counter = ""

	if (counter - 1) % 30 != 0:
		print()
		print("Data Elements:   " + output_str)
		print("Position Number: " + output_counter)


'''
	Print the individual data elements depending on the segment inputted
'''
def parseSegmentLayout(segment_str):
	if len(segment_str) < 5:
		unknownSegment()
		return

	segment_level = segment_str[4]
	segment = segment_layouts.get(segment_level)

	if segment == None:
		unknownSegment()
		return

	if type(segment) is list:
		segment = handleMultipleSegment(segment)

	segment_obj = segment(segment_str)

	print("\n\033[1m\033[92m" + segment_obj.getSegmentName() + "\033[0m")

	segment_obj.parseSegment()


'''
	Ask user to input state for state-specific segments
'''
def handleMultipleSegment(stateSegments):
	states = [x['state'] for x in stateSegments]

	state = input("\nEnter state (" + ", ".join(states)+"): ")
	while state not in states:
		state = input("Enter state (" + ", ".join(states)+"): ")

	return [x for x in stateSegments if x['state'] == state][0]["segment"]

