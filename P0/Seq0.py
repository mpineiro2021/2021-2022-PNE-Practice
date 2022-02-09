def seq_ping():
    print("Ok")
def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you wnat to open: ")
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File doesn't exist")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n","")
    return seq

def seq_len(seq):
'''gene = input("Choose a gene")
f= open(FOLDER+ gene+".txt")
print(f.read())'''

FOLDER = "./sequences/"
list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
number = []
for l in list_genes:
    number = number.append(len(Seq0.seq_read_fasta(FOLDER+l+".txt")))
    return number
