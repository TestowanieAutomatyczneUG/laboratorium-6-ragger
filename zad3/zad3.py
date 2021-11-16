class ChristmasSong:
	christmasSong=[
		lines for lines in [
			line.strip() for line in """
				On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
				On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
				On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
			""".split("\n")
		] if lines
	]

	def getVerse(self, i):
		if i < 0:
			raise IndexError
		if i > len(self.christmasSong):
			raise IndexError
		if not isinstance(i, int):
			raise ValueError
		return self.christmasSong[i]

	def getVerses(self, startAt=None, endAt=None):
		startAt = 0 if startAt is None else startAt
		endAt = len(self.christmasSong) if endAt is None else endAt
		if startAt < 0 or endAt < 0:
			raise IndexError
		if startAt > len(self.christmasSong) or endAt > len(self.christmasSong):
			raise IndexError
		if endAt < startAt:
			raise ValueError
		return self.christmasSong[startAt:endAt]

	def getAllVerses(self):
		return self.christmasSong