# gocloud_youtube
This project provides example on how to push/delete video files to/from YouTube using Google's Sample code provided on
https://developers.google.com/youtube/v3/quickstart/python 
https://github.com/youtube/api-samples

Google provided samples uses Python 2 version. For this test, code has been convered to Python 3.

Prerequisite: Refer to the Python Quickstart section on 
https://developers.google.com/youtube/v3/quickstart/python



Execute python file with the following arguments from the command line.

python upload_video.py --file="{provide path to the video file}" \
                       --title="{provide title of the video}" \
                       --description="{description }" \
                       --keywords="key word" \
                       --category="22" \
                       --privacyStatus="private"


To delete file from YouTube run this command and provide Youtube Video ID

python delete.py --id {YouTube Video ID}


