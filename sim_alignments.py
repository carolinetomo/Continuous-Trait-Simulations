import sys,os

ctldir = sys.argv[1]+"/"
for i in os.listdir(ctldir):
    cmd = "echo indelible_control_files/"+i+" | indelible"
    os.system(cmd)
    
cmd = "rm *.fas"
os.system(cmd)
cmd = "mv *.phy alignments/"
os.system(cmd)
