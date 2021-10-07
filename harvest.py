############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairings(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
   
    musk = MelonType (
        "musk", 
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )    

    casab = MelonType(
        "cas",
        2003,
        "orange",
        True,
        None,
        "Casaba"
    )

    shaw = MelonType(
        "cren",
        1996,
        "green",
        True,
        None,
        "Crenshaw"
    )
    watermel = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "Watermelon"
    )
    

    musk.add_pairings(["mint"])
    casab.add_pairings(["strawberries", "mint"])
    shaw.add_pairings(["prosciutto"])
    watermel.add_pairings(["ice cream"])

    all_melon_types.append(musk)
    all_melon_types.append(casab)
    all_melon_types.append(shaw)
    all_melon_types.append(watermel)
    
    #all_melon_types = [musk, casab, shaw, watermel]
    # print(all_melon_types)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        
        print(melon.pairings)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_codes = {}
    for melon in melon_types:
       melon_codes[melon.code] = {}
    # print(melon_codes)
    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, code, shape_rating, color_rating, field, harvested):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field 
        self.harvested = harvested

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False
        
       

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    # Fill in the rest
    nine_melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila') 
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    nine_melons = [melon_1, melon_2, melon_3, melon_4,
                   melon_5, melon_6, melon_7, melon_8, melon_9]
    
    return nine_melons
    
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
        
    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable() is True:
            print(f"Harvested by {melon.harvested} from Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvested} from Field {melon.field} (NOT SELLABLE)")


kay = list(make_melon_types())
print_pairing_info(kay)

make_melon_type_lookup(kay)

all_types = make_melons(kay)
get_sellability_report(all_types)
# print(all_types)