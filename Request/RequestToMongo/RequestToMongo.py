from RequestByCountStatusID import RequestByCountStatusID
from RequestCountByStatus import RequestCountByStatus
from RequestSumBetweenDate import RequestSumBetweenDate
from RequestSumPriceByProvider import RequestSumPriceByProvider


class RequestToMongo(RequestByCountStatusID, RequestCountByStatus, RequestSumBetweenDate, RequestSumPriceByProvider):
    __result_request = []
    __request_to_db = [RequestByCountStatusID(), RequestCountByStatus(), RequestSumBetweenDate(),
                       RequestSumPriceByProvider()]


    def get_result_request(self):
        self.__do_request()
        return self.__result_request

    def __do_request(self):
        for i in self.__request_to_db:
            self.__result_request.extend(i.get_result_request())
