#!/usr/bin/python3
"""The module that tests file: state.py
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class that tests state.py"""

    def __init__(self, *args, **kwargs):
        """The constructor for the test_state class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """more testing of the state name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
