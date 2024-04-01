import argparse
import pandas as pd
import os


def json_to_csv(json_file, csv_file):
    # Read the JSON file into a pandas DataFrame
    df = pd.read_json(json_file)

    # Create a copy of the DataFrame to modify the columns
    df_copy = df.copy()

    # Convert "Objetivos" (Objectives) and "Finalidades" (Goals) columns to comma-separated strings
    df_copy["Objetivos"] = df_copy["Objetivos"].apply(lambda x: ", ".join(x))
    df_copy["Finalidades"] = df_copy["Finalidades"].apply(lambda x: ", ".join(x))

    # Rename the columns
    df_copy.columns = ["IDProc", "Titulo", "Objetivos", "Finalidades"]

    # Check if the output file already exists
    if os.path.exists(csv_file):
        # If it exists, append the new data to the end of the file
        df_copy.to_csv(csv_file, mode='a', header=False, index=False, quoting=1)
    else:
        # If it doesn't exist, write the DataFrame to the CSV file
        df_copy.to_csv(csv_file, index=False, quoting=1)


def main():
    parser = argparse.ArgumentParser(description="Convert JSON file to CSV format")
    parser.add_argument("-i", "--input", help="Input JSON file path", required=True)
    parser.add_argument("-o", "--output", help="Output CSV file path")
    args = parser.parse_args()

    json_file = args.input

    if args.output:
        csv_file = args.output
    else:
        # If output file not provided, use the same name as JSON file with .csv extension
        base_name = os.path.splitext(json_file)[0]
        csv_file = f"{base_name}.csv"

    json_to_csv(json_file, csv_file)
    print(f"Conversion completed. CSV file saved to: {csv_file}")


if __name__ == "__main__":
    main()
