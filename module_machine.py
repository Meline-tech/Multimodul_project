import module_coffee
import module_tea
functions = ["Wait for powering on", "Powered on", "Wait for powering off", "Powered off"]
class Machine():
    def __init__(self, functions:list):
        self.functions = functions
        self.is_on = False

    def power_on(self):
        if self.is_on:
            print(functions[1])
        else:
            self.is_on = True
            print(functions[0])
    def power_off(self):
        if not self.is_on:
            print(functions[3])
        else:
            self.is_on = False
            print(functions[2])
    def preference(self):
        pass



