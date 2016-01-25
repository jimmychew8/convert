# Converts amongst musical frequency, midi values, and note values.

import sys
import math
from decimal import *


class Convert(object):


	def midi(self, frequency):
		"""Given frequency in hertz returns midi value."""


		return 12 * math.log(frequency / 440, 2) + 69

	def freq(self, midi):
		"""Given midi value returns frequency."""


		return (math.pow(2, (midi - 69) / 12)) * 440

	def midi_note(self, midi):
		"""Given midi value returns note name and octave (ie. A5)."""


		return note[(midi % 12 + 1)]

	def freq_note(self, frequency):
		"""Given frequency returns tuple:
		(note name, quartertone inflection, octave).
		"""
		quartertone = ''

		midi = 12 * math.log(Decimal(frequency) / Decimal(440), 2) + 69

		# The decimal places of the midi value.
		decimal = (str(midi).split('.')[1])[0:3]
		decimal = int(decimal)

		if decimal == 0:

			quartertone = '_'

		if decimal > 0 and decimal < 500:

			quartertone = 'quartertone sharp'

		if decimal > 500 and decimal < 1000:

			quartertone = '3 quartertones sharp'


		count = 0

		for i in range(int(midi)):

			if i % 12 == 0:

				count += 1


		return note[int((midi % 12 + 1))], quartertone, count - 1


if __name__ == '__main__':

	note = {
		1 : 'C',
		2 : 'C#',
		3 : 'D',
		4 : 'D#',
		5 : 'E',
		6 : 'F',
		7 : 'F#',
		8 : 'G',
		9 : 'G#',
		10 : 'A',
		11 : 'A#',
		12 : 'B'
		}

	conversion = Convert()

	print conversion.freq_note(1000)
	print conversion.midi(880)
	print conversion.freq(81)
	print conversion.midi_note(81)
