
import time



known_intruder_1 = """--o-----o--
---o---o---
--ooooooo--
-oo-ooo-oo-
ooooooooooo
o-ooooooo-o
o-o-----o-o
---oo-oo---
""" 

known_intruder_2 = """---oo---
--oooo--
-oooooo-
oo-oo-oo
oooooooo
--o--o--
-o-oo-o-
o-o--o-o
"""

radar_sample = """----o--oo----o--ooo--ooo--o------o---oo-o----oo---o--o---------o----o------o-------------o--o--o--o-
--o-o-----oooooooo-oooooo---o---o----o------ooo-o---o--o----o------o--o---ooo-----o--oo-o------o----
--o--------oo-ooo-oo-oo-oo-----O------------ooooo-----oo----o------o---o--o--o-o-o------o----o-o-o--
-------o--oooooo--o-oo-o--o-o-----oo--o-o-oo--o-oo-oo-o--------o-----o------o-ooooo---o--o--o-------
------o---o-ooo-ooo----o-----oo-------o---oo-ooooo-o------o----o--------o-oo--ooo-oo-------------o-o
-o--o-----o-o---o-ooooo-o-------oo---o---------o-----o-oo-----------oo----ooooooo-ooo-oo------------
o-------------ooooo-o--o--o--o-------o--o-oo-oo-o-o-o----oo------------o--oooo--ooo-o----o-----o--o-
--o-------------------------oo---------oo-o-o--ooo----oo----o--o--o----o--o-o-----o-o------o-o------
-------------------o----------o------o--o------o--------o--------o--oo-o-----oo-oo---o--o---o-----oo
----------o----------o---o--------------o--o----o--o-o------------oo------o--o-o---o-----o----------
------o----o-o---o-----o-o---o-----oo-o--------o---------------------------------o-o-o--o-----------
---------------o-------o-----o-------o-------------------o-----o---------o-o-------------o-------oo-
-o--o-------------o-o-----o--o--o--oo-------------o----ooo----o-------------o----------oo----o---o-o
-o--o-------------o----oo------o--o-------o--o-----o-----o----o-----o--o----o--oo-----------o-------
-o-----oo-------o------o----o----------o--o----o-----o-----o-------o-----------o---o-o--oooooo-----o
-o--------o-----o-----o---------oo----oo---o-o---------o---o--oooo-oo--o-------o------oo--oo--o-----
------------o---------o---------o----oooo-------------oo-oo-----ooo-oo-----o-------o-oo-oooooooo---o
----------------------o------------oooooooo---o-----o-------o--oooooo-o------------o-o-ooooooo-o----
------------o------o---o---o-------oo-oo--o--o---------o--o-o-o-ooooo-o--------------oo-o----o-oo-o-
---o-o----------oo-------oo----o----oooooooo-------o----o-o-o-o-----o-o-----o----------ooo-oo--o---o
-o-o---------o-o---------------o--o--o--ooo---ooo-------o------oo-oo------------o--------o--o-o--o--
-------oo---------------------------o-oo----------o------o-o-------o-----o----o-----o-oo-o-----o---o
---o--------o-----o-------o-oo-----oo--oo-o----oo----------o--o---oo------oo----o-----o-------o-----
---o--ooo-o---------o-o----o------------o---------o----o--o-------o----o--------o----------------oo-
---o------o----------------o----o------o------o---oo-----------o-------------o----------oo---------o
--oo---------------o--o------o---o-----o--o-------------o------o-------o-----o-----o----o------o--o-
-o-------o----------o-o-o-------o-----o--o-o-----------o-oo-----------o------o---------o-----o-o----
----------o----o-------o----o--o------o------------o---o---------------oo----o-----ooo--------------
----o--------oo----o-o----o--o------ooo----o-oooo---o--o-oo--------o-oo-----o-o---o-o--o-----oo-----
------o--------o-ooooo----o---o--o-----o---------------o-o-------o-----o----------------------------
o-------oo----o--oooooo-o---o--o------oooo----------o-oo-------o---o----------o------oo-------------
-o---o----------o--oo-oo-o---o-----o-o-----------------------oo--o------o------o--------------------
-----oo-o-o-o---ooooooooo----o----o--------o--o---oo---o------------o----------o-o---o------o-o--oo-
------o------o---ooo-o---------------------------o--o---o---o----o--o-------o-----o------o----o----o
-------o----------ooo-o-----o----o---o--o-oo--o--o-o--o------o--o-oo---ooo------------------------o-
-o-------o------o-o--ooo--o---o---oo-----o----o-------------o----o-ooo-o------o--o-o------o-o-------
---oo--o---o-o---------o---o--------------o--o-----o-------o-----o--o---o-oo--------o----o----o-----
o------o----oo-o-----------oo--o---o--------o-o------o-------o-o------o-oo---------o-----oo---------
----o--o---o-o-----------o---o------------o-------o----o--o--o--o-o---------------o-----------------
-------oo--o-o-----o-----o----o-o--o----------------------o-------o------o----oo----ooo---------o---
o-----oo-------------------o--o-----o-----------o------o-------o----o-----------o----------------o--
--o---o-------o------------o--------------------o----o--o-------------oo---o---------oo--------o----
--o--------o---------o------------o------o-------o------------o-------o---o---------oooooX--X-------
------o--------------o-o-o---------o---o-------o--o-----o-------o-o----------o-----oo-ooo----------o
--o---------------o----o--oo-------------o---------o-------------------oo---------oo-o-ooo----------
-o-----------o------ooo----o----------------ooo-----o--------o--o---o-----------o-o-oooooo--------oo
-o---o-------o---o-oooo-----o-------------------o----oo-----------------o--o--------o--o------o--o--
-------o---o------oooooo--o----ooo--o--------o-------o----------------------------oo-oo-o--o--------
o--oo------o-----oo--o-oo------------oo--o------o--o-------------oo----o------------oooo-o------oo--
-----o----------ooooooooo--------------oo--------------oo-----o-----o-o--o------o----------o----o---
"""





