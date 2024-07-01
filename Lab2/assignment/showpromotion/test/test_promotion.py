import pytest
import assignment.showpromotion.source.print_promotion as print_promotion


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