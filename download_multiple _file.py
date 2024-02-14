import requests
import os
from collections import deque

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

def download_books(links):
    queue = deque(links)

    for index, link in enumerate(queue):
        filename = f'download{index}.pdf'
        downloaded_filepath = download_file(link, filename)

        if downloaded_filepath:
            print(f"Download successful. File saved at: {downloaded_filepath}")
        else:
            print(f"Download failed for link: {link}")

if __name__ == "__main__":
    links = [
        'https://www.junkybooks.com/administrator/thebooks/63546e51cb429-financing-real-estate-investments.pdf',
        'https://www.junkybooks.com/administrator/thebooks/635475f85b56f-money-banking-and-international-finance.pdf',
        'https://www.junkybooks.com/administrator/thebooks/63ee996db7f68-behavioural-economics-and-finance.pdf'
    ]

    download_books(links)
