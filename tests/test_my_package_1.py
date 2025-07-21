import unittest
from my_package.main import Calculator, main

class TestCalculator(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.calc = Calculator()

    async def test_add(self):
        result = await self(calc).add(2.0, 3.0)
        assert math.isclose(result, 5.0)

    async def test_subtract(self):
        result = await self(calc).subtract(5.0, 3.0)
        assert math.isclose(result, 2.0)

    async def test_multiply(self):
        result = await self(calc).multiply(4.0, 5.0)
        assert math.isclose(result, 20.0)

    async def test_divide_positive(self):
        result = await self(calc).divide(6.0, 3.0)
        assert math.isclose(result, 2.0)

    async def test_divide_negative(self):
        with self.assertRaises(ZeroDivisionError):
            await self(calc).divide(-6.0, 0)

    async def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            await self(calc).divide(6.0, 0)

    async def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            await self(calc).add("a", "b")

    async def test_main(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            main()
        except SystemExit as e:
            assert e.code == 0
        finally:
            output = captured_output.getvalue().strip()
            self.assertIn("Simple Calculator", output)

if __name__ == "__main__":
    unittest.main()