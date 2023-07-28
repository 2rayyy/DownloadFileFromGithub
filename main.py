import requests

def download_file_from_github(url, save_as):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors during the download

        with open(save_as, 'wb') as f:
            f.write(response.content)

        print(f"File downloaded and saved as '{save_as}'")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading the file: {e}")

if __name__ == "__main__":
    # Replace 'GITHUB_RAW_FILE_URL' with the direct link to the file on GitHub
    github_raw_file_url = 'https://raw.githubusercontent.com/2rayyy/FindChromeDriver/main/requirements.txt'

    # Replace 'local_filename' with the desired file name to save the downloaded file as
    local_filename = 'requirement.txt'

    download_file_from_github(github_raw_file_url, local_filename)
