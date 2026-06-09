from urllib.parse import urlencode


def build_redirect_response(next_url):
    return {
        "status": 302,
        "headers": {
            "Location": next_url,
        },
    }


def build_login_redirect(base_url, email):
    query = urlencode({"email": email})
    return "{}?{}".format(base_url, query)
