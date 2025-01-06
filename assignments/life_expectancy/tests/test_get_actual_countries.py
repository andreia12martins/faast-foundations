"""
Test for get_countries() from the Region class
"""

from life_expectancy.region import Region


def test_get_actual_countries():
    """Test if get_countries() returns a list of actual countries."""
    expected_countries = [
        'AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE',
        'EL', 'ES', 'FI', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 
        'LU', 'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'RU', 
        'SE', 'SI', 'SK', 'SM', 'TR', 'UA', 'UK', 'XK'
    ]

    actual_countries = Region.get_countries()

    assert expected_countries == actual_countries
