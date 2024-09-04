# Combine CSV App

This Python application allows you to easily combine multiple CSV files into a single CSV file. The application is designed to handle CSV files with identical headers and outputs the combined file into a designated folder.

## Project Structure

```
combine_csv_app/
│
├── combine_csv.py          # The main Python script to combine CSV files
├── requirements.txt        # Python dependencies required to run the script
├── .env                    # Environment variables for configuration
├── input/                  # Folder where you place the CSV files to be combined
├── output/                 # Folder where the combined CSV file will be saved
└── README.md               # This README file
```

## Features

- **Folder-based Input/Output**: Place your CSV files in the `input/` folder and the combined output will be saved in the `output/` folder.
- **Environment Configuration**: Configure the input folder, output folder, and output file name using a `.env` file.
- **Scalable**: Easily extendable to handle large datasets.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed on your system.
- **pip**: Python package installer should be available.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nathanrish/combine-csv-app.git
cd combine-csv-app
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

It's good practice to use a virtual environment to manage dependencies.

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure the Environment Variables

Edit the `.env` file to specify your configuration:

```bash
# .env
INPUT_FOLDER=input
OUTPUT_FOLDER=output
OUTPUT_FILENAME=combined_output.csv
```

- `INPUT_FOLDER`: Folder where your CSV files are located.
- `OUTPUT_FOLDER`: Folder where the combined CSV file will be saved.
- `OUTPUT_FILENAME`: Name of the output CSV file.

### 5. Prepare Input Files

Place all the CSV files you want to combine in the `input/` folder.

### 6. Run the Application

Execute the Python script to combine the CSV files:

```bash
python combine_csv.py
```

The combined CSV file will be saved in the `output/` folder with the name specified in the `.env` file (default: `combined_output.csv`).

## Usage Example

Suppose you have three CSV files (`file1.csv`, `file2.csv`, `file3.csv`) in the `input/` folder. Running the script will produce a single `combined_output.csv` file in the `output/` folder containing all the data from these three files.

## Troubleshooting

### Common Issues

- **No CSV Files in the Input Folder**: Ensure that you have placed CSV files in the `input/` folder.
- **Output Folder Not Created**: The script should create the `output/` folder if it does not exist. Ensure you have the necessary write permissions.
- **Merge Conflicts**: Ensure all CSV files have identical headers.

### Log Output

The script will print status messages to the console, informing you of the progress and any issues encountered.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Python dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.

