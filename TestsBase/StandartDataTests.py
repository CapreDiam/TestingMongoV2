import Tests


class StandartDataCalc(Tests.Tests):
    __results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def calculating_standart_data(self, generated_data):
        for element in generated_data:
            if element.get_status() == "New":
                self.__results[0] += 1
            elif element.get_status() == "To Provider":
                self.__results[1] += 1
            elif element.get_status() == "Partially Filled":
                self.__results[2] += 1
            elif element.get_status() == "Filled":
                self.__results[3] += 1
            else:
                self.__results[4] += 1
            # sum price for each provider
            if element.get_provider() == "*":
                self.__results[5] += float(element.get_price())
            else:
                self.__results[6] += float(element.get_price())
            # count id, status order
            if element.get_id() == generated_data[0].get_id():
                self.__results[7] += 1
                # sum price between 2 date
                #buff_date = datetime.strptime(json_string["date"], '%Y.%m.%d %H:%M:%S.%f')
            if element.get_date_time() >= element.get_date_time() and element.get_date_time() <= element.get_date_time():
                self.__results[8] += 1

    def get_result(self):
        return self.__results
