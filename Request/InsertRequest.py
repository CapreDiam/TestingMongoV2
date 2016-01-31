import commands

from Request.PerfomanceRequest import PerfomanceRequest


class InsertRequest(PerfomanceRequest):

    def __init__(self):
        pass

    __operation = "echo '{}' > .q && mongo < .q"
    __result_insert = ''


    def perfomance_request(self, request):
        self.__result_insert = commands.getoutput(self.__operation.format(request))


    def get_result(self):
        return self.__result_insert

    def __prepare_result(self):
        pass
