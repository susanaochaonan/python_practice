from mitmproxy import http
def request(flow: http.HTTPFlow):
    if 'quote.json' in flow.request.pretty_url:
        with open(r"F:\a.json",'r') as f:
            flow.response=http.HTTPResponse.make(
                200,
                f.read(),
                {"Content-Type": "application/json"}
            )

            print(flow.response)