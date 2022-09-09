from urllib.parse import urlparse

# Checks if URL is valid
def isValidURL(url):
    try:
        res = urlparse(url)
        if res[1] == "pub-calgary.escribemeetings.com":
            return True
        else:
            return False
    except ValueError:
        return False