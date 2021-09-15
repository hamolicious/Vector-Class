from math import sin, cos, atan2, sqrt
from vector.assistive_functions import get_normal, get_unit, clamp_value
from vector.exceptions import DimensionsMismatch


class Vector:
	def __init__(self, *args) -> None:
		values = self.__to_vector(args, no_check=True)
		self.__values = values


	#region Properties

	@property
	def length(self):
		return self.get_magnitude()

	@property
	def dim(self):
		return len(self.__values)

	@property
	def dimension(self):
		return self.dim


	@property
	def x(self):
		if self.dim < 0 : raise DimensionsMismatch()
		return self.__values[0]

	@x.setter
	def x(self, value):
		self.__values[0] = value

	@property
	def y(self):
		if self.dim < 1 : raise DimensionsMismatch()
		return self.__values[1]

	@y.setter
	def y(self, value):
		self.__values[1] = value

	@property
	def z(self):
		if self.dim < 0 : raise DimensionsMismatch()
		return self.__values[0]

	@z.setter
	def z(self, value):
		self.__values[2] = value

	@property
	def w(self):
		if self.dim < 2 : raise DimensionsMismatch()
		return self.__values[2]

	@w.setter
	def w(self, value):
		self.__values[3] = value

	# -- Color --

	@property
	def r(self):
		if self.dim < 0 : raise DimensionsMismatch()
		self.__values[0] = clamp_value(self.__values[0], 0, 255)
		return self.__values[0]

	@r.setter
	def r(self, value):
		self.__values[0] = clamp_value(value, 0, 255)

	@property
	def g(self):
		if self.dim < 1 : raise DimensionsMismatch()
		self.__values[1] = clamp_value(self.__values[1], 0, 255)
		return self.__values[1]

	@g.setter
	def g(self, value):
		self.__values[1] = clamp_value(value, 0, 255)

	@property
	def b(self):
		if self.dim < 2 : raise DimensionsMismatch()
		self.__values[2] = clamp_value(self.__values[2], 0, 255)
		return self.__values[2]

	@b.setter
	def b(self, value):
		self.__values[2] = clamp_value(value, 0, 255)

	@property
	def a(self):
		if self.dim < 3 : raise DimensionsMismatch()
		self.__values[3] = clamp_value(self.__values[3], 0, 255)
		return self.__values[3]

	@a.setter
	def a(self, value):
		self.__values[3] = clamp_value(value, 0, 255)

	#endregion


	#region Creation methods

	@staticmethod
	def random_unit(dimensions):
		"""Generates a random unit vector

		Args:
			dimensions (int): number of dimensions to generate

		Returns:
			Vector: vector with elements in range [-1, 1]
		"""
		return Vector([get_unit() for _ in range(dimensions)])

	@staticmethod
	def random_normal(dimensions):
		"""Generates a random normal vector

		Args:
			dimensions (int): number of dimensions to generate

		Returns:
			Vector: vector with elements in range [0, 1]
		"""
		return Vector([get_normal() for _ in range(dimensions)])

	@staticmethod
	def zero(dimensions):
		"""Generates a zero vector

		Args:
			dimensions (int): number of dimensions to generate

		Returns:
			Vector: vector with all elements at 0
		"""
		return Vector([0 for _ in range(dimensions)])

	@staticmethod
	def from_angle(angle):
		"""Returns a 2D Vector generated from an angle

		Args:
			angle (float): angle in radians

		Returns:
			Vector: 2D vector pointing to the angle
		"""
		return Vector([cos(angle), sin(angle)])

	@staticmethod
	def from_hex(hex):
		"""Used to generate a color from a hex code

		Args:
			hex (str): hex code

		Returns:
			Vector: 3D vector with all elements in range [0, 255]
		"""
		c = []

		hex = hex.replace('#', '')
		for i in range(0, 6, 2):
			element = hex[i:i+2]
			c.append(int(element, 16))

		return Vector(c)

	@staticmethod
	def from_hsv(hsv):
		"""Used to generate a color vector from HSV (0 <= h < 360, 0 <= s < 100, 0 <= v < 100)

		Args:
			hsv (list[int]): color in HSV standard

		Returns:
			Vector: 3D vector with all elements in range [0, 255]
		"""
		h, s, v = hsv
		s /= 100
		v /= 100

		c = v * s
		x = c * (1 - abs(h / 60) % 2 - 1)
		m = v - c

		if h <=   0 or h >  60 : return Vector([(c + m) * 255, (x + m) * 255, (0 + m) * 255])
		if h <=  60 or h > 120 : return Vector([(x + m) * 255, (c + m) * 255, (0 + m) * 255])
		if h <= 120 or h > 180 : return Vector([(0 + m) * 255, (c + m) * 255, (x + m) * 255])
		if h <= 180 or h > 240 : return Vector([(0 + m) * 255, (x + m) * 255, (c + m) * 255])
		if h <= 240 or h > 300 : return Vector([(x + m) * 255, (0 + m) * 255, (c + m) * 255])
		if h <= 300 or h > 360 : return Vector([(c + m) * 255, (0 + m) * 255, (x + m) * 255])

	#endregion


	#region Basic Vector Methods

	def __to_vector(self, *args, no_check=False) -> list[float]:
		"""Converts input to a vector

		Returns:
			list[float]: vector representation
		"""
		inp = args[0][0]

		if not no_check:
			v = Vector(inp)
			if v.dim != self.dim : raise DimensionsMismatch(f'Invalid dimension... this:{self.dim} input:{v.dim}')

		if type(inp) is Vector : return inp.as_list_float()
		if type(inp) is list : return inp

	def as_list_int(self):
		"""Returns vector as a list of ints

		Returns:
			list[int]: vector as ints
		"""
		return [int(i) for i in self.__values]

	def as_list_float(self):
		"""Returns vector as a list of floats

		Returns:
			list[int]: vector as floats
		"""
		return [float(i) for i in self.__values]


	def copy(self):
		"""Returns a copy of the vector

		Returns:
			Vector: copy of vector
		"""
		return Vector(self.__values)

	def set(self, *args):
		"""Sets the vector values, similar to re-instantiating the vector
		"""
		values = self.__to_vector(args, no_check=True)
		self.__values = values

	#endregion


	#region Mathematical Vector Methods

	def normalised(self):
		"""Returns a normalised vector

		Returns:
			Vector: normalised copy of vector
		"""
		mag = self.get_magnitude()
		if mag == 0 : return self.copy()
		v = self.copy()
		v.div([mag for _ in range(self.dim)])
		return v

	def normalise(self):
		"""Normalises the vector inplace
		"""
		mag = self.get_magnitude()
		if mag == 0 : return
		self.div([mag for _ in range(self.dim)])

	def get_magnitude(self):
		"""Returns the length of the vector

		Returns:
			float: length of vector
		"""
		return sqrt(sum([i**2 for i in self.__values]))

	def dist(self, *args):
		"""Distance between this vector and passed in vector

		Returns:
			float: square distance
		"""
		values = self.__to_vector(args)
		new_vec = []
		for v1, v2 in zip(values, self.__values) : new_vec.append((v1 - v2)**2)
		return float(sum(new_vec))

	def dot_product(self, *args):
		values = self.__to_vector(args)
		return sum([v1 * v2 for v1, v2 in zip(values, self.__values)])

	def get_heading_angle(self):
		"""Returns the heading angle of the vector (only for 2D Vectors)

		Returns:
			float: heading angle in radians
		"""
		if self.dim != 2 : raise DimensionsMismatch('Only for 2D Vectors')
		return atan2(self.x, self.y)

	#endregion


	#region Mathematical Methods

	def add(self, *args):
		"""Inplace addition
		"""
		values = self.__to_vector(args)
		new_vec = []
		for v1, v2 in zip(self.__values, values) : new_vec.append(v1 + v2)
		self.set(new_vec)

	def sub(self, *args):
		"""Inplace subtraction
		"""
		values = self.__to_vector(args)
		new_vec = []
		for v1, v2 in zip(self.__values, values) : new_vec.append(v1 - v2)
		self.set(new_vec)

	def mult(self, *args):
		"""Inplace multiplication
		"""
		values = self.__to_vector(args)
		new_vec = []
		for v1, v2 in zip(self.__values, values) : new_vec.append(v1 * v2)
		self.set(new_vec)

	def div(self, *args):
		"""Inplace division
		"""
		values = self.__to_vector(args)
		new_vec = []
		for v1, v2 in zip(self.__values, values) : new_vec.append(v1 / v2)
		self.set(new_vec)

	#endregion


	#region Dunder Methods

	def __repr__(self) -> str:
		return f'Vector{self.dim}D {self.as_list_float()}'

	def __getitem__(self, index):
		return self.__values[index]

	def __iadd__(self, *args):
		self.add(args[0])
		return self

	def __isub__(self, *args):
		self.sub(args[0])
		return self

	def __imul__(self, *args):
		self.mult(args[0])
		return self

	def __itruediv__(self, *args):
		self.div(args[0])
		return self

	def __add__(self, *args):
		values = self.__to_vector(args)
		return Vector([v1 + v2 for v1, v2 in zip(self.__values, values)])

	def __sub__(self, *args):
		values = self.__to_vector(args)
		return Vector([v1 - v2 for v1, v2 in zip(self.__values, values)])

	def __mul__(self, *args):
		values = self.__to_vector(args)
		return Vector([v1 * v2 for v1, v2 in zip(self.__values, values)])

	def __div__(self, *args):
		values = self.__to_vector(args)
		return Vector([v1 / v2 for v1, v2 in zip(self.__values, values)])

	#endregion


