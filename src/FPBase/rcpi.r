library("Rcpi")
x <- readFASTA(system.file('protseq/P00750.fasta', package = 'Rcpi'))[[1]]
x <- x[(sapply(x, checkProt))]
# Generalized BLOSUM and PAM Matrix-Derived Descriptors
#blosum = extractPCMBLOSUM(x, submat = 'AABLOSUM62', k = 5, lag = 7, scale = TRUE, silent = FALSE)

#blosum

descscales = extractPCMDescScales(x, propmat = 'AATopo', index = c(37:41, 43:47),
pc = 5, lag = 7, silent = FALSE)

descscales
