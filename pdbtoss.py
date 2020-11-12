from Bio.PDB import DSSP, PDBParser
import os

dir='*/casp11.domains/'
list=os.listdir('*/casp11.domains')
#print(list)
q1=open("/home/ystroot/Documents/seqcasp11.txt","a")
q2=open("/home/ystroot/Documents/sscasp11.txt","a")

for i in list:
    print(i)
    l=dir+i
    p = PDBParser()
    structure = p.get_structure("Model", l)
    model = structure[0]
    dssp = DSSP(model, l)        
    for row in dssp:
        #if row[0] < 1000:
            q1.write(str(row[1]))
        #with open("/home/ystroot/Documents/sscasp11.txt","a") as q2:
            q2.write(str(row[2]))
    q1.write('\n')
    q2.write('\n')

q1.close()
q2.close()
