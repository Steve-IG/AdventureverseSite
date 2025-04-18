import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Base URL
base_url = 'https://www.adventureversegame.com/'

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(os.path.join('assets', filename), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching page: {str(e)}")
        return None

def main():
    # Get the page content
    content = get_page_content(base_url)
    if not content:
        return

    # Parse the HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all images
    images = soup.find_all('img')
    
    # Download each image
    for img in images:
        src = img.get('src')
        if src:
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, src)
            filename = os.path.basename(src)
            download_image(absolute_url, filename)

if __name__ == "__main__":
    main() 