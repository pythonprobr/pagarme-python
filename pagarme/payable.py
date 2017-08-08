from pagarme.resources import handler_request
from pagarme.resources.routes import payable_routes


def create(dictionary):
    return handler_request.post(payable_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(payable_routes.GET_ALL_PAYABLES)


def find_by(search_param):
    return handler_request.get(payable_routes.GET_PAYABLE_BY.format(search_param))