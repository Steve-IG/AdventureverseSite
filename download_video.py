import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_video(url, filename):
    try:
        print(f"Downloading video from {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        filepath = os.path.join('assets', filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching page: {str(e)}")
        return None

def main():
    base_url = 'https://www.adventureversegame.com/'
    content = get_page_content(base_url)
    
    if not content:
        return

    soup = BeautifulSoup(content, 'html.parser')
    
    # Look for video elements or background videos in the page
    video_elements = soup.find_all(['video', 'source'])
    
    for video in video_elements:
        src = video.get('src') or video.get('data-src')
        if src:
            video_url = urljoin(base_url, src)
            download_video(video_url, 'hero-video.mp4')
            break

if __name__ == "__main__":
    if not os.path.exists('assets'):
        os.makedirs('assets')
    main() 