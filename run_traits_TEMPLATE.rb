#this is intended to be run on RevBayes v1.0.0
#v1.0.1 changed several function names
# 
fl <- "TRAITINFILE"  #continuous character set used for analysis in nexus format
outtr <- "OUTTREEFILE" #file to write sampled trees
outlf <- "OUTLOGFILE" #MCMC log
outsm <- "OUTSUMFILE" #MAP summary tree file
contData<- readContinuousCharacterData(fl)

numTips = contData.ntaxa()
numNodes = numTips * 2 - 1
names = contData.names()
diversification ~ dnLognormal(0,1)
turnover = 0 #we are going to parameterise the BD prior
speciation := diversification + turnover
extinction := turnover 
sampling_fraction <- 1
psi ~ dnBDP(lambda=speciation, mu=extinction, rho=sampling_fraction, rootAge=1, nTaxa=numTips,names=names) #instantiate a tree with the parameters set above
mvi = 0 #we are going to set tree rearrangement and node height scaling moves
moves[++mvi] = mvSubtreeScale(psi, weight=5.0)
moves[++mvi] = mvNodeTimeSlideUniform(psi, weight=10.0)
moves[++mvi] = mvNNI(psi, weight=5.0)
moves[++mvi] = mvFNPR(psi, weight=5.0)

monitors[3] = mnFile(filename=outtr, printgen=100,separator = TAB, psi)

logSigma ~ dnNormal(0,1) #place a prior on BM sigma.
sigma := 10^logSigma
moves[++mvi] = mvSlide(logSigma, delta=1.0, tune=true, weight=2.0)

#specify that we are going calculate BM likelihood using the REML PIC algorithm 
traits ~ dnPhyloBrownianREML(psi, branchRates=1.0, siteRates=sigma, nSites=contData.nchar())

traits.clamp( contData )
bmv = model(sigma)
monitors[1] = mnScreen(printgen=50000, sigma)
monitors[2] = mnFile(filename=outlf, printgen=400, separator = TAB,sigma)

#set up MCMC
chain = mcmc(bmv, monitors, moves)
chain.burnin(generations=50000,tuningInterval=500)
chain.run(150000)
treetrace = readTreeTrace(file = outtr, "clock")
treefl <-outsm

#set MAP tree (we will also summarise trees as MCC representation outside revbayes
map = mapTree( file=treefl, treetrace )
q()

