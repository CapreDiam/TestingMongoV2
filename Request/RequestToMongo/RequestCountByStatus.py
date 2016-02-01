import re

from Request.PerfomanceRequest import PerfomanceRequest


class RequestCountByStatus(PerfomanceRequest):

    __statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
    __string_insert = 'db.orders.find( { status:  "'
    __string_insert_count = '" } ).count()'
    __result_request = []
    
    def __init__(self):
        pass

    def get_result_request(self):
        self.__do_request()
        return self.__result_request
        
    def __do_request(self):
        self._PerfomanceRequest__do_request("db.orders.find().sort( { $date: -1} )")
        for i in range(len(self.__statuses)):
            self.prepare_result(self._PerfomanceRequest__do_request(self.__string_insert +
                                                                    self.__statuses[i] +
                                                                    self.__string_insert_count))

    def prepare_result(self, res):
        #print "Count By Status",  res
     #   res.split("/n") r'"(\S*?)"' [1-9]
        result = re.findall(r'\n(\S*?)\n', res)
        #print "Count By Status result ",  result[0]
        self.__result_request.append(result[0])
