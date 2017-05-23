import os,sys

if len(sys.argv) < 5:
    print "usage: python "+sys.argv[0]+" <R script> <directory of trees> <output directory> <transition rate>"
    sys.exit(0)

script = sys.argv[1]
treedir = sys.argv[2]
traitdir = sys.argv[3]
rate = sys.argv[4]
reps = 100

for i in range(0,reps):
    cmd = "Rscript "+script+" "+ treedir+"dated."+str(i)+".tre"+" "+ traitdir +" "+str(i) +" "+str(rate)
    os.system(cmd)

for i in os.listdir(traitdir):
        if i.split(".")[-1]=="nex":
            continue
        newfl = open(traitdir+".".join(i.split(".")[0:2])+".nex","w")
        oldfl = open(traitdir+i,"r")
        newfl.write("#NEXUS"+"\n"+"Begin data;"+"\n"+"Dimensions ntax=10 nchar=500;\n" +"Format datatype=standard missing = ?;"+"\n"+"Matrix"+"\n")
        for j in oldfl:
            newfl.write(j)
        newfl.write(";"+"\n"+"end;"+"\n"+"Begin MrBayes;\n\tLset Rates = Equal;\n\tprset applyto=(1) brlenspr=clock:uniform;\n\tmcmc ngen=1000000 samplefreq=100 printfreq=10000 nchains=1 nruns=1;\n\tsump;\n\tsumt burnin = 200;\n\tquit;\nend;")

cmd = "rm "+traitdir+"*.tsv"
os.system(cmd)
