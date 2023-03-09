# youtube_channel_scraper
Code that uses the YouTube API to scrape channels for their video metadata

# Bash Prerequisites
- pip install google-api-python-client
- pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## Python Quickstart and Client Library
These are great websites for instructions on how to set up python quickstart and client library:
- https://developers.google.com/docs/api/quickstart/python
- https://cloud.google.com/ai-platform/prediction/docs/python-client-library

## API Set Up Instructions
These are great websites for instructions on how to set up your YouTube API Key and Credentials:
- https://blog.hubspot.com/website/how-to-get-youtube-api-key
- https://developers.google.com/youtube/registering_an_application
- https://developers.google.com/youtube/v3/guides/auth/installed-apps

## Python Quickstart and Client Library
These are great websites for instructions on how to set up python quickstart and client library:
- https://developers.google.com/docs/api/quickstart/python
- https://cloud.google.com/ai-platform/prediction/docs/python-client-library

## Obtain a JSON file with the credentials for your Google Service Account:
1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Select the project for which you want to create a service account.
3. In the left-hand menu, click on "IAM & admin" and then select "Service accounts."
4. Click on the "Create Service Account" button.
5. Give your service account a name and description, then click on "Create."
6. Select Owner role under "Projects".
7. Click on "Continue" to complete the role selection process.
8. On the "Create Key" page, select "JSON" as the key type and click on "Create."
9. The JSON file with your service account credentials will be downloaded to your computer.

If you have already created a service account in the Google Cloud Console and you now want to obtain the JSON file with its credentials, you can follow these alternative steps:

1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Select the project that contains the service account for which you want to obtain the JSON file.
3. In the left-hand menu, click on "IAM & admin" and then select "Service accounts."
4. Find the service account for which you want to obtain the JSON file and click on its name.
5. In the "Service account details" page, click on the "Keys" tab.
6. Click on the "Add Key" button and select "JSON" as the key type.
7. The JSON file with the service account credentials will be downloaded to your computer.

## What is a UC Code?
- UC code is the unique identifier for a YouTube channel
- It typically takes the format of https://www.youtube.com/channel/UCLOtswgQ-2WRs5WX2gt86Xw
- With the above example, the UC code is: UCLOtswgQ-2WRs5WX2gt86Xw
