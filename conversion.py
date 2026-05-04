"""Functions that convert metric and imperial units."""

# Temperature 
def cel2fah(c):
    """Converts from Celsius to Fahrenheit."""
    return 9/5 * c + 32

def fah2cel(f):
    """Converts from Fahrenheit to Celsius."""
    return 5/9 * (f - 32)

# Length 
def km2mi(km):
    """Converts from kilometers to miles."""
    return km / 1.60934

def mi2km(mi):
    """Converts from miles to kilometers."""
    return mi * 1.60934

def cm2in(cm):
    """Converts from centimeters to inches."""
    return cm / 2.54

def in2cm(inches):
    """Converts from inches to centimeters."""
    return inches * 2.54

# Weight 
def kg2lb(kg):
    """Converts from kilograms to pounds."""
    return kg * 2.20462

def lb2kg(lb):
    """Converts from pounds to kilograms."""
    return lb / 2.20462

# Volume 
def l2gal(liters):
    """Converts from liters to gallons."""
    return liters / 3.78541

def gal2l(gallons):
    """Converts from gallons to liters."""
    return gallons * 3.78541