import re

from Request.PerfomanceRequest import PerfomanceRequest
from Strings.SingletonString import SingletonString


class RequestByCountStatusID(PerfomanceRequest):

    __string = SingletonString()
    __result_request = []
    
    def __init__(self):
        pass



    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self.__prepare_result(self._PerfomanceRequest__do_request(self.__string.string_insert_by_count_status_id))

    
    def __prepare_result(self, first_result):
        #print "By COunt Status ID OK", first_result
        result = re.findall(r': (\S*?) ', first_result)
        #print "By COunt Status ID result ", result[1]
        #result = re.findall(r'[1-9]+\n', first_result)
       # for i in range(len(result) - 2):
        self.__result_request.append(result[1])
