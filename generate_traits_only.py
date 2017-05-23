import os,sys

if len(sys.argv) < 4:
    print "usage: python "+sys.argv[0]+" <R script for simulation> <directory where simulated trees will be stored> <directory where simulated traits will be stored> <repliates = 100>"
    sys.exit(0)

if len(sys.argv) == 5:
    reps = int(sys.argv[4])
else:
    reps = 100

##run sim_traits_trees.R N times
script = sys.argv[1]
treedir = sys.argv[2]+"/"
traitdir = sys.argv[3]+"/"

#generate files
for i in range(0,reps):
    cmd = "Rscript " + script+ " " + str(i)+" "+ treedir+"dated."+str(i)+".tre" +" " + traitdir
    os.system(cmd) 

#convert traits files from tsv to nexus

for i in os.listdir(traitdir):
    if i.split(".")[-1]=="nex":
        continue
    newfl = open(traitdir+".".join(i.split(".")[0:2])+".nex","w")
    oldfl = open(traitdir+i,"r")
    newfl.write("#NEXUS"+"\n"+"Begin data;"+"\n"+"Dimensions ntax=10 nchar=500;\n" +"Format datatype=Continuous missing = ?;"+"\n"+"Matrix"+"\n")
    for j in oldfl:
        newfl.write(j)
    newfl.write(";"+"\n"+"end;")

cmd = "rm "+traitdir+"*.tsv"
os.system(cmd)

