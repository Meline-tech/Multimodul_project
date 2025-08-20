def calculate_price (components, comp_prices):
    total = 0
    for component, deal in components.items():
        price_per = comp_prices.get(component, 0)

        total += deal * price_per/100
    return total



