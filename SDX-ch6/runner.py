import unittest

class Sign_Test(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(-1, sign(-3))

    def test_positive(self):
        self.assertEqual(1, sign(19))

    def test_zero(self):
        self.assertEqual(1, sign(0))

    def test_error(self):
        with self.assertRaises(NameError):
            sgn(1)

def sign(value):
    if value < 0:
        return -1
    else:
        return 1

def test_sign_negative():
    assert sign(-3) == -1

def test_sign_positive():
    assert sign(19) == 1

def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sgn(1) == 1

# [run]
def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
# [/run]

unittest.main()
