import copy

from Request.InsertRequest import InsertRequest


class GenerationInsert:

    __clean_db = 'db.orders.remove({})'
    __orders = []
    __performance_request = InsertRequest()
    __insert_request = 'db.orders.insert({})'

    def __init__(self):
        pass

    def prepare_db(self):
        self.__performance_insert(self.__clean_db)

    def __performance_insert(self, insert_request):
        self.__performance_request.perfomance_request(insert_request)

    def set_orders(self, orders):
        self.__orders = copy.copy(orders)
        self.__prepare_request()

    def __prepare_request(self):
        for i in range(len(self.__orders)):
            self.__performance_insert(self.__insert_request.format(self.__orders[i].get_insert_request()))
