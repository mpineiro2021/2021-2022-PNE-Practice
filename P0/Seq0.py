def seq_ping():
    print("Ok")
def valid_filename():
    exit = False
    FOLDER = "./sequences/"
    while not exit:
        filename = input("Which file do you want to open: ")
        filename = FOLDER + filename

        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File doesn't exist")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    sequence = ""
    for line in body:
        sequence += line
    return sequence



def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)
    '''for b in seq:
        if b == base:
            total += 1
    return total'''

def seq_count():
    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
    dict_list = []
    for l in list_genes:
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER + l + ".txt")).count(keys)
        dict_list.append(d)
    return dict_list,list_genes

def seq_reverse():
    FOLDER = "./sequences/"
    frag = (seq_read_fasta(FOLDER +"U5.txt"))
    rev = (seq_read_fasta(FOLDER + "U5.txt"))[::-1]
    return frag[:20],rev[:20]

def seq_complement():
    d = {"A": "T", "C": "G", "G": "C", "T": "A"}
    FOLDER = "./sequences/"
    sequence = (seq_read_fasta(FOLDER +"U5.txt"))[:20]
    bases = list(sequence)
    bases = [d[base] for base in bases]
    return sequence, ''.join(bases)

def max_V(dict_list):
    value_list= []
    i = 0
    while i < len(dict_list):
        for d in dict_list[i]:
            max_key = max(d, key=d.get)
        value_list.append(max_key)
        i += 1
    return value_list












