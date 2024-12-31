import pandas as pd
import pickle

# Load the CSV file
file_path = 'Data/survey.csv'  # Replace with your actual file path
survey_data = pd.read_csv(file_path)

# Save the data as a pickle file
pickle_file_path = 'Data/survey.pkl'  # Replace with your desired pickle file path
with open(pickle_file_path, 'wb') as pkl_file:
    pickle.dump(survey_data, pkl_file)

print(f"Data has been saved as a Pickle file: {pickle_file_path}")
