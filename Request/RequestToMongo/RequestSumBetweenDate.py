import re

from Request.PerfomanceRequest import PerfomanceRequest


class RequestSumBetweenDate(PerfomanceRequest):
    __string_request = "db.orders.aggregate( [ { $match : { date: { $gte: " \
                      "new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.25" + '"' + "),$lte: " \
                      "new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.725" + '"' + ") } } }, { $group: { _id:" " null, " \
                                                                                                                                                                     "count: { $sum: 1 } } } ] )"
    __result_request = []

    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request

    def __do_request(self):
        self.__prepare_result(self._PerfomanceRequest__do_request(self.__string_request))

    def __prepare_result(self, res):
        print res
        result = re.findall(r'\n\{.+\}', res)
        self.__result_request.append(result)
