import re

from Request.PerfomanceRequest import PerfomanceRequest

class RequestByCountStatusID(PerfomanceRequest):

    __result_request = []
    
    def __init__(self):
        pass



    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self.__prepare_result(self._PerfomanceRequest__do_request(self._PerfomanceRequest__strings.string_insert_by_count_status_id))

    
    def __prepare_result(self, first_result):
        result = re.findall(r': (\S*?) ', first_result)
        self.__result_request.append(result[1])
