import json
import urllib2
import base64

# For testing
# ip = '127.0.0.1'
# port = '8080'

# For deployment
# port = '80'

# The username on XBMC's web interface (just comment or delete this line if you don't use authentication
# username = 'xbmc'
# Same as the username.
# password = 'xbmc'

#method = 'Addons.ExecuteAddon'
#parameters = {"addonid":"script.artwork.downloader", "params":{"silent":"true"}, "wait":True}


def getJsonRemote(method,parameters='',host='127.0.0.1',port='8080'):
    ''' Wrapper for HTML JSON requests for XBMC '''
    
    # First we build the URL we're going to talk to
    url = 'http://%s:%s/jsonrpc' %(host, port)
    # Next we'll build out the Data to be sent
    values ={}
    values["jsonrpc"] = "2.0"
    values["method"] = method
    # This fork handles instances where no parameters are specified
    if parameters:
        values["params"] = parameters
    values["id"] = "1"
    headers = {"Content-Type":"application/json",}
    # Format the data
    data = json.dumps(values)

    #print('JSON Req: %s\n' % data)

    # Now we're just about ready to actually initiate the connection
    req = urllib2.Request(url, data, headers)
    #print('HTTP Req: %s\n' % req)

    # This fork kicks in only if both a username & password are provided
    #if username and password:
        # This properly formats the provided username & password and adds them to the request header
    #    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    #    req.add_header("Authorization", "Basic %s" % base64string)
 
    # try: statement to allow for graceful error handling
    try:
        response = urllib2.urlopen(req)
        response = response.read()
        response = json.loads(response)
        # A lot of the XBMC responses include the value "result", which lets you know how your call went
        # This logic fork grabs the value of "result" if one is present, and then returns that.
        # Note, if no "result" is included in the response from XBMC, the JSON response is returned instead.
        # You can then print out the whole thing, or pull info you want for further processing or additional calls.
        if 'result' in response:
            response = response['result']
    # This error handling is specifically to catch HTTP errors and connection errors
    except urllib2.URLError as e:
        # In the event of an error, I am making the output begin with "ERROR " first, to allow for easy scripting.
        # You will get a couple different kinds of error messages in here, so I needed a consistent error condition to check for.
        response = 'ERROR '+str(e.reason)
    return response