def hamming(signal_a, signal_b):

    if len(signal_a) != len(signal_b):
        return -1 

    hamming_distance = 0
    for i, j in zip(signal_a, signal_b): 
        if i != j:
            hamming_distance += 1 

    return hamming_distance 



def get_signal_dimensions(signal):

    rows = 0 

    for i in signal:
        if ord(i) == 10: 
            rows += 1

    columns = (len(signal)-rows)/rows            

    return (rows, columns)




def tokenize_intruder_signal(intruder_signal): 

    dimensions = get_signal_dimensions(intruder_signal)

    rows = []
    
    for i in range(0, int(dimensions[0]) * (int(dimensions[1])), int(dimensions[1] + 1)):
        row = intruder_signal[i:i+int(dimensions[1])]
        rows.append(row)


    return rows
        


tokenize_intruder_signal(known_intruder_2) 


def detect_intruder(radar_signal, known_intruder):


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
            
            #if i == 1373:
            #    print(intruder_signal[j], comparison_string, distance)


        
        if window_hamming < min_hamming:

            min_hamming = window_hamming
            min_hamming_start_index = i 

    
    visualize_intruder(radar_signal, radar_signal_dimensions, intruder_signal, min_hamming_start_index)

        
    
    return min_hamming, min_hamming_start_index



def visualize_intruder(radar_signal, radar_signal_dimensions, tokenized_intruder_signal, min_hamming_start_index): 


    row_interval = 0

    for i in range(0, len(tokenized_intruder_signal)):

        start_index = min_hamming_start_index + row_interval
        end_index = start_index + len(tokenized_intruder_signal[0])

        comparison_string = radar_signal[start_index:end_index]

        row_interval += int(radar_signal_dimensions[1]) + 1

        print(tokenized_intruder_signal[i], comparison_string)



        




            
detect_intruder(radar_sample, known_intruder_1)
 





    

