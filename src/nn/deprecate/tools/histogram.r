library(readr)
library(ggplot2)

calculate_bins <- function(data) {
  data <- na.omit(data) # Remove NA values from the data
  
  q25 <- quantile(data, 0.25)
  q75 <- quantile(data, 0.75)
  iqr <- q75 - q25
  
  bin_width <- (2 * iqr) / (length(data)^(1/3))
  num_bins <- round((max(data) - min(data)) / bin_width)
  
  return(num_bins)
}

# Read the CSV file
df <- read_csv('molecules.csv')

# Extract the "Molecular weight (g mol-1)" column
emission_max <- df$`Emission max (nm)`

# Calculate the number of bins
num_bins <- calculate_bins(emission_max)

# Plot the histogram
plot_title <- 'Histogram of Emission Max'

plot <- ggplot(df, aes(x = emission_max)) + 
  geom_histogram(bins = num_bins, fill = "blue", color = "black") +
  labs(title = plot_title, x = 'Emission Max [nm]', y = 'Frequency') + 
  theme_minimal() +
  theme(panel.grid.major = element_line(colour = "grey80"))

# Ensure the "figures" directory exists, if not create it
if (!dir.exists("figures")) {
  dir.create("figures")
}

# Save the plot in the "figures" directory
ggsave(filename = paste0("figures/", plot_title, ".png"), plot = plot)

# Display the plot
print(plot)

