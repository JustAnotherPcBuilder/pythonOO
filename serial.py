"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.count = 0
    

    def generate(self):
        """Returns the start value, but increases every time it is called sequencially by 1"""
        value = self.start + self.count
        self.count += 1
        return value

    def reset(self):
        """Resets the value of generate to the original start value"""
        self.count = 0