import sys,os
from random import sample

if len(sys.argv) != 3:
    print "usage: "+sys.argv[0]+" <full alignments folder> <# seqs to sample>"
    sys.exit(0)

nchars = sys.argv[2]
full = sys.argv[1]+"/"
sampdir = full.replace("500",str(nchars)) 

for i in os.listdir(full):
    cur=open(full+i,"r")
    samp=open(sampdir+i,"w")
    #lines = {}
    start = False
    for j in cur:
        if j.strip() == "":
            continue
        elif start == False and j.strip() != "Matrix":
            if "Dimensions" in j:
                j=j.replace("500",str(nchars))
            samp.write(j)#+"\n") 
        elif "Matrix" in j.strip(): 
            samp.write(j)#+"\n")
            start = True
        elif j.strip() == ";":
            start = False
            samp.write(";\n")
        elif start == True and j.strip()!=";":
            spls = j.strip().split("\t")
            curtax = spls[0]
            traits = spls[1:]
            samptraits = traits[0:int(nchars)]
            #print len(samptraits)
            samp.write(curtax+"\t"+"\t".join(samptraits)+"\n")




