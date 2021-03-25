import pytest
from signals import IntruderSignal, RadarSignal, Signal
from detector import Detector
from helper import hamming, visualize_intruder

# Example data
from main import known_intruder_1, known_intruder_2, radar_sample


def test_get_signal_edge_cases():

    
    # Test that empty strings cant be created for Signal class
    with pytest.raises(Exception, match="Signal string can not be empty") as exec_info:
        signal = Signal("")


    # Test that empty strings cant be created for subclasses of Signal class
    with pytest.raises(Exception, match="Signal string can not be empty") as exec_info:
        signal = RadarSignal("")

    with pytest.raises(Exception, match="Signal string can not be empty") as exec_info:
        signal = IntruderSignal("")


    # Test that the constructor does not take none as argument
    with pytest.raises(Exception, match="Signal string can not be empty") as exec_info:
        signal = RadarSignal(None)




def test_get_signal_dimensions():
    
    s_1 = Signal(known_intruder_1)


    assert s_1.get_signal_dimensions() == (8, 11)

    s_2 = Signal("----")

    assert s_2.get_signal_dimensions() == (1, 4)

    

def test_hamming_function():


    # Check that passed in strings are not empty
    with pytest.raises(Exception, match="Strings can not be empty") as exec_info:
        hamming("","")


    # Check that strings are equal length
    with pytest.raises(Exception, match="Signals strings must be equal length") as exec_info:
        hamming("--","-")


    # Test cases 

    string_1 = "-o-o-o-o-"
    string_2 = "-o-o-o-o-"

    assert hamming(string_1, string_2) == 0

    string_3 = "o-o-o-o-o"
    string_4 = "-o-o-o-o-"

    assert hamming(string_3, string_4) == 9



def test_tokenize_signal_function():

    i_1 = IntruderSignal(known_intruder_1)

    tokens = ['--o-----o--', '---o---o---', '--ooooooo--', '-oo-ooo-oo-', 'ooooooooooo', 'o-ooooooo-o', 'o-o-----o-o', '---oo-oo---']

    
    assert i_1.tokenize_signal() == tokens


def test_sliding_window_function():

    intruder_1 = IntruderSignal(known_intruder_1)
    intruder_2 = IntruderSignal(known_intruder_2)

    radar_signal = RadarSignal(radar_sample)


    
    min_hamming, min_hamming_start_index = Detector.sliding_window(radar_signal, intruder_1)

    
    assert (min_hamming, min_hamming_start_index) == (8, 1373)

    min_hamming, min_hamming_start_index = Detector.sliding_window(radar_signal, intruder_2)


    assert (min_hamming, min_hamming_start_index) == (8, 42)


    




