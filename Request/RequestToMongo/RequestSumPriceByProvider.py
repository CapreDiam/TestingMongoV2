import re

from Request.PerfomanceRequest import PerfomanceRequest


class RequestSumPriceByProvider(PerfomanceRequest):
    __providers = ['~', '*']
    __result_request = []
    __string_insert_sum_price = "db.orders.aggregate( [ { $match : { provider: " + '"'
    __string_insert_sum_price_second_part = '"' + " } }, { $group: { _id: " + '"' + "$provider" + '"' + ", sum: { $sum: " + \
                                            '"' + "$price" + '"' + " } } } ] )"

    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request

    def __do_request(self):
        for i in range(len(self.__providers)):
            res = self._PerfomanceRequest__do_request(self.__string_insert_sum_price + self.__providers[i] + self.__string_insert_sum_price_second_part)
            self.prepare_result(res)

    def prepare_result(self, res):
        result = re.findall(r'\{.+\}', res)
        self.__result_request.append(result[0])
