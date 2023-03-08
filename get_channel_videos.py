import csv
import os
import google.auth
from googleapiclient.discovery import build
import json
import sys
# Optional
from googleapiclient.errors import HttpError

# YouTube Data API v3 key
API_KEY = 'YOUR_API_KEY'

# File that houses string UC codes, 1 per line
SOURCE_FILE = 'YOUR_SOURCE_FILE.csv'

# Google Service account credentials specified in a JSON file
CREDENTIALS_FILE = 'YOUR_CREDENTIALS_FILE.json'

# Create a folder where your Video .json files can be stored
OUTPUT_DIRECTORY = 'YOUR_OUTPUT_DIRECTORY'

# Create a YouTube API client
# Setting this environment variable allows applications to access Google APIs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_FILE
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Make function to get video ids from uploads playlist
def get_channel_videos(channel_id, max_videos=100):
    
    # Get Uploads playlist ID
    # Calls the YouTube Data API to retrieve information about a channel
    result = youtube.channels().list(id=channel_id,  
                                  part='contentDetails').execute() 
    # Retrieves the ID of the "uploads" playlist for the channel from the API response
    playlist_id = result['items'][0]['contentDetails']['relatedPlaylists']['uploads'] 
    
    # Initializes an empty list to hold the retrieved videos
    videos = []
    
    # The token for the next page of results to retrieve, initially set to None
    next_page_token = None
    
    # Starts a loop to retrieve all the videos from the "uploads" playlist
    while 1:
        # Calls the YouTube Data API to retrieve a page of videos from the playlist
        result = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        # Add the retrieved videos to the list of videos
        videos += result['items']
        # Gets the token for the next page, or None if no more pages
        next_page_token = result.get('nextPageToken')
        # If there are no more pages or the maximum number of videos has been retrieved, breaks the loop
        if next_page_token is None or len(videos) >= max_videos:
            break
    # Returns the list of retrieved videos
    return videos
    
# Gets video metadata
def get_video_stats(video_id):
    result1 = youtube.videos().list(id=video_id, part='statistics,liveStreamingDetails,contentDetails,snippet,status,topicDetails').execute()
    return result1['items'][0]


# Processes each channel id from a list
def process_channel_videos(channel_id):
    print(f"Processing channel {channel_id}")
    videos = get_channel_videos(channel_id)
    filename = f'{OUTPUT_DIRECTORY}/{channel_id}.json'
    with open(filename, 'w') as f:
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            vstats = get_video_stats(video_id)
            #print('stats')
            #print(vstats)
            #print()
            out_str = json.dumps(vstats)
            #print(out_str)
            f.write(out_str + '\n')

# Loops through SOURCE_FILE to retrieve all videos from UC codes
# and saves them to a file for each UC code
def loop_through_uc_codes():
    with open(SOURCE_FILE, 'r') as uccodes:
        for row in uccodes:
            # Debugs csv headline ufeff issue
            # This will read the csv as the first row not a headline
            channel_id = row.strip().replace(u'\ufeff','')
            process_channel_videos(channel_id)


# Calls the function
if __name__ == "__main__":
    loop_through_uc_codes()

# DNU BELOW
# # put videos in a txt file
# videos = get_channel_videos('UC0CvB-RlwNvox0GEwb8_jdA')
# #open the file
# with open(filename, 'w') as f:
#     for video in videos:
#         video_id = video['snippet']['resourceId']['videoId']
#         vstats = get_video_stats(video_id)
#         print('stats')
#         print(vstats)
#         print()
#         out_str = json.dumps(vstats)
#         print(out_str)
#         #close the file
#         f.write(out_str + '\n')
