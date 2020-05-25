import re
fasta = {}
import argparse
import os

parser=argparse.ArgumentParser(prog='count freq',usage='%(prog)s [opthions] [value]',description='count freq !')
parser.add_argument('-INPUT','--input',help='input',metavar='')
argv=vars(parser.parse_args())



with open(argv['input']) as file:
    sequence = ""
    for line in file:
        if line.startswith(">"):
            name = line[1:].rstrip()
            fasta[name] = ''
            continue
        fasta[name] += line.rstrip().upper()

def complement(s):
    basecomplement = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G",
	"N":"N",
          }
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

for seqname,seq in fasta.items():
    for i in range(len(seq)):
        for j in range(0,100):
            selectseq = seq[i:i+j]
            reverse_complement_seq = complement(selectseq)[::-1]
            temp=int(len(selectseq)/2-1)
            if selectseq[:temp] == reverse_complement_seq[:temp]:
                maxlen = len(selectseq)
                if maxlen > 14:
                    start = i+1
                    end = i+j+1
                    CPSeq = selectseq
                    print(argv['input'].strip(".fa")+"\t"+str(start)+"\t"+str(end)+"\t"+str((maxlen-(temp*2)))+"\t"+str(maxlen)+"\t"+CPSeq+"\n")
