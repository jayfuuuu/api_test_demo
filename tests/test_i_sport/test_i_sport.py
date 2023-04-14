import json

import pytest

from api.i_sport.constant import ERROR_CODE
from api.i_sport.i_sport_api import ISportAPI
from utils.time import Time


class TestCase:
    api = ISportAPI()
    test_data = json.load(open('./test_data/i_sport/data_i_sport.json'))

    @pytest.mark.parametrize("data", test_data)
    def test_get_datasets(self, data):
        # Data
        init, request, test = data['init'], data['request'], data['test']
        time_format = "%Y%m%d"
        begin_date = Time.relative_time(years=-1911, days=request['offset_days'])
        end_data = Time.relative_time(time=begin_date, days=request['range_days'])
        # Request
        response = self.api.get_activity_list(
            county=request['country'],
            activity_kind=request['activity_kind'],
            activity_date_begin=begin_date.strftime(time_format)[1:],
            activity_date_end=end_data.strftime(time_format)[1:],
            paging=bool(request['paging'])
        ).json()
        # Test
        if test['error_code'] == ERROR_CODE.SUCCESS:
            assert response['errorCode'] == test['error_code']
            assert response['totalCount'] == len(response['data'])
            for events in response['data']:
                assert events['activityKind'] in test['kind']
                assert events['activityCounty'] == test['country']
            """
            TODO: add test content reference by content of database will be better
            """
