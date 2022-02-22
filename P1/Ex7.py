from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("----| Exercise 7 |------")
print("Sequence 1: (length:", str(s1.len())+")",s1)
print("Bases:",s1.count())
print("rev:",s1.reverse())
print("Sequence 2: (length:", str(s2.len())+")", s2)
print("Bases:",s2.count())
print("rev:",s2.reverse())
print("Sequence 2: (length:", str(s3.len())+")", s3)
print("Bases:",s3.count())
print("rev:",s3.reverse())