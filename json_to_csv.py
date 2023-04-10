import os
import pandas as pd
import sys
import json

def is_all_type(l, t):
    # Create a list of booleans indicating whether each element in `l` is of type `t`.
    is_type = [type(x) == t for x in l]
    # Return `True` if all elements in `l` are of type `t`, `False` otherwise.
    return all(is_type)

def flatten_json(y):
    # Initialize an empty dictionary to hold the flattened key-value pairs.
    out = {}
    # Define a helper function to flatten the nested JSON object.
    def flatten(x, name=''):
        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:
             # Iterate through each key-value pair in the dictionary and recursively call the `flatten` function.
            for a in x:
                flatten(x[a], name + a + '_')
 
        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:
            # Check if all elements in the list are integers, floats, or strings.
            is_int = is_all_type(x, int)
            is_float = is_all_type(x, float)
            is_str = is_all_type(x, str)
            # If all elements in the list are of the same type, add the list as a key-value pair to the `out` dictionary.
            if is_int or is_float or is_str:
                out[name[:-1]] = x
            # Otherwise, recursively call the `flatten` function on each element in the list and add the resulting key-value pairs to the `out` dictionary.
            else:
                i = 0
    
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
        # If the Nested key-value pair is neither a dictionary nor a list, add it as a key-value pair to the `out` dictionary.
        else:
            out[name[:-1]] = x
    # Call the `flatten` function on the input JSON object.
    flatten(y)
    # Return the flattened key-value pairs as a single-level dictionary.
    return out

def json_file_to_df(filename):
    # Initialize an empty list to hold the data frames.
    list_df = []
    # Open the file in read-only mode.
    with open(filename, 'r') as f:
        # Iterate through each line in the file.
        for line in f:
             # Load the line as a JSON object.
            jline = json.loads(line)
            # Flatten the JSON object using the `flatten_json` function.
            jline_flat = flatten_json(jline)
            # Convert the flattened key-value pairs to a data frame.
            df = pd.DataFrame.from_dict([jline_flat])
            # Append the data frame to the list.
            list_df.append(df)
    # If no data frames were created, return `None`.
    if len(list_df) == 0:
        return None
    # Concatenate all data frames in the list into a single data frame.
    all_df = pd.concat(list_df)
    # Return the concatenated data frame.
    return all_df

def json_file_to_csv(filename, outpath):
    # Convert the JSON file to a data frame.
    all_df = json_file_to_df(filename)
    # Save the data frame as a CSV file.
    all_df.to_csv(outpath, index=False)

def directory_to_csv(dirpath, outpath):
    # Initialize an empty list to hold the data frames.
    list_df = []
    # Get a list of all files in the directory.
    files = os.listdir(dirpath)
    # Iterate through each file in the directory.
    for i, file in enumerate(files):
        # Check if the file has a `.json` extension.
        if file.endswith('.json'):
            # Create the full path to the file.
            filename = os.path.join(dirpath, file)
            # Print a message indicating which file is being processed.
            print(f"processing {file} ({i} / {len(files)})")
            # Convert the JSON file to a data frame using the `json_file_to_df` function.
            df = json_file_to_df(filename)
            # If the data frame is not empty, append it to the list.
            if df is not None:
                list_df.append(df)
    # Concatenate all data frames in the list into a single data frame.
    all_df = pd.concat(list_df)
    # Save the resulting data frame as a CSV file.
    all_df.to_csv(outpath, index=False)
           

if __name__ == '__main__':
    json_path = sys.argv[1]  # Path to JSON files
    output_path = sys.argv[2]  # Output path
    directory_to_csv(json_path, output_path)