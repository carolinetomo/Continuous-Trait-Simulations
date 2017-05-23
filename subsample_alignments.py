import sys,os
from random import sample

if len(sys.argv) != 3:
    print "usage: "+sys.argv[0]+" <full alignments folder> <# seqs to sample>"
    sys.exit(0)

numseqs = sys.argv[2]
full = sys.argv[1]+"/"
sampdir = str(numseqs)+"SAMP_"+full
os.system("mkdir " + sampdir)
for i in os.listdir(full):
    cur=open(full+i,"r")
    samp=open(sampdir+"SAMP."+".".join(i.split(".")[0:-1])+".nex","w")
    header = cur.readline()
    hspls = header.strip().split()
    ntax = hspls[0]
    seqlen = hspls[1]
    lines = []
    for j in cur:
        spls = j.strip().split("\t")
        if j.strip() == "":
            continue
        lines.append(j.strip())
    towrite = sample(lines,int(numseqs))
    samp.write("#NEXUS"+"\n"+"Begin data;"+"\n"+"Dimensions ntax="+str(ntax)+" nchar="+seqlen+";\n" +"Format datatype=dna interleave=no gap=- missing = ?;"+"\n"+"Matrix"+"\n")
    for j in lines:
        if j not in towrite:
            samp.write(j.replace("A","-").replace("C","-").replace("G","-").replace("T","-")+"\n")
    for j in towrite:
        samp.write(j+"\n")
    samp.write(";\nend;")


        
     


