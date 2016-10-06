class AbstractMelonOrder(object):
    """All melon orders"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None
    

    def get_total(self):
        """Calculate price"""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic melon order"""
    self.order_type = "domestic"
    self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international melon order"""

    def __init__(self, species,qty, country_code):
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init___(self, species, qty)

    def get_country_code(self):
    """Return the country code."""

    return self.country_code