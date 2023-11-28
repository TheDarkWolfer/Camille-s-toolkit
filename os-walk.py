import os

def walk(dir,verbose=False):
    # Specify the directory path

    out={}

    # Ensure the specified path is a directory
    if os.path.isdir(dir):
        # Iterate through the files in the directory
        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            # Check if it's a file (not a subdirectory)
            if os.path.isfile(file_path):
                # Get the file size in bytes
                file_size_bytes = os.path.getsize(file_path)
                # Convert file size to megabytes
                file_size_megabytes = file_size_bytes / (1024 * 1024)
                # Print the filename and size in MB

                out[filename]=file_size_megabytes

                if verbose:
                    print(f'File: {filename}, Size: {file_size_megabytes:.2f} MB')
        return out
    else:
        #return -1 if there's an error
        return -1