

class Signal:

    def __init__(self, signal):

        if signal == None or len(signal) == 0:
            raise Exception("Signal string can not be empty")
        else:
            self.signal = signal




    # Gets the number of rows, columns for a given signal
    
    def get_signal_dimensions(self):

        # Check if the signal is a vector and not a multidimensional matrix. Set number of rows to 1
        if "\n" not in self.signal:
            return (1, len(self.signal))

        rows = 0 

        for i in self.signal:
            if ord(i) == 10: 
                rows += 1

        columns = (len(self.signal)-rows)/rows            

        return (int(rows), int(columns))



# The signal patterns to be spotted

class IntruderSignal(Signal):

    def __init__(self, signal):

        super(IntruderSignal, self).__init__(signal)


    # The Detector class compares known intruder signal with radar signal row by row.
    # We therefore use the tokenize_signal function to return a list of rows from the intruder signal pattern

    def tokenize_signal(self): 

        dimensions = self.get_signal_dimensions()

        rows = []
        
        for i in range(0, dimensions[0] * dimensions[1], dimensions[1] + 1):
            row = self.signal[i:i+dimensions[1]]
            rows.append(row)

        return rows
        

# The signal which potentially contains the pattern of a known intruder

class RadarSignal(Signal):

    def __init__(self, signal):

        super(RadarSignal, self).__init__(signal)




