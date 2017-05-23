import os,sys,dendropy
from dendropy.calculate import treecompare

if len(sys.argv) < 3:
    print "usage: "+sys.argv[0]+ " <true tree directory> <inferred tree directory>"
    sys.exit(0)

ttdir = sys.argv[1]+"/"
itdir = sys.argv[2]+"/"
rfout = open("correlated.unwt.rfdist","w")
rfout.write("trait_dimensions\tcovariance\tunweighted_rf\tBLD\n")

for i in os.listdir(itdir):
    spls = i.split("_")
    covar = spls[1]
    dims = spls[2]
    for j in os.listdir(itdir+"/"+i):
        if j.split(".")[-2] == "mcc": #== "tre" or j.split(".")[-1] == "sumtree":
            spls = j.split(".")
            num = spls[0]
            tree = dendropy.Tree()
            tns = dendropy.TaxonNamespace()
            tt = tree.get_from_path(ttdir+"dated."+str(num)+".tre","newick",taxon_namespace=tns)
            it = tree.get_from_path(itdir+i+"/"+j,"nexus",taxon_namespace=tns)
            tt.encode_bipartitions()
            it.encode_bipartitions()
            #vals[i].append(str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\n")
            rfout.write(dims+"\t"+covar+"\t"+str(treecompare.symmetric_difference(tt,it))+"\t"+str(treecompare.euclidean_distance(tt,it))+"\n")

