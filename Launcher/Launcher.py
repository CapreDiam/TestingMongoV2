from Generation.GenerationDataOrder import GenerationDataOrder


class Launcher:


    def __init__(self):
        self.start = GenerationDataOrder()
        self.start.generation_data()
        self.mongo_res = self.start.mongo_test.get_result_request()
        self.standard_data = self.start.calc_standart_data.get_result()

    def starting(self):
        for i in range(len(self.mongo_res)):
            if self.mongo_res[i] == self.standard_data[i]:
                print "OK"
            else:
                print self.mongo_res[i]
                print self.standard_data[i]
                print "Wrong"


a = Launcher()
a.starting()