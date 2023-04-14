from urllib.parse import urljoin

from api.base_api import BaseAPI
from api.env.config import ISportConfig


class ISportAPI(BaseAPI):
    """i運動資訊平台 API

    Document: https://isports.sa.gov.tw/Api/Rest/v1/openData.html#/Activity.svc/activityList
    """
    BASE_URL = urljoin(ISportConfig.BASE_URL, "Api/Rest/V1/Activity.svc/")
    ACTIVITY_LIST = "GetActivityList"

    def get_activity_list(
            self, county: str, activity_kind: str, activity_date_begin: str, activity_date_end: str,
            paging: bool, page_size: int = None, page_no: int = None
    ):
        """取得體育活動清單

        Args:
            county (str): 縣市
            activity_kind (int): 活動類型
            activity_date_begin (str): 活動日期查詢起日(民國年)
            activity_date_end (str): 活動日期查詢訖日(民國年)
            paging (bool): 是否需要分頁
            page_size (int): 分頁筆數
            page_no (int): 分頁頁碼

        Returns:
            dict: 平台刊登之體育活動清單
        """
        url = urljoin(self.BASE_URL, self.ACTIVITY_LIST)
        params = {
            'county': county,
            'activity_kind': activity_kind,
            'activity_date_begin': activity_date_begin,
            'activity_date_end': activity_date_end,
            'paging': paging,
            'page_size': page_size,
            'page_no': page_no
        }
        response = self.send_request(url=url, method="GET", params=params)
        return response
