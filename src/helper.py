
import time


# Compare two strings of equal length and return their hamming distanceß

def hamming(signal_a, signal_b):

    if (signal_a == None or signal_b == None) or (len(signal_a) == 0 or len(signal_b) == 0):
        raise Exception("Strings can not be empty")


    if len(signal_a) != len(signal_b):
        raise Exception("Signals strings must be equal length")

    hamming_distance = 0
    for i, j in zip(signal_a, signal_b): 
        if i != j:
            hamming_distance += 1 

    return hamming_distance 
        



# Given the location of the window with the minimum hamming distance, visualize the window next to the known intruder pattern

def visualize_intruder(radar_signal, radar_signal_dimensions, tokenized_intruder_signal, min_hamming_start_index): 


    row_interval = 0

    for i in range(0, len(tokenized_intruder_signal)):

        start_index = min_hamming_start_index + row_interval
        end_index = start_index + len(tokenized_intruder_signal[0])

        comparison_string = radar_signal[start_index:end_index]

        row_interval += int(radar_signal_dimensions[1]) + 1

        print(tokenized_intruder_signal[i], comparison_string)