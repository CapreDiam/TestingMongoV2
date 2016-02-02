import commands
from Strings.SingletonString import SingletonString


class PerfomanceRequest:
    __strings = SingletonString()

    def __do_request(self, string_insert):
        return commands.getoutput(self.__strings.operation.format(string_insert))
