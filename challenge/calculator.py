class Calculator:
    def __init__(self, type_error, value_error, name_error, zero_division_error):
        self.type_error = type_error
        self.value_error = value_error
        self.name_error = name_error
        self.zero_division_error = zero_division_error

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.error = exc_value
        return exc_value