# splitscan

A simple python wrapper which will call the Hub Rest API and JSON splitter to perform the following options:

1. Splits all json files in the directory and renames it to filename.split
2. Uploads the split scan graph jobs and renames them to uploaded

Requires the Blackduck Hub Rest API bindings to upload:

pip install blackduck
