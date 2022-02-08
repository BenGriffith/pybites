from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_
def test_fizzbuzz():
    assert fizzbuzz(15) == "Fizz Buzz"
    assert fizzbuzz(30) == "Fizz Buzz"

def test_fizz():
    assert fizzbuzz(9) == "Fizz"

def test_buzz():
    assert fizzbuzz(25) == "Buzz"

def test_number():
    assert fizzbuzz(11) == 11