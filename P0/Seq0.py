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

def create_zip_list():

    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
    list_number = []
    for l in list_genes:
        list_number.append(len(seq_read_fasta(FOLDER+l+".txt")))
    zip_list = list(zip(list_genes,list_number))
    print(zip_list)
    return zip_list
