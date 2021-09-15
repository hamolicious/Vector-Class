from vector import Vector

def test_add():
	v1 = Vector([5, 3.6, 1])
	v2 = Vector([5, 6.4, 9])

	v1.add(v2)

	assert v1.as_list_float() == [10, 10, 10]

def test_sub():
	v1 = Vector([5, 3.6, 1])
	v2 = Vector([5, 6.4, 9])

	v1.sub(v2)

	assert v1.as_list_float() == [0, -2.8000000000000003, -8]

def test_mult():
	v1 = Vector([5, 1.5, 1])
	v2 = Vector([5, 2, 9])

	v1.mult(v2)

	assert v1.as_list_float() == [25, 3.0, 9.0]

def test_div():
	v1 = Vector([5, 3, 100])
	v2 = Vector([5, 2, 10])

	v1.div(v2)

	assert v1.as_list_float() == [1, 1.5, 10]

def test_iadd():
	v1 = Vector([5, 3.6, 1])
	v2 = Vector([5, 6.4, 9])

	v1 += v2

	assert v1.as_list_float() == [10, 10, 10]

def test_isub():
	v1 = Vector([5, 3.6, 1])
	v2 = Vector([5, 6.4, 9])

	v1 -= v2

	assert v1.as_list_float() == [0, -2.8000000000000003, -8]

def test_imult():
	v1 = Vector([5, 1.5, 1])
	v2 = Vector([5, 2, 9])

	v1 *= v2

	assert v1.as_list_float() == [25, 3.0, 9.0]

def test_idiv():
	v1 = Vector([5, 3, 100])
	v2 = Vector([5, 2, 10])

	v1 /= v2

	assert v1.as_list_float() == [1, 1.5, 10]

