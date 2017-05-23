import sys,os

if len(sys.argv) < 2:
    print "usage: python " + sys.argv[0]+ " <input directory>"
    sys.exit(0)

indir = sys.argv[1]+"/"

for i in os.listdir(indir):
    spls = i.strip().split(".")
    if spls[-1] == "t" or spls[-1] == "trees":
        treesfl = indir+i
        outtre = indir+".".join(spls[0:-1])+".mcc.tre"
        cmd = "treeannotator2 -burnin 20 "+treesfl +" "+outtre
        os.system(cmd)
