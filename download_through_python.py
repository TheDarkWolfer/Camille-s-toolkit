import subprocess
import re

def download_with_progress(url, output_path):
    command = ["wget", url, "-O", output_path]

    # Start the subprocess
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1,
    )

    # Regular expression pattern to match download progress
    progress_pattern = re.compile(r"(\d+)%.*", re.MULTILINE)

    # Process the output of wget
    for line in iter(process.stdout.readline, ""):
        print(line, end="")  # Print the wget output

        # Match the progress percentage
        progress_match = progress_pattern.match(line)
        if progress_match:
            progress_percent = int(progress_match.group(1))
            print(f"Download Progress: {progress_percent}%")

    process.stdout.close()
    return process.wait()

url = "https://download.kiwix.org/zim/wikipedia_fr_all_maxi.zim"
output_path = "wikipedia_fr_all_maxi.zim"

return_code = download_with_progress(url, output_path)
if return_code == 0:
    print("Download complete.")
else:
    print("Download failed.")
