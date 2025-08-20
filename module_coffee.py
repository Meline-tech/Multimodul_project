import price_modul
comp_prices = {"Espresso": 600, "Milk": 400}
class Coffee():
    def __init__(self, name, components: dict):
        self.name = name
        self.components = components

    def get_price(self):
        return price_modul.calculate_price(self.components, comp_prices)

    def prepare(self):
        print(f"Պատրաստվում է {self.name} ")
        for components, deal in self.components.items():
            print(f" Պարունակում է {deal} մլ  {components}")
        print(f" {self.name}-ն պատրաստ է")



class Latte(Coffee):
    def __init__(self):
        super().__init__("Latte", {"Espresso": 50, "Milk": 150})

    def prepare(self):
        print("Այժմ կպատրաստենք սուրճ Լատտե")
        super().prepare()


class Espresso(Coffee):
    def __init__(self):
        super().__init__("Espresso", {"Espresso": 200, "Milk": 0})

    def prepare(self):
        print("Այժմ կպատրաստենք սուրճ Էսպրեսսո")
        super().prepare()
class Cappuccino(Coffee):
    def __init__(self):
        super().__init__("Cappuccino", {"Espresso": 70, "Milk": 130})

    def prepare(self):
        print("Այժմ կպատրաստենք սուրճ Կապուչինո")
        super().prepare()

latte=Latte()
latte.prepare()
print(f"Լատեի գինը՝ {latte.get_price()} դրամ")

espresso = Espresso()
espresso.prepare()
print(f"Էսպրեսսոյի գինը՝ {espresso.get_price()} դրամ")