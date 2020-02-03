import pytest
import readLAcodes

def test_read_LA_codes():
    returned_value = readLAcodes.read_LA_codes()
    assert returned_value.shape == (391,4)

def test_find_code():
    returned_code = readLAcodes.find_code(readLAcodes.read_LA_codes(),"County Durham")
    assert returned_code == 'E06000047'

def test_find_LA():
    returned_LA = readLAcodes.find_LA(readLAcodes.read_LA_codes(),'E06000047')
    assert returned_LA == "County Durham"