from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("----| Exercise 4 |------")
print("Sequence 1: (length:", str(s1.len())+")",s1)
print("Sequence 2: (length:", str(s2.len())+")", s2)
print("Sequence 2: (length:", str(s3.len())+")", s3)