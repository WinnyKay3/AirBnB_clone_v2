#!/usr/bin/python3
""" Test for console"""
import unittest
from io import StringIO
from console import HBNBCommand
from models.user import User
from models.place import Place
from models.state import State
from models.base_model import BaseModel
import sys

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture printed output
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.stdout

    def test_create_valid_params(self):
        # Test object creation with valid parameters
        cmd = HBNBCommand()
        cmd.do_create("User name=\"John\" age=30")
        output = sys.stdout.getvalue()
        self.assertIn("User", output)  # Check if the class name is present
        self.assertIn("name", output)  # Check if a parameter key is present
        self.assertIn("age", output)   # Check if another parameter key is present

    def test_create_invalid_params(self):
        # Test object creation with invalid parameters
        cmd = HBNBCommand()
        cmd.do_create("User name=John age=\"thirty\"")
        output = sys.stdout.getvalue()
        self.assertIn("** class name missing **", output)  # Check for error message
        self.assertNotIn("User", output)                   # Check if the class name is not present
        self.assertNotIn("name", output)                   # Check if a parameter key is not present
        self.assertNotIn("age", output)                    # Check if another parameter key is not present

    def test_create_string_param(self):
        # Test object creation with a string parameter
        cmd = HBNBCommand()
        cmd.do_create("User name=\"John Doe\"")
        user = User.all()[0]
        self.assertEqual(user.name, "John Doe")

    def test_create_float_param(self):
        # Test object creation with a float parameter
        cmd = HBNBCommand()
        cmd.do_create("Place price_by_night=199.99")
        place = Place.all()[0]
        self.assertEqual(place.price_by_night, 199.99)

    def test_create_integer_param(self):
        # Test object creation with an integer parameter
        cmd = HBNBCommand()
        cmd.do_create("State population=1000000")
        state = State.all()[0]
        self.assertEqual(state.population, 1000000)

    def test_create_escaped_quotes(self):
        # Test object creation with escaped double quotes
        cmd = HBNBCommand()
        cmd.do_create("User name=\"John \\\"Doe\\\"\"")
        user = User.all()[0]
        self.assertEqual(user.name, 'John "Doe"')

    def test_create_invalid_float(self):
        # Test object creation with an invalid float parameter
        cmd = HBNBCommand()
        cmd.do_create("Place price_by_night=invalid")
        output = sys.stdout.getvalue()
        self.assertIn("** value missing **", output)
        self.assertNotIn("Place", output)

    def test_create_empty_string(self):
        # Test object creation with an empty string parameter
        cmd = HBNBCommand()
        cmd.do_create("State name=\"\"")
        state = State.all()[0]
        self.assertEqual(state.name, "")

    def test_create_duplicate_params(self):
        # Test object creation with duplicate parameters (last one should take precedence)
        cmd = HBNBCommand()
        cmd.do_create("User name=\"John\" name=\"Doe\"")
        user = User.all()[0]
        self.assertEqual(user.name, "Doe")

    def test_create_with_underscore(self):
        # Test object creation with underscores in parameter names
        cmd = HBNBCommand()
        cmd.do_create("User first_name=\"John\" last_name=\"Doe\"")
        user = User.all()[0]
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()

