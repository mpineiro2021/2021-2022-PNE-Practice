from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("----| Exercise 6 |------")
print("Sequence 1: (length:", str(s1.len())+")",s1)
print("Bases:",s1.count_base())
print("Sequence 2: (length:", str(s2.len())+")", s2)
print("Bases:",s2.count_base())
print("Sequence 2: (length:", str(s3.len())+")", s3)
print("Bases:",s3.count_base())