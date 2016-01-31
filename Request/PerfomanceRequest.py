import commands


class PerfomanceRequest:

    __operation = "echo '{}' > .q && mongo < .q"


    def __do_request(self, string_insert):
        return commands.getoutput(self.__operation.format(string_insert))
