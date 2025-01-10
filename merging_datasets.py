import pandas as pd
import os

def merge_datasets(folder_path, files, output_file):
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        
        dataframes = []
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            try:
                print(f"Reading file: {file_path}")
                df = pd.read_csv(file_path)
                dataframes.append(df)
            except FileNotFoundError:
                print(f"Error: File not found - {file_path}")
                continue
            except pd.errors.EmptyDataError:
                print(f"Error: File is empty - {file_path}")
                continue
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
        
        if not dataframes:
            raise ValueError("No valid files to merge. Check file paths and contents.")
        
        merged_df = pd.concat(dataframes, ignore_index=True)
        
        merged_df.to_csv(output_file, index=False)
        print(f"Datasets merged and saved successfully to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = "Pickup Five Cities Datasets"
files = ["pickup_cq.csv", "pickup_hz.csv", "pickup_jl.csv", "pickup_sh.csv", "pickup_yt.csv"]
output_file = "merged_pickup_data.csv"

merge_datasets(folder_path, files, output_file)
