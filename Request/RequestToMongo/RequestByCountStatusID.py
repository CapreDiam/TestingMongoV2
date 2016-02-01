import re

from Request.PerfomanceRequest import PerfomanceRequest


class RequestByCountStatusID(PerfomanceRequest):

    __result_request = []
    __string_insert = 'db.orders.aggregate( { $group: { _id: "$id", count: { $sum: 1 } } }, { $limit: 1 } )'
    
    def __init__(self):
        pass



    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self.__prepare_result(self._PerfomanceRequest__do_request(self.__string_insert))

    
    def __prepare_result(self, first_result):
        #print "By COunt Status ID OK", first_result
        result = re.findall(r': (\S*?) ', first_result)
        #print "By COunt Status ID result ", result[1]
        #result = re.findall(r'[1-9]+\n', first_result)
       # for i in range(len(result) - 2):
        self.__result_request.append(result[1])
