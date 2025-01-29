import kagglehub

# Download latest version
path = kagglehub.dataset_download("juhibhojani/airline-reviews")

print("Path to dataset files:", path)