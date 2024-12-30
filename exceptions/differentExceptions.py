'''
These are the most frequently encountered exceptions:

Exception: The base class for all exceptions.
ArithmeticError: Base class for errors in numerical operations.
ZeroDivisionError: Raised when dividing by zero.
OverflowError: Raised when a result is too large to be represented.
FloatingPointError: Raised for floating-point-related errors (rarely used).
'''

def generalException():
    try:
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
    except Exception as e:
        print(f"Caught an exception: {e}")
        print(f"Type of exception: {type(e)}")

def generalException():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except Exception as e:  # Catch other exceptions
        print(f"An unexpected error occurred: {e}")

def arithmeticalError():
    try:
        x=1/0
    except ZeroDivisionError:
        print ('cannot divide by 0')

def overFlow():
    try:
        return 
    except OverflowError:
        print('too large')

'''
IndexError: Raised when accessing a sequence with an out-of-range index.
KeyError: Raised when a dictionary key is not found.
'''
def indexError():
    my_list = [1, 2, 3]
    try:
        print(my_list[5])
    except IndexError:
        print("Index out of range!")

def keyError():
    dict={'a':1,'b':2}
    try:
        return dict['c']
    except KeyError:
        print('Key not found')

'''
ValueError: Raised when a function receives an argument with the right type but an invalid value.
TypeError: Raised when an operation is performed on an incompatible type.
'''

def valueError():
    try:
        return int('abc')
    except ValueError:
        print('Cannot make letters to int')

'''
ImportError: Raised when an import fails.
ModuleNotFoundError: A subclass of ImportError for nonexistent modules.
'''

def importError():
    try:
        import nonexistent_module
    except ModuleNotFoundError:
        print("Module not found!")

'''
FileNotFoundError: Raised when trying to open a nonexistent file.
IOError: Base class for input/output errors (includes FileNotFoundError).
'''

def fileError():
    try:
        with open('nonexistent.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File does not exist!")

'''
AssertionError: Raised when an assert statement fails.
AttributeError: Raised when an invalid attribute is accessed.
'''
def attrError():
    try:
        x = "hello"
        x.append("world")  # Strings don't have an `append` method
    except AttributeError:
        print("Invalid attribute!")

'''
StopIteration: Raised when an iterator has no more items.
RuntimeError: Raised for general runtime errors.
'''

def iterError():
    my_iter = iter([1, 2, 3])
    try:
        while True:
            print(next(my_iter))
    except StopIteration:
        print("Iteration complete!")

'''
KeyboardInterrupt: Raised when the user interrupts program execution (e.g., Ctrl+C).
SystemExit: Raised when the program is exiting.
'''

def keyBoradError():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Program interrupted!")

'''
Custom error
'''

class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print(e)
    
'''
The finally block in Python is used to specify code that should execute no matter what happens in 
the try and except blocks. It is commonly used for cleanup tasks like closing files or releasing resources.
'''

