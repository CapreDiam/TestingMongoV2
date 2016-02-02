import commands

from Request.PerfomanceRequest import PerfomanceRequest
from Strings.SingletonString import SingletonString


class InsertRequest(PerfomanceRequest):

    __strings = SingletonString()
    __result_insert = ''

    def __init__(self):
        pass




    def perfomance_request(self, request):
        self.__result_insert = commands.getoutput(self.__strings.operation.format(request))


    def get_result(self):
        return self.__result_insert

    def __prepare_result(self):
        pass
