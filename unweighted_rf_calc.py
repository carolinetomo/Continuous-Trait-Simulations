import os,sys,dendropy
from dendropy.calculate import treecompare

if len(sys.argv) < 3:
    print "usage: "+sys.argv[0]+ " <true tree directory> <inferred tree directory>"
    sys.exit(0)

ttdir = sys.argv[1]+"/"
itdir = sys.argv[2]+"/"
rfout = open(sys.argv[2].replace("/","")+".unwt.rfdist","w")

for i in os.listdir(itdir):
    if i.split(".")[-1] != "sumtree":
        continue
    spls = i.split(".")
    num = spls[0]
    tree = dendropy.Tree()
    tns = dendropy.TaxonNamespace()
    #tt = tree.get_from_path(ttdir+"dated."+str(i)+".tre","newick",taxon_namespace=tns)
    tt = tree.get_from_path(ttdir+"dated."+str(num)+".tre","newick",taxon_namespace=tns)
    #it = tree.get_from_path(itdir+str(i)+".tre","nexus",taxon_namespace=tns)
    it = tree.get_from_path(itdir+i,"nexus",taxon_namespace=tns)
    tt.encode_bipartitions()
    it.encode_bipartitions()
    #vals[i].append(str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\n")
    rfout.write(str(treecompare.symmetric_difference(tt,it))+"\n")



