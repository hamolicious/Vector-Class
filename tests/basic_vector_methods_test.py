from vector import Vector

def test__to_vector_list():
	v = Vector([255, 5, 0, 0, 1])
	assert v.as_list_int() == [255, 5, 0, 0, 1]

def test__to_vector_vector():
	v = Vector(Vector([255, 5, 0, 0, 1]))
	assert v.as_list_int() == [255, 5, 0, 0, 1]

def test_as_list_float():
	v = Vector([255])
	assert v.as_list_int() == [255.0]

def test_as_list_int():
	v = Vector(Vector([25.43]))
	assert v.as_list_int() == [25]

def test_copy():
	v = Vector([34, 212, 657, 0])
	assert v.copy().as_list_float() == v.as_list_float()

def test_set():
	v = Vector([34, 212, 657, 0])
	v.set([10, 3, 5])
	assert v.as_list_int() == [10, 3, 5]


