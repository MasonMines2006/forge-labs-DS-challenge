import kagglehub

# Specify the target folder where you want to save the dataset
target_folder = "/Users/mmines/PycharmProjects/forge-labs-DS-challenge/data"

# Download the latest version of the dataset and save it to the target folder
path = kagglehub.dataset_download("paulchambaz/google-street-view", target_folder)

print("Path to dataset files:", path)
