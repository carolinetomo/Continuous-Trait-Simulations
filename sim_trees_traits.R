require(phytools)
require(OUwie)
require(ape)

args <- commandArgs(trailingOnly = TRUE)
rep <- 3#toString(args[1])
treedir <- "testT"#toString(args[2])
traitdir <- "testTr"#toString(args[3])

time_height <- 1
time_tre <- pbtree(b=1,d=0,scale=time_height,n=10,nsim=1,type="continuous")
#time_tre <-read.newick("testTdated.2.tre")
mol_height <- 1
mol_tre <- time_tre
mol_tre$edge.length <- mol_tre$edge.length*(mol_height/time_height)


reg<-data.frame(taxon=time_tre$tip.label,Reg=1:length(time_tre$tip.label))
reg[,2]<-1
time_tre$node.label <- reg[,2][1:9]
sim<-OUwie.sim(time_tre,reg,alpha=c(10e-10,10e-10),
               sigma.sq=c(0.5,0.5),theta0=1.0,theta=c(0,0))

for(i in 1:50) {
        sim[,i+1] = OUwie.sim(time_tre,reg,
        alpha=c(10e-10,10e-10),
        sigma.sq=c(0.5,0.5),
        theta0=1.0,
        theta=c(0,0)
        )[,3]
}

mol_tre_nm <- paste("mol.",rep,".tre",sep="")
dated_tree_nm <- paste("dated.",rep,".tre",sep="")
traitfl <- paste("traits.",rep,".tsv",sep="")

write.tree(mol_tre,file=paste(treedir,mol_tre_nm,sep=""))
write.tree(time_tre,file=paste(treedir,dated_tree_nm,sep=""))
write.table(sim,sep = "\t", row.names=FALSE,col.names=FALSE,quote=FALSE,file=paste(traitdir,traitfl,sep=""))
