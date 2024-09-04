import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def combine_csv_files(input_folder, output_folder, output_filename):
    # Ensure input folder exists
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the input folder.")
        return

    # Initialize an empty list to hold dataframes
    dataframes = []

    # Loop through each CSV file and read it into a dataframe
    for file in csv_files:
        filepath = os.path.join(input_folder, file)
        df = pd.read_csv(filepath)
        dataframes.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the combined dataframe to the output folder
    output_filepath = os.path.join(output_folder, output_filename)
    combined_df.to_csv(output_filepath, index=False)

    print(f"Combined CSV has been saved to '{output_filepath}'.")

if __name__ == "__main__":
    # Fetch values from environment variables
    input_folder = os.getenv('INPUT_FOLDER')
    output_folder = os.getenv('OUTPUT_FOLDER')
    output_filename = os.getenv('OUTPUT_FILENAME')

    combine_csv_files(input_folder, output_folder, output_filename)