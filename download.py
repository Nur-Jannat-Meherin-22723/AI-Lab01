'''import requests

downloadUrl = 'https://www.junkybooks.com/book/the-handbook-of-international-trade-and-finance'

req  = requests.get(downloadUrl)

# Accessing headers in Python
headers = req.headers
print(headers)

print("URL:", req.url)

filename = req.url[downloadUrl.rfind('/')+1:]
print(filename)

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            
def download_file(url, filename=''):
    try:
        if filename:
            pass
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]
            
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                
            return filename
        
    except Exception as e:
        print(e)
        return None
    
    
downloadLink = 'https://www.junkybooks.com/administrator/thebooks/6483a9c6a2e4d-the-handbook-of-international-trade-and-finance.pdf'
download_file(downloadLink, 'download.pdf')
print("download Successful")'''
##################################################################################################################################
'''
import requests
import os

def download_file(url, filename=''):
    try:
        if not filename:
            # If no filename is provided, extract from the URL
            filename = url.split("/")[-1]

        with requests.get(url) as req:
            req.raise_for_status()  # Raise an exception for bad responses
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            return filename

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

# Example usage
downloadLink = 'https://www.junkybooks.com/administrator/thebooks/6483a9c6a2e4d-the-handbook-of-international-trade-and-finance.pdf'
downloaded_filename = download_file(downloadLink, 'download.pdf')

if downloaded_filename:
    print(f"Download successful. File saved as: {downloaded_filename}")
else:
    print("Download failed.")
'''

import requests
import os

def download_file(url, filename=''):
    try:
        if not filename:
            # If no filename is provided, extract from the URL
            filename = url.split("/")[-1]

        # Specify the directory where you want to save the file
        save_path = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson'

        # Create the directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Combine the directory and filename
        filepath = os.path.join(save_path, filename)

        with requests.get(url) as req:
            req.raise_for_status()  # Raise an exception for bad responses
            with open(filepath, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

        return filepath

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

# Example usage
downloadLink = 'https://www.junkybooks.com/administrator/thebooks/6483a9c6a2e4d-the-handbook-of-international-trade-and-finance.pdf'
downloaded_filepath = download_file(downloadLink, 'download.pdf')

if downloaded_filepath:
    print(f"Download successful. File saved at: {downloaded_filepath}")
else:
    print("Download failed.")
