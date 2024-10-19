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

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f'{self.code} - {message}')

print(AppException.Timeout.value, AppException.Timeout.message, AppException.Timeout.exception)

try:
    raise AppException.Timeout.exception(f'{AppException.Timeout.value} - {AppException.Timeout.message}')
except Timeout as ex:
    print(ex)

try:
    raise AppException.NotAnInteger.throw()
except Exception as ex:
    print(ex)

try:
    raise AppException.NotAnInteger.throw('blah blah blah')
except Exception as ex:
    print(ex)

print(list(AppException))

print([(ex.name, ex.code, ex.exception, ex.exception.__name__, ex.message) for ex in AppException])



