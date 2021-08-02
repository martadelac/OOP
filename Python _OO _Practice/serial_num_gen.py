class serialGenerator:
    """Generates incrementing serial numbers"""
    
    def __init__(self,start=0):
        self.start = self.next = start

    def generate(self):
        """Returns next number"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Returns start number"""
        
        self.next = self.start