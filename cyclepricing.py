from datetime import date

class Component:
    def __init__(self, component_id, name, component_type):
        self.component_id = component_id
        self.name = name
        self.component_type = component_type


class ComponentPrice:
    def __init__(self, component_id, price, effective_from, effective_to=None):
        self.component_id = component_id
        self.price = price
        self.effective_from = effective_from
        self.effective_to = effective_to

    def is_valid(self, selected_date):
        if selected_date < self.effective_from:
            return False

        if self.effective_to is not None:
            if selected_date > self.effective_to:
                return False

        return True


class PricingService:

    def __init__(self, components, prices):
        self.components = components
        self.prices = prices

    def get_valid_price(self, component_id, selected_date):

        valid_prices = []

        for price in self.prices:

            if price.component_id == component_id:
                if price.is_valid(selected_date):
                    valid_prices.append(price)

        if len(valid_prices) == 0:
            raise Exception("Price not available")

   
        valid_prices.sort(
            key=lambda x: x.effective_from,
            reverse=True
        )

        return valid_prices[0].price

    def calculate_price(self, selected_components, selected_date):

        total = 0

        for component_id, quantity in selected_components:

            price = self.get_valid_price(
                component_id,
                selected_date
            )

            total = total + (price * quantity)

        return total


components = [
    Component(1, "Mountain Frame", "FRAME"),
    Component(2, "Shimano Gear", "GEAR"),
    Component(3, "Hero Tyre", "TYRE"),
    Component(4, "Disc Brake", "BRAKE")
]




prices = [

    ComponentPrice(
        1, 5000,
        date(2026, 1, 1),
        date(2026, 12, 31)
    ),

    ComponentPrice(
        2, 2000,
        date(2026, 1, 1),
        date(2026, 12, 31)
    ),

    ComponentPrice(
        3, 200,
        date(2026, 1, 1),
        date(2026, 11, 30)
    ),

    ComponentPrice(
        3, 230,
        date(2026, 12, 1),
        None
    ),

    ComponentPrice(
        4, 800,
        date(2026, 1, 1),
        date(2026, 12, 31)
    )
]



pricing_service = PricingService(
    components,
    prices
)

selected_components = [
    (1, 1),  
    (2, 1),  
    (3, 2),  
    (4, 1),
]

selected_date = date(2026, 12, 10)

total_price = pricing_service.calculate_price(
    selected_components,
    selected_date
)

print("Total Cycle Price: ₹", total_price)