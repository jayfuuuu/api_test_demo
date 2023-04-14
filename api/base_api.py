import json
import textwrap
import requests
from datetime import datetime


class BaseAPI:
    def __init__(self, waiting_time: int = 5):
        self.waiting_time = waiting_time

    def send_request(self, url: str, method: str, **kwargs):
        response = requests.Session().request(url=url, method=method, **kwargs)
        # self.debug_print(response)
        return response

    @staticmethod
    def debug_print(response: requests.Response):
        req_body = response.request.body
        if req_body:
            req_body = json.loads(req_body)

        try:
            res = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            res = response.text

        information = {
            'datetime': f"{datetime.now():%Y/%m/%d %H:%M:%S}",
            'request': f"[{response.request.method}] {response.request.url}",
            'headers': json.dumps(dict(response.request.headers), indent=4, ensure_ascii=False),
            'body': json.dumps(req_body, indent=4, ensure_ascii=False),
            'elapsed': f"{response.elapsed.total_seconds()} s",
            'status': response.status_code,
            'response': res
        }

        print(textwrap.dedent(
            """
            --------------------------------
            🐞 debug prints
            --------------------------------
            {content}
            --------------------------------
            """
        ).format(content=''.join([f"\n * {key}: {val}" for key, val in information.items()])))
