import os,sys,dendropy
from dendropy.calculate import treecompare

if len(sys.argv) < 3:
    print "usage: "+sys.argv[0]+ " <true tree directory> <inferred tree directory>"
    sys.exit(0)

ttdir = sys.argv[1]+"/"
itdir = sys.argv[2]+"/"
rfout = open("ALL.euclidean.tsv","w")
rfout.write("trait_type\tnum_traits\trate\tunweighted_rf\tweighted_rf\n")

for i in os.listdir(itdir):
    if "discrete" in i:
        trait_cat = "discrete"
        spls = i.split("discrete")
        rate = spls[0]
        aln_size = spls[1]
    elif "traits" in i:
        trait_cat = "continuous"
        spls = i.split("traits")
        rate = spls[0]
        aln_size = spls[1]
    elif "corr" in i or "5SAMP" in i or "8SAMP" in i or os.path.isdir(i) == False:
        continue
    for j in os.listdir(i):
        if j.split(".")[-2] =="mcc": #j.split(".")[-1] == "tre" or j.split(".")[-1] == "sumtree":
            spls = j.split(".")
            num = spls[0]
            tree = dendropy.Tree()
            tns = dendropy.TaxonNamespace()
            tt = tree.get_from_path(ttdir+"dated."+str(num)+".tre","newick",taxon_namespace=tns)
            it = tree.get_from_path(itdir+i+"/"+j,"nexus",taxon_namespace=tns)
            tt.encode_bipartitions()
            it.encode_bipartitions()
            #vals[i].append(str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\n")
            rfout.write(trait_cat+"\t"+str(aln_size)+"\t"+str(rate)+"\t"+str(treecompare.symmetric_difference(tt,it))+"\t"+str(treecompare.weighted_robinson_foulds_distance(tt,it))+"\n")


