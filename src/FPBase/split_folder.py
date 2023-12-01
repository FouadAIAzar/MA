import os
import random
import shutil

# Directory where the files are located
source_dir = 'adjusted_spectra/'
# Directory where 10% of the files will be moved
test_dir = os.path.join(source_dir, 'test')

# Ensure the test directory exists
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# List all files in the source directory
all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# Calculate the number of files to move to the test set (10%)
num_test_files = int(len(all_files) * 0.10)

# Randomly select files for the test set
test_files = random.sample(all_files, num_test_files)

# Move the selected files to the test directory
for file in test_files:
    shutil.move(os.path.join(source_dir, file), os.path.join(test_dir, file))

print(f"Moved {len(test_files)} files to the test set in {test_dir}")

