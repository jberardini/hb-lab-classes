class AbstractMelonOrder(object):
    """All melon orders"""

    def __init__(self, species, qty, country_code, tax, order_type):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
    

    def get_total(self):
        """Calculate price"""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic melon order"""
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 'U.S', 0.08, 'domestic')


class InternationalMelonOrder(AbstractMelonOrder):
    """An international melon order"""

    def __init__(self, species,qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 0.17, 'international')
        
