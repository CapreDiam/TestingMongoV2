from datetime import datetime, timedelta


class SingletonString:

    clean_db = 'db.orders.remove({})'
    insert_request = 'db.orders.insert({})'
    size = 20
    string_insert_by_count_status_id = 'db.orders.aggregate( { $group: { _id: "$id", count: { $sum: 1 } } }, { $limit: 1 } )'
    statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
    string_insert_count_by_status = 'db.orders.find( { status:  "'
    string_insert_count_by_status_second_part = '" } ).count()'
    string_prepare_db = "db.orders.find().sort( { $date: -1} )"
    string_request_sum_between_date = "db.orders.aggregate( [ { $match : { date: { $gte: " \
                      "new Date(" + str(datetime.now() - timedelta(25)) + "),$lte: " \
                      "new Date(" + str(datetime.now() - timedelta(20)) + ") } } }, { $group: { _id:" " null, " \
                       "count: { $sum: 1 } } } ] )"
    providers = ['*', '~']
    string_insert_sum_price = "db.orders.aggregate( [ { $match : { provider: " + '"'
    string_insert_sum_price_second_part = '"' + " } }, { $group: { _id: " + '"' + "$provider" + '"' + ", sum: { $sum: " + \
                                            '"' + "$price" + '"' + " } } } ] )"
    operation = "echo '{}' > .q && mongo < .q"

    class __SingletonString:

        def __init__(self):
            pass

    instance = None

    def __init__(self):
        if not SingletonString.instance:
            SingletonString.instance = SingletonString.__SingletonString()
        else:
            SingletonString.instance.val = self

    def __getattr__(self):
        return getattr(self.instance)
