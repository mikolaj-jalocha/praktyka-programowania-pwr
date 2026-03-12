class AddTest(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(Add(""), 0)

    def test_with_one_parameter_parameter_is_returned(self):
        self.assertEqual(Add("3"), 3)

    def test_3_plus_2_returns_5(self):
        self.assertEqual(Add("3,2"), 5)

    def test_minus_3_plus_minus_2_returns_minus_5(self):
        self.assertEqual(Add("-3,-2"), -5)

    def test_more_than_2_args_returns_correct_result(self):
        self.assertEqual(Add("3,2,1"), 6)

    def test_incorrect_values_returns_value_error(self):
        with self.assertRaises(ValueError):
            Add("a,1")

    def test_new_line_as_separator_returns_correct_result(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_comma_and_new_line_returns_value_error(self):
        with self.assertRaises(ValueError):
            Add("a,\n")