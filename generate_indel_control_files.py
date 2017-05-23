import sys,os

if len(sys.argv) != 3:
    print "usage " + sys.argv[0]+" <tree directory> <control file directory>"
    sys.exit(0)

trees = []
treedir = sys.argv[1]+"/"
ctldir =  sys.argv[2]+"/"
for i in os.listdir(treedir):
    spls = i.split(".")
    if spls[0]=="dated":
        continue
    tree_index = spls[1]
    fl=open(treedir+i,"r")
    nwk=fl.readline()
    trees.append(nwk)
    outfl = open(ctldir+"ctl"+tree_index+".txt","w")
    outfl.write("[TYPE] NUCLEOTIDE 1\n[MODEL] jukes\n [submodel] JC\n[TREE] tree "+nwk+"\n"+"[PARTITIONS] partition1 \n [tree jukes 1000]\n[EVOLVE]\n\tpartition1 1 aln"+tree_index+"\n")

