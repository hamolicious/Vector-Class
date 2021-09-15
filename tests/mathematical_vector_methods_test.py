from vector import Vector


def test_normalised():
	v = Vector([5, 324, 44])
	vnorm = v.normalised()

	assert vnorm.as_list_float() == [0.015289947922006207, 0.9907886253460023, 0.13455154171365463]

def test_normalise():
	v = Vector([5, 324, 44])
	v.normalise()
	assert v.as_list_float() == [0.015289947922006207, 0.9907886253460023, 0.13455154171365463]

def test_get_magnitude():
	v = Vector([5, 324, 44])
	assert v.get_magnitude() == 327.0122321871156

def test_dist():
	v1 = Vector([7,4,3])
	v2 = Vector([17,6,2])

	assert round(v1.dist(v2), 3) == round(10.246951**2, 3)

def test_dot_product():
	v1 = Vector([15, 75, 93])
	v2 = Vector([9, 31, 52])

	assert v1.dot_product(v2) == 7296

def test_get_heading_angle():
	v = Vector([10, 5])
	assert round(v.get_heading_angle(), 5) == round(1.107148717794, 5)







