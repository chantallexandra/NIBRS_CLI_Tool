class Segment:

	def __init__(self, segment_str):
		self.segment_str = segment_str

	def parseSegment(self):
		i = 0
		for data_element in self.getDataElements():
			# If the data element is a list it will be formated: [number_of_repetitions, {data element 1}, {data element 2}, ...]
			if type(data_element) is list:
				repetitions = data_element[0]
				# Count of the number of repetitions
				count = 0
				while count < repetitions:
					print("--------")
					for element in data_element[1:]:
						inc = element["length"] * count
						print("\033[1m" + element["name"] + "(" + str(count + 1) + ")" + ":\033[0m " + self.segment_str[i:i+element["length"]])
						i += element["length"]
					count += 1 
				print("--------")
				continue
			# Otherwise it is a single data element formated like {name: data_element_name, length: number_of_characters_in_data_element}
			else:
				print("\033[1m" + data_element["name"] + ":\033[0m " + self.segment_str[i:i+data_element["length"]])
				i += data_element["length"]

	def getSegmentName(self):	
		raise NotImplementedError("Segment should be overriden with getSegmentName method")

	def getDataElements(self):
		raise NotImplementedError("Segment should be overriden with getDataElements method")