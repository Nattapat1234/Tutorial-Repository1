# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Mr.......
# Student ID:

MINIMUM = 500
MIDRANGE = 700
MAXIMUM = 1200
FREE_ICECREAM = "Free ice cream cone = "
FREE_CAKE = "Free chocolate cake = "
NO_GIFT = "Thank you and see you next time"

def print_promotion(total_cost):
    if not isinstance(total_cost, (int, float)) or total_cost < 0:
        return 'Invalid input'

    num_icecream = 0
    num_cake = 0

    while total_cost >= MAXIMUM:
        num_icecream += 1
        num_cake += 1
        total_cost -= MAXIMUM

    while total_cost >= MIDRANGE:
        num_cake += 1
        total_cost -= MIDRANGE

    while total_cost >= MINIMUM:
        num_icecream += 1
        total_cost -= MINIMUM

    if num_icecream == 0 and num_cake == 0:
        return NO_GIFT

    promotion = []
    if num_icecream > 0:
        promotion.append(FREE_ICECREAM + str(num_icecream))
    if num_cake > 0:
        promotion.append(FREE_CAKE + str(num_cake))

    return ' and '.join(promotion)
# Positive case
def test_promotion_500():
    assert print_promotion(500) == 'Free ice cream cone = 1'

def test_promotion_700():
    assert print_promotion(700) == 'Free chocolate cake = 1 and Free ice cream cone = 1'

def test_promotion_1200():
    assert print_promotion(1200) == 'Free ice cream cone = 2 and Free chocolate cake = 2'

def test_promotion_1500():
    assert print_promotion(1500) == 'Free ice cream cone = 3 and Free chocolate cake = 2'

# Negative case
def test_promotion_150():
    assert print_promotion(150) == 'Thank you and see you next time'

# Boundary condition
def test_promotion_499():
    assert print_promotion(499) == 'Thank you and see you next time'

def test_promotion_500_boundary():
    assert print_promotion(500) == 'Free ice cream cone = 1'

def test_promotion_699():
    assert print_promotion(699) == 'Free ice cream cone = 1'

def test_promotion_700_boundary():
    assert print_promotion(700) == 'Free chocolate cake = 1 and Free ice cream cone = 1'

def test_promotion_1199():
    assert print_promotion(1199) == 'Free chocolate cake = 1 and Free ice cream cone = 2'

def test_promotion_1200_boundary():
    assert print_promotion(1200) == 'Free ice cream cone = 2 and Free chocolate cake = 2'

# Error condition
def test_promotion_negative():
    assert print_promotion(-100) == 'Invalid input'

def test_promotion_non_numeric():
    assert print_promotion('abc') == 'Invalid input'
