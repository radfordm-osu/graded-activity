import calculator


class TestCalculator:
    def test_add(self):
        assert 5 == calculator.addition(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

    def test_mult(self):
        assert 12 == calculator.mult(3, 4)
