import webbrowser
def firefox (url1):
    if url1=='facebook':
     facebook_link()
     print(url1)
    
    
    
def facebook_link():
    url = "https://www.facebook.com"  # Replace with the URL you want to open
     # Open Firefox with the specified URL
    webbrowser.get("firefox").open(url)     
