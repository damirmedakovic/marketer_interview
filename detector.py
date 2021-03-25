



class Detector:


    def __init__(self, radar_signal, known_intruder): 
        

    
    def detect_intruder(radar_signal, known_intruder):

        if len(radar_signal) == 0 or len(known_intruder) == 0: 
            raise Exception("Signal strings can not be empty")
            

        # Get signal dimensions

        radar_signal_dimensions = get_signal_dimensions(radar_signal)

        known_intruder_dimensions = get_signal_dimensions(known_intruder)


        # The sliding window runs until it reaches the edge 

        end_index = int(len(radar_signal) - (radar_signal_dimensions[1] * known_intruder_dimensions[0] + known_intruder_dimensions[0]) + (radar_signal_dimensions[1] - known_intruder_dimensions[1]))

        intruder_signal = tokenize_intruder_signal(known_intruder)

        window_hamming_distance = 0 

        min_hamming = float("inf")

        for i in range(0, end_index):

            row_interval = 0 
            window_hamming = 0

            for j in range(0, len(intruder_signal)):

                start_index = i + row_interval
                end_index = start_index + int(known_intruder_dimensions[1])

                comparison_string = radar_signal[start_index:end_index]

                distance = hamming(intruder_signal[j], comparison_string)

                window_hamming += distance

                row_interval += int(radar_signal_dimensions[1]) + 1
                
            
            if window_hamming < min_hamming:

                min_hamming = window_hamming
                min_hamming_start_index = i 

        
        visualize_intruder(radar_signal, radar_signal_dimensions, intruder_signal, min_hamming_start_index)

            
        return min_hamming, min_hamming_start_index