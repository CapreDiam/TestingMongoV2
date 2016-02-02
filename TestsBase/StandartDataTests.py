import Tests
from Strings.SingletonString import SingletonString

class StandartDataCalc(Tests.Tests):

    __strings = SingletonString()
    __results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def calculating_standart_data(self, generated_data):
        for element in generated_data:
            if element.get_status() == self.__strings.statuses[0]:
                self.__results[0] += 1
            elif element.get_status() == self.__strings.statuses[1]:
                self.__results[1] += 1
            elif element.get_status() == self.__strings.statuses[2]:
                self.__results[2] += 1
            elif element.get_status() == self.__strings.statuses[3]:
                self.__results[3] += 1
            else:
                self.__results[4] += 1
                # count id, status order
            if element.get_id() == generated_data[0].get_id():
                self.__results[5] += 1
            # sum price for each provider
            if element.get_provider() == "*":
                self.__results[6] += float(element.get_price())
            else:
                self.__results[7] += float(element.get_price())
            # sum price between 2 date
            if element.get_date_time() >= element.get_date_time() and element.get_date_time() <= element.get_date_time():
                self.__results[8] += 1
        self.__results[6] = round(self.__results[6], 2)
        self.__results[7] = round(self.__results[7], 2)

    def get_result(self):
        return self.__results

