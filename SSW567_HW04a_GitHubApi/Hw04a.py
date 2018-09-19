'''
Created on Sep 18, 2018

@author: Kristen Tan
I pledge my Honor that I have abided by the Stevens Honor System. Kristen Tan
'''

import requests
import json

def getGitHubInfo(gitHubUserId):
    """Takes in a username for a GitHub user and returns a list of their repos and the number of commits per repo."""
    try:
        urlString =  "https://api.github.com/users/" + gitHubUserId + "/repos"
    except TypeError as error:
        return "gitHubUserId must be a string"
    resultList = []
    gitHubInfo = requests.get(urlString)
    gitHubInfoJson = json.loads(gitHubInfo.content)
    for repo in gitHubInfoJson:
        gitCommits = requests.get("https://api.github.com/repos/" + gitHubUserId + "/" + repo['name'] + "/commits")
        gitCommitsJson = json.loads(gitCommits.content)
        count = 0
        for commitItem in gitCommitsJson:
            count += 1
        resultList.append([repo['name'], count])
    return resultList #repos will be alphabetical