import re

from Request.PerfomanceRequest import PerfomanceRequest


class RequestCountByStatus(PerfomanceRequest):

    __result_request = []
    
    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self._PerfomanceRequest__do_request(self._PerfomanceRequest__strings.string_prepare_db)
        for i in range(len(self._PerfomanceRequest__strings.statuses)):
            self.prepare_result(self._PerfomanceRequest__do_request(self._PerfomanceRequest__strings.string_insert_count_by_status +
                                                                    self._PerfomanceRequest__strings.statuses[i] +
                                                                    self._PerfomanceRequest__strings.string_insert_count_by_status_second_part))

    def prepare_result(self, res):
        result = re.findall(r'\n(\S*?)\n', res)
        self.__result_request.append(result[0])
