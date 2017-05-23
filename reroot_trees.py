import sys,os

indir = sys.argv[1]+"/"

for i in os.listdir(indir):
    if "mcc" in i:
        cmd = "pxrr -u -t "+indir+i + " > "+indir+i+".rr"
        os.system(cmd)
