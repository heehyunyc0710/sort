import pytest
from sort import sort

"""
Valid test cases
"""
# STANDARD
def test_standard_package():
    assert sort(50, 50, 50, 10) == "STANDARD"

# width>150 should return SPECIAL
def test_bulky_package():
    assert sort(200, 50, 50, 10) == "SPECIAL"  

# mass>20 should return SPECIAL
def test_heavy_package():
    assert sort(50, 50, 50, 25) == "SPECIAL"  

# both Bulky & Heavy should return REJECTED
def test_rejected_package():
    assert sort(200, 200, 200, 30) == "REJECTED"  

# volume is greater than or equal to 1,000,000 cm³ should return SPECIAL
def test_bulky_by_volume():
    assert sort(100, 100, 100, 10) == "SPECIAL"  



"""
Edge cases
Dimension and mass cannot be less than or equal to 0 and cannot be None.
"""
# any dimension or mass is negative -> should return error
def test_negative_length():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(-50, 50, 50, 10)
def test_negative_width():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, -50, 50, 10)
def test_negative_height():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, 50, -50, 10)
def test_negative_mass():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, 50, 50, -5)

# zero values
def test_zero_length():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(0, 50, 50, 10)
def test_zero_width():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, 0, 50, 10)
def test_zero_height():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, 50, 0, 10)
def test_zero_mass():
    with pytest.raises(ValueError, match="Dimension and mass cannot be less than or equal to 0 and cannot be None."):
        sort(50, 50, 50, 0)

"""
Dimension and mass must be a number and cannot be None.
"""
# any dimension or mass is not a number -> should return error
def test_non_numeric_length():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, "a", 10)
def test_non_numeric_width():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, "a", 50, 10)
def test_non_numeric_height():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, "a", 10)
def test_non_numeric_mass():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, 50, "a")

# any dimension or mass is None -> should return error
def test_none_length():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(None, 50, 50, 10)
def test_none_width():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, None, 50, 10)
def test_none_height():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, None, 10)
def test_none_mass():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, 50, None)
        
# any dimension or mass is empty string -> should return error
def test_empty_string_length():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort("", 50, 50, 10)
def test_empty_string_width():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, "", 50, 10)
def test_empty_string_height():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, "", 10)
def test_empty_string_mass():
    with pytest.raises(ValueError, match="Dimension and mass must be a number and cannot be None."):
        sort(50, 50, 50, "")



