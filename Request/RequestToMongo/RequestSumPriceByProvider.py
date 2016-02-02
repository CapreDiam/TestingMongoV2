import re

from Request.PerfomanceRequest import PerfomanceRequest
from Strings.SingletonString import SingletonString


class RequestSumPriceByProvider(PerfomanceRequest):

    __strings = SingletonString()
    __result_request = []
    __providers = ['*', '~']

    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request

    def __do_request(self):
        for i in range(len(self.__providers)):
            res = self._PerfomanceRequest__do_request(self.__strings.string_insert_sum_price + self.__strings.providers[i] + self.__strings.string_insert_sum_price_second_part)
            self.prepare_result(res)

    def prepare_result(self, res):
        result = re.findall(r': (\S*?) ', res)
        self.__result_request.append(round(float(result[1]), 2))
