"""Test module for region.py."""

import unittest
from life_expectancy.region import Region, string_2_enum


class TestRegion(unittest.TestCase):
    """Test cases for Region enum and related functions."""

    def test_region_enum_values(self):
        """Test that Region enum members have correct values."""
        self.assertEqual(Region.AL.value, 'AL')
        self.assertEqual(Region.UK.value, 'UK')
        self.assertEqual(Region.EU27_2020.value, 'EU27_2020')

    def test_get_countries(self):
        """Test get_countries returns correct list of two-letter country codes."""
        countries = Region.get_countries()

        # Test some expected countries are in the list
        self.assertIn('AL', countries)
        self.assertIn('UK', countries)

        # Test that non-country codes are not in the list
        self.assertNotIn('EU28', countries)
        self.assertNotIn('EA19', countries)

        # Test that all returned values are 2 characters long
        self.assertTrue(all(len(country) == 2 for country in countries))

    def test_string_2_enum_valid(self):
        """Test string_2_enum with valid region strings."""
        self.assertEqual(string_2_enum('AL'), Region.AL)
        self.assertEqual(string_2_enum('EU27_2020'), Region.EU27_2020)

    def test_string_2_enum_invalid(self):
        """Test string_2_enum with invalid region string."""
        self.assertIsNone(string_2_enum('XX'))
