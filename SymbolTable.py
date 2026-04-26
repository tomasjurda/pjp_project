class SymbolTable:
    def __init__(self):
        self._variables = {}

    def __setitem__(self, key, value):
        if key in self._variables:
            print(f"Multiple declaration of variable '{key}'")
            return "error"
        else:
            self._variables[key] = value

    def __getitem__(self, key):
        if key not in self._variables:
            print(f"Unknown variable '{key}'")
            return "error"
        else:
            return self._variables[key]

    def __str__(self):
        s = ""
        for var in self._variables:
            s += f"variable {var} is type {self._variables[var]}\n"
        return s
