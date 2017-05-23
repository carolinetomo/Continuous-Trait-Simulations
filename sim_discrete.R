require(geiger)

args <- commandArgs(trailingOnly = TRUE)
tree <- read.tree(toString(args[1]))
traitdir <- toString(args[2])
iter <- toString(args[3])
rate <- as.numeric(args[4])

#change transition frequencies as needed
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char= sim.char(tree,q,model="discrete",n=500)
char = data.frame(char)

outfl = paste(traitdir,toString(iter),".discrete.tsv",sep="")
write.table(char,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = outfl) 



