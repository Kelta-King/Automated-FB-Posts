from . import "config_hid.py" as config

def getAccessToken():
    return config.accessToken
    
def getPageId():
    return config.pageId
    
def getPageAccessToken():
    return config.pageAccessToken
    
def getAppId():
    return config.appId
    
def getClientToken():
    return config.clientToken

def getUserId():
    return config.userId

# Config_hid.py file looks like below
# 
# accessToken = "ACCESS_TOKEN"
# appId = "APP_ID"
# clientToken = "CLIENT_TOKEN"
# pageId = "PAGE_ID"
# userId = "USER_ID"
# pageAccessToken = "PAGE_ACCESS_TOKEN"