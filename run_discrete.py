import sys,os

if len(sys.argv) != 2:
    print "usage: python "+sys.argv[0]+ " <discrete character directory>"
    sys.exit(0)

traitdir = sys.argv[1]+"/"

for i in os.listdir(traitdir):
    if i.strip().split(".")[-1] != "nex":
        continue
    cmd = "mb "+traitdir+i
    os.system(cmd)

