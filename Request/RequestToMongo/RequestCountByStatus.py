import re

from Request.PerfomanceRequest import PerfomanceRequest
from Strings.SingletonString import SingletonString


class RequestCountByStatus(PerfomanceRequest):

    __string = SingletonString()
    __result_request = []
    
    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self._PerfomanceRequest__do_request(self.__string.string_prepare_db)
        for i in range(len(self.__string.statuses)):
            self.prepare_result(self._PerfomanceRequest__do_request(self.__string.string_insert_count_by_status +
                                                                    self.__string.statuses[i] +
                                                                    self.__string.string_insert_count_by_status_second_part))

    def prepare_result(self, res):
        result = re.findall(r'\n(\S*?)\n', res)
        self.__result_request.append(result[0])
