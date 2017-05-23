import sys,os

indir = sys.argv[1]+"/"

for i in os.listdir(indir):
    if "mcc" in i:
        cmd = "pxt2new < "+indir+i+" | pxtscale -r 1 > "+indir+i+".rescale"
        os.system(cmd)
