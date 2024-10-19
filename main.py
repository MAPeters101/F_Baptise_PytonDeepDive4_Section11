from enum import Enum, unique

class GenericException(Exception):
    pass

class Timeout(Exception):
    pass

@unique
class AppException(Enum):
    Generic = 100, GenericException, 'Application exception'
    Timeout = 101, Timeout, 'Timeout connecting to resource'
    NotAnInteger = 200, ValueError, "Value must be an integer"
    NotAList = 201, ValueError, 'Value must be a list'

    def __new__(cls, ex_code, ex_class, ex_message):
        member = object.__new__(cls)

        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

print(AppException.Timeout.value, AppException.Timeout.message, AppException.Timeout.exception)

try:
    raise AppException.Timeout.exception(f'{AppException.Timeout.value} - {AppException.Timeout.message}')
except Timeout as ex:
    print(ex)



