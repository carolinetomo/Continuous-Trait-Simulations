require(phytools)

args <- commandArgs(trailingOnly = TRUE)
rep <- toString(args[1])#3
time_tre <- read.tree(toString(args[2]))#"testT"
traitdir <- toString(args[3])#"testTr"
corr <- 0.1 
mat_size <- 25 

vcv <- matrix(corr,mat_size,mat_size)
diag(vcv)<-1.0

Q<-matrix(c(-0.00001,0.00001,0.00001,-0.00001),2,2) #This maps regimes to tree, allowing covariance strength to vary across the tree. It is set to keep covariance uniform across tree
tre<-sim.history(time_tre,Q)
sim<-sim.corrs(tre,vcv)
for(i in 1:19) {
    sim<-cbind(sim,sim.corrs(tre,vcv)) 
}


traitfl <- paste("traits.",rep,".tsv",sep="")
write.table(sim,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file=paste(traitdir,traitfl,sep=""))
