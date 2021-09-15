from vector import Vector

def vector_add(vector1, vector2):
	return vector1 + vector2

def vector_sub(vector1, vector2):
	return vector1 - vector2

def vector_mult(vector1, vector2):
	return vector1 * vector2

def vector_div(vector1, vector2):
	return vector1 / vector2

def vector_linear_interpolate(vector1: Vector, vector2: Vector, t=0.5):
	new_vec = []

	for i in range(vector1.dim):
		new_vec.append(vector1[i] + t * (vector2[i] - vector1[i]))

	return Vector(new_vec)
