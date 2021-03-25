
from signals import IntruderSignal, RadarSignal
from helper import hamming, visualize_intruder



# The detector class takes a radar signal and a known intruder pattern
# The class can be extended to include several types of the detectors other than a sliding window

class Detector:

    
    def sliding_window(radar_signal, known_intruder):

        # Get intruder and radar signal dimensions

        radar_signal_dimensions = radar_signal.get_signal_dimensions()
        known_intruder_dimensions = known_intruder.get_signal_dimensions()


        # The sliding window runs until it reaches the edge 
        # The end index defines the upper left corner of the last sliding window before it reaches the bottom right edge of the radar signal

        end_index = int(len(radar_signal.signal) - (radar_signal_dimensions[1] * known_intruder_dimensions[0] + known_intruder_dimensions[0]) + (radar_signal_dimensions[1] - known_intruder_dimensions[1]))


        # Get all rows in known_intruder pattern (see tokenize_signal function)

        tokenized_intruder_signal = known_intruder.tokenize_signal()

        print(tokenized_intruder_signal)


        # We calculate the hamming distance for each sliding window and keep track of the closest match in the min_hamming variable
        window_hamming_distance = 0 
        min_hamming = float("inf")

        for i in range(0, end_index):

            
            row_interval = 0 
            window_hamming = 0


            # We compare the sliding window with the tokenized intruder pattern signal row by row
            for j in range(0, len(tokenized_intruder_signal)):

                start_index = i + row_interval
                end_index = start_index + int(known_intruder_dimensions[1])


                comparison_string = radar_signal.signal[start_index:end_index]

                distance = hamming(tokenized_intruder_signal[j], comparison_string)

                window_hamming += distance

                # Incrementing row interval by radar_signal_dimensions[1] effectively moves us to the next row in the radar signal
                # The +1 assures us that we jump over the newline character, which is present in the radar signal

                row_interval += int(radar_signal_dimensions[1]) + 1
                
            
            # Keep track of the closest match, measured by hamming distance
            if window_hamming < min_hamming:

                min_hamming = window_hamming
                min_hamming_start_index = i 

        
        
        # Visualize the closest match before returning
        visualize_intruder(radar_signal.signal, radar_signal_dimensions, tokenized_intruder_signal, min_hamming_start_index)

            
        return min_hamming, min_hamming_start_index
