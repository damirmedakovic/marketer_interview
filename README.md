


### Detect invaders in ASCII dataset


The solution uses a sliding window to detect known intruders in the radar signal.

The sliding window is implemented in the "detect_intruder" function and the window has the same dimensions as the known intruder example. The window iterates through the whole radar signal in order to scan for intruders.

Intruders are detected by computing the hamming distance between the known intruder and the sliding window. 



# TODO

The solution can easily be extended for an improved intruder detection program:

- Check for "noise" in the radar signal (other symbols than "-" or "o") and handle it. An "O" (which is found in the given radar sample) could for example be substituted with an "o". 
- Better edge case handling. Currently we are mostly checking whether the radar signal inputs are empty. This could be extended to include more edge cases. 

