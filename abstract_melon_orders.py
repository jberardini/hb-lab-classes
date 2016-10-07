class AbstractMelonOrder(object):
    """All melon orders"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price"""

        if self.species == "Christmas":
            base_price = 5 * 1.5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == 'international':
            total = total + 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic melon order"""

    tax = 0.08
    order_type = 'domestic'
    country_code = 'U.S.'


class InternationalMelonOrder(AbstractMelonOrder):
    """An international melon order"""

    tax = 0.17
    order_type = 'international'
    flat_fee = 3

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
