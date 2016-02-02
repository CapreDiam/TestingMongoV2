import re
from Strings.SingletonString import SingletonString

from Request.PerfomanceRequest import PerfomanceRequest


class RequestSumBetweenDate(PerfomanceRequest):

    __strings = SingletonString()
    __result_request = []

    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request

    def __do_request(self):
        self.__prepare_result(self._PerfomanceRequest__do_request(self.__strings.string_request_sum_between_date))

    def __prepare_result(self, res):
        result = re.findall(r'\n\{.+\}', res)
        self.__result_request.append(result)
