class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):#no se retorna nada en la init function

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases =="NULL":
            print("NULL Seq created")
        elif not self.validate_sequence():
            self.strbases = "Error"
            print("INVALID Seq!")
        else:
            print("New sequence created!")

    @staticmethod
    def validate_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


    def validate_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases
    def len(self):
        #len_bases = []
        if self.validate_sequence():
            return len(self.strbases)

            #len_bases.append(len(self.strbases))
        else:
            return 0
            #len_bases.append(0)
        #return len_bases
    def count_base(self):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        #bases_list = ["A","C","G","T"]
        #number_list = []
        if self.validate_sequence():
            for s in self.strbases:
                if s == "A":
                    count_a += 1
                elif s == "C":
                    count_c += 1
                elif s == "G":
                    count_g += 1
                elif s == "T":
                    count_t += 1
        else:
            count_a = 0
            count_c = 0
            count_g = 0
            count_t = 0
        return count_a, count_c, count_g, count_t

    def count(self):
        d = {"A": 0,"C": 0,"G": 0,"T": 0}
        if self.strbases == "NULL" or self.strbases == "Error":
            return d
        else:
            for keys in d.keys():
                d[keys] = self.strbases.count(keys)
            return d
    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "Error":
            rev = self.strbases
            return rev
        else:
            rev = self.strbases[::-1]
            return rev



