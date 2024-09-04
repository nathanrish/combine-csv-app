import os
import pandas as pd
import logging
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='combine_csv.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_env_variable(var_name, default_value=None):
    return os.getenv(var_name, default_value)

def combine_csv_files(input_folder, output_folder, output_filename):
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        logging.error(f"Input folder '{input_folder}' does not exist.")
        return

    # Create output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    if not csv_files:
        print("Error: No CSV files found in the input folder.")
        logging.error("No CSV files found in the input folder.")
        return

    dataframes = []

    for file in csv_files:
        filepath = os.path.join(input_folder, file)
        try:
            # Read CSV file and handle bad lines
            df = pd.read_csv(filepath, on_bad_lines='skip')
            dataframes.append(df)
            print(f"Successfully read {file}.")
            logging.info(f"Successfully read {file}.")
        except pd.errors.ParserError as e:
            print(f"Warning: Error reading {file}: {e}")
            logging.warning(f"Error reading {file}: {e}")
        except Exception as e:
            print(f"Error: Unexpected error reading {file}: {e}")
            logging.error(f"Unexpected error reading {file}: {e}")

    if dataframes:
        try:
            # Combine all dataframes
            combined_df = pd.concat(dataframes, ignore_index=True)
            output_filepath = os.path.join(output_folder, output_filename)
            combined_df.to_csv(output_filepath, index=False)
            print(f"Combined CSV has been saved to '{output_filepath}'.")
            logging.info(f"Combined CSV has been saved to '{output_filepath}'.")
        except Exception as e:
            print(f"Error: Failed to save the combined CSV: {e}")
            logging.error(f"Failed to save the combined CSV: {e}")
    else:
        print("No valid dataframes to combine.")
        logging.info("No valid dataframes to combine.")

if __name__ == "__main__":
    # Get configuration from environment variables
    input_folder = get_env_variable('INPUT_FOLDER', 'input')
    output_folder = get_env_variable('OUTPUT_FOLDER', 'output')
    output_filename = get_env_variable('OUTPUT_FILENAME', 'combined_output.csv')

    combine_csv_files(input_folder, output_folder, output_filename)
