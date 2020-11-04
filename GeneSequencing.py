#!/usr/bin/python3

from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
	from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
	from PyQt4.QtCore import QLineF, QPointF
else:
	raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))

import math
import time
import random
from DynamicTable import *

# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

class GeneSequencing:

	def __init__( self ):
		pass
	
# This is the method called by the GUI.  _seq1_ and _seq2_ are two sequences to be aligned, _banded_ is a boolean that tells
# you whether you should compute a banded alignment or full alignment, and _align_length_ tells you 
# how many base pairs to use in computing the alignment

	def align( self, seq1, seq2, banded, align_length):
		self.banded = banded
		self.MaxCharactersToAlign = align_length

		sub1 = seq1[0:align_length]
		sub2 = seq2[0:align_length]

		table = DynamicTable()

		table.initTable(sub1, sub2, banded)
		alignments = table.getTraces()

###################################################################################################
# your code should replace these three statements and populate the three variables: score, alignment1 and alignment2
		score = table.getScore()
		alignment1 = '{}  DEBUG:({} chars,align_len={}{})'.format(alignments[0], len(seq1), align_length, ',BANDED' if banded else '')
		alignment2 = '{}  DEBUG:({} chars,align_len={}{})'.format(alignments[1], len(seq2), align_length, ',BANDED' if banded else '')
###################################################################################################					
		
		return {'align_cost':score, 'seqi_first100':alignment1, 'seqj_first100':alignment2}


