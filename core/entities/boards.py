class Phone:

    def __init__(self, name: str, price: int, quantity: int, years: int, id=None):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._years = years
        self._id = id

    # Get method for the attributed name
    @property
    def name(self):
        return self._name

    # Set method for the attributed name
    @name.setter
    def name(self, value):
        self._name = value

    # Get method for the attributed price
    @property
    def price(self):
        return self._price

    # Set method for the attributed price
    @price.setter
    def price(self, value):
        self._price = value

    # Get method for the attributed quantity
    @property
    def quantity(self):
        return self._quantity

    # Set method for the attributed quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    # Get method for the attributed years
    @property
    def years(self):
        return self._years

    # Set method for the attributed years
    @years.setter
    def quantity(self, value):
        self._years = value

    # Get method for the attributed id
    @property
    def id(self):
        return self._id
