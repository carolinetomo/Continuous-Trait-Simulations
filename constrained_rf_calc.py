import os,sys,dendropy
from dendropy.calculate import treecompare

if len(sys.argv) < 4:
    print "usage: "+sys.argv[0]+ " <true tree directory> <inferred tree directory> <discrete or continuous>"
    sys.exit(0)

ttdir = sys.argv[1]+"/"
itdir = sys.argv[2]+"/"
rfout = open("ALL.euclidean.unwt.rfdist","w")
rfout.write("trait_type\tunweighted_rf\tweighted_rf\teuclidean_dist\n")
trait_cat = sys.argv[3]

for j in os.listdir(itdir):
    if "mcc" in j:  #and j.split(".")[-1]!="rr":#j.split(".")[-2] =="mcc" or j.split(".")[-3]=="mcc": #j.split(".")[-1] == "tre" or j.split(".")[-1] == "sumtree":
        spls = j.split(".")
        num = spls[0]
        tree = dendropy.Tree()
        tns = dendropy.TaxonNamespace()
        tt = tree.get_from_path(ttdir+"dated."+str(num)+".tre","newick",taxon_namespace=tns)
        #it = tree.get_from_path(itdir+i+"/"+j,"newick",taxon_namespace=tns)
        it = tree.get_from_path(itdir+"/"+j,"nexus",taxon_namespace=tns)
        tt.encode_bipartitions()
        it.encode_bipartitions()
        #vals[i].append(str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\n")
        rfout.write(trait_cat+"\t"+str(treecompare.symmetric_difference(tt,it))+"\t"+str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\t"+str(treecompare.euclidean_distance(tt,it))+"\n")


