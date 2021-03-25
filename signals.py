

class Signal:

    def __init__(self, signal):

        if len(signal) == 0 or signal == None:
            raise Exception("Signal string can not be empty")
        else:
            self.signal = signal

    
    def get_signal_dimensions(self):

        rows = 0 

        for i in self.signal:
            if ord(i) == 10: 
                rows += 1

        columns = (len(self.signal)-rows)/rows            

        return (int(rows), int(columns))


    def __str__(self):
        return self.signal



class IntruderSignal(Signal):

    def __init__(self, signal):

        super(IntruderSignal, self).__init__(signal)


    def tokenize_signal(self): 

        dimensions = self.get_signal_dimensions()

        rows = []
        
        for i in range(0, dimensions[0] * dimensions[1], dimensions[1] + 1):
            row = self.signal[i:i+dimensions[1]]
            rows.append(row)

        return rows
        


class RadarSignal(Signal):

    def __init__(self, signal):

        super(RadarSignal, self).__init__(signal)




