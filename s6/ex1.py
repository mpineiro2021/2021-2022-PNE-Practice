class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases #attribute called strbases
        print("New sequence created!")
    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases


#Main program
#Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
# Create another object of the Class Seq
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print("Testing....")