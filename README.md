# Extracting the list of hosted websites from Jenkins

The intention is to extract the list of client names and its hosted websites of a specific job name like simplified list instances from the Jenkins server and store it in some data format like csv and most preferably Google Sheets.

## Connecting to the Jenkins Server

### Steps to reproduce the data from Jenkins server
1. Login to your Jenkins account.
2. Generate an API token from the configure settings.
3. Connect to the Jenkins Server.
4. Get Job Information from your desired Job.
5. Extract the required build number.
6. Print the build data from its console output to a text file.

#### To get the client name and client routes data from the text file
* Iterate over the lines from the text file.
* Extract the strings that are required from the lines
* Store it into some data format like list.
* Convert the list into a CSV fomat and load it to the google sheets.

## Connecting to the Google Sheets
1. Go to the site https://console.developers.google.com/
2. Login to your google account.
3. Create new project and enable Google Sheets API and Google Drive API.
4. Get the credentials.json file.

The following libraries are used access the Google Sheets are:
* Gspread
* Oauth2client

Follow this documentation to get more details related to Python- Jenkins
* [Python-Jenkins Documentation](https://python-jenkins.readthedocs.io/en/latest/examples.html)