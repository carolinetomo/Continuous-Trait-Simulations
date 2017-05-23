require(phytools)

args <- commandArgs(trailingOnly = TRUE)
rep <- toString(args[1])#3
time_tre <- read.tree(toString(args[2]))#"testT"
traitdir <- toString(args[3])#"testTr"

Q<-matrix(c(-0.4,0.4,0.4,-0.4),2,2)
tre<-sim.history(time_tre,Q)
sim<-sim.corrs(tre,vcv)
for(i in 1:19) {
    sim<-cbind(sim,sim.corrs(tre,vcv)) 
}


traitfl <- paste("traits.",rep,".tsv",sep="")
write.table(sim,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file=paste(traitdir,traitfl,sep=""))
