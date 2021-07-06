
from mitmproxy import http
def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"]="susan"
    print(flow.request.headers)
