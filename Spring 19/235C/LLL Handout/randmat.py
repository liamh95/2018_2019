from fractions import Fraction

class QMat:

	def __init__(self, rows):
		self.m = len(rows)
		self.n = len(rows[0])

		for row in rows:
			if len(row) != n:
				raise Exception('Each row should have the same length.')

		self.rows = rows

	def __add__(self, other):
		if (self.m != other.m) or (self.n != other.n):
			raise Exception('Dimension mismatch')
		return QMat([[self.rows[i][j] +other.rows[i][j] for j in range(n)] for i in range(m)])


	def interchange(self, i, j):
		temp = rows[i]
		rows[i] = rows[j]
		rows[j] = temp