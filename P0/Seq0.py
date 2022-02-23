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

    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n","")
    return seq

def seq_len():

    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
    list_number = []
    for l in list_genes:
        list_number.append(len(seq_read_fasta(FOLDER+l+".txt")))

    return list_genes,list_number

def seq_count_base():
    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
    list_a = []
    list_c = []
    list_g = []
    list_t = []
    for l in list_genes:
        list_a.append((seq_read_fasta(FOLDER + l + ".txt")).count("A"))
        list_c.append((seq_read_fasta(FOLDER + l + ".txt")).count("C"))
        list_g.append((seq_read_fasta(FOLDER + l + ".txt")).count("G"))
        list_t.append((seq_read_fasta(FOLDER + l + ".txt")).count("T"))
    return list_a, list_c, list_g, list_t, list_genes

def seq_count():
    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    dict_list = []
    for l in list_genes:
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER + l + ".txt")).count(keys)
        dict_list.append(d)

        return dict_list,list_genes








