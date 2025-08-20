import price_modul
comp_prices = {"tea": 50, "water": 20, "flowers":40}
class Tea():
    def __init__(self, name, components: dict):
        self.name = name
        self.components = components

    def get_price(self):
        return price_modul.calculate_price(self.components, comp_prices)

    def prepare(self):
        print(f"Պատրաստվում է {self.name} ")
        for components, deal in self.components.items():
            print(f" Պարունակում է {deal} գրամ  {components}")
        print(f" {self.name}-ն պատրաստ է")


class Black(Tea):
    def __init__(self):
        super().__init__("Սև թեյ", {"tea": 100, "Water": 50})

    def prepare(self):
        print("Այժմ կպատրաստենք սև թեյ")
        super().prepare()


class Black_with_flowers (Tea):
    def __init__(self):
        super().__init__("Ծաղիկներով թեյ", {"tea": 100, "flowers": 100, "Water": 50})

    def prepare(self):
        print("Այժմ կպատրաստենք ծաղկային սև թեյ")
        super().prepare()
black = Black()
black.prepare()
print (f"Սև թեյի արժեքը կլինի {black.get_price()} դրամ")

fl_black = Black_with_flowers()
fl_black.prepare()
print (f"Ծաղիկներով սև թեյի արժեքը կլինի {fl_black.get_price()} դրամ")