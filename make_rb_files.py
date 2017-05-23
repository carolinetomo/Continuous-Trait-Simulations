import os,sys

traitfpre = "traits.REP.nex"
outtrpre = "REP.trees"
outlfpre = "REP.log"
outsmpre = "REP.sumtree"
reps = 100
runfile = "RUN3.rb"

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "python "+sys.argv[0]+" template traitfolder outfolder"
        sys.exit(0)
    trfolder = sys.argv[2]
    oufolder = sys.argv[3]
    template = open(sys.argv[1],"r")
    templstr = ""
    for i in template:
        templstr += i
    template.close()

    traitfpre = trfolder+"/"+traitfpre
    outtrpre = oufolder+"/"+outtrpre
    outlfpre = oufolder+"/"+outlfpre
    outsmpre = oufolder+"/"+outsmpre

    for i in range(reps):
        tempw = open(runfile,"w")
        tempw.write(templstr.replace("TRAITINFILE",traitfpre.replace("REP",str(i))).replace("OUTTREEFILE",outtrpre.replace("REP",str(i))).replace("OUTLOGFILE",outlfpre.replace("REP",str(i))).replace("OUTSUMFILE",outsmpre.replace("REP",str(i))))
        tempw.close()
        cmd = "rb-mpi "+runfile
        os.system(cmd)
