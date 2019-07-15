from blackduck.HubRestApi import HubInstance
import os
import git
import subprocess

hub = HubInstance()

def gitClone():
#clone the splitter repo
    remote = 'https://github.com/blackducksoftware/json-splitter.git'
    local = 'json-splitter'

    if (os.path.exists(local)):
       print('REPO ALREADY EXISTS...MOVING ON')
    else:
       print('CLONING REPO TO ' + local)
       git.Repo.clone_from(remote, local)

#split the files, ignoring .restconfig and any split files
def splitFiles():
    for file in os.listdir("."):
        if file.endswith(".json") and not file.startswith(".rest"):
            file_to_move = file
            print('SPLITTING JSON FILES...')
            split_result = subprocess.call(["python", "json-splitter/src/split_scan_graph_json.py", file], stdout=subprocess.DEVNULL)
            os.rename(file, file+'.split')

#loop over the directory again looking for files to push to hub
def uploadFiles():
    for file in os.listdir("."):
        if file.endswith(".json") and not file.startswith(".rest"):
            print('UPLOADING ' + file + '...')
            response = hub.upload_scan(file)
            os.rename(file, file+'.uploaded')

gitClone()
splitFiles()
uploadFiles()
