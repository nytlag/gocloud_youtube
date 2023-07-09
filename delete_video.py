import os
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from oauth2client.tools import argparser, run_flow

# API credentials
CLIENT_SECRETS_FILE = "{replaice with key value}"
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def delete_video(youtube, video_id):
    youtube.videos().delete(id=video_id).execute()
    print("Video with ID '%s' deleted successfully." % video_id)

if __name__ == "__main__":
    argparser.add_argument("--id", required=True, help="Youtube video ID")  
    args = argparser.parse_args()

    youtube = get_authenticated_service()
    video_id = args.id  
    delete_video(youtube, video_id)
