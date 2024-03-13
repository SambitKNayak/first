# converters.py has 2 functions:
# kg_to_lbs
# lbs_to_kg

import converters

print(converters.kg_to_lbs(111))

from converters import kg_to_lbs

print(kg_to_lbs(100))
# -------------------

from utils import find_max

numbers = [10, 2, 7, 13]
print(find_max(numbers))

# max,min --> built in function
print(max(numbers))
print(min(numbers))

# package --> set of modules --> set of functions
# shipping.py is module in ecommerce package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()  # calc_shipping() is a function in shipping module

# Alt

from ecommerce.shipping import calc_shipping

calc_shipping()

# Alt-- when shipping is an object then we can accesss all the fuctions inside the shipping module

from ecommerce import shipping

shipping.calc_shipping()

