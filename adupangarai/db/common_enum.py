import enum

@enum.unique
class Category(str, enum.Enum):
    FRUITS = "Fruits"
    VEGETABLES = "Vegetables"
    GROCERIES = "Groceries"
    NONVEG = "Non-Veg"
    SNACKS = "Snacks"


@enum.unique
class Unit(str, enum.Enum):
    KG = "kg"
    GRAMS = "grams"
    LITERS = "liters"
    ML = "ml"
    PIECES = "pieces"
    PACKETS = "packets"
