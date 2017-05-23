require(phytools)
require(OUwie)

args <- commandArgs(trailingOnly = TRUE)
rep <- toString(args[1])#3
time_tre <- read.tree(toString(args[2]))#"testT"
traitdir <- toString(args[3])#"testTr"

reg<-data.frame(taxon=time_tre$tip.label,Reg=1:length(time_tre$tip.label))
reg[,2]<-1
time_tre$node.label <- reg[,2][1:9]
sim<-OUwie.sim(time_tre,reg,alpha=c(10e-10,10e-10),
               sigma.sq=c(0.05,0.05),theta0=1.0,theta=c(0,0))

for(i in 1:500) {
        sim[,i+1] = OUwie.sim(time_tre,reg,
            alpha=c(10e-10,10e-10),
            sigma.sq=c(0.05,0.05),
            theta0=1.0,
            theta=c(0,0)
        )[,3]
}

traitfl <- paste("traits.",rep,".tsv",sep="")
write.table(sim,sep = "\t", row.names=FALSE,col.names=FALSE,quote=FALSE,file=paste(traitdir,traitfl,sep=""))
