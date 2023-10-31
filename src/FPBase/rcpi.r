library("Rcpi")

# Read the CSV file
data <- read.csv('proteins_info.csv', stringsAsFactors = FALSE)

# Initialize an empty list to store results
results <- list()

# Loop over the rows of data
for(i in 1:nrow(data)) {
  seq <- data$seq[i]
  # Check if the sequence is a protein
  if(checkProt(seq)) {
    paac <- extractProtPAAC(seq)
    results[[i]] <- c(data$id[i], data$seq[i], paac)
  }
}

# Convert list to dataframe
results_df <- do.call(rbind, results)
colnames(results_df) <- c("id", "seq", names(paac))

# Write the dataframe to a new CSV file
write.csv(results_df, 'proteins_paac.csv', row.names = FALSE, quote = FALSE)
