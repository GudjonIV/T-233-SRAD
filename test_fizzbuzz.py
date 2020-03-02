import fizzbuzz

def test_returns_number():
    assert fizzbuzz.fizzbuzz(2) == 2

def test_return_fizz():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"

def test_return_buzz():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"

def test_return_fizzbuzz():
    assert fizzbuzz.fizzbuzz(15) == "Fizzbuzz"