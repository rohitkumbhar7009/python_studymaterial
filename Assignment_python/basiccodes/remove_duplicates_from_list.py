# Remove duplicates from a list 7Way remove duplicates


# ✅ 1. Using set() (no order guaranteed)
nums = [1,2,4,0,525,4,1,45,8,5,7,48,4,00,7,4,5,3,458,2]
unique =  list(set(nums))
print("1st Way",unique)


# ✅ 2. Using a for loop (preserves order)

uniuqe2 = []

for num in nums:
    if num not in uniuqe2:
        uniuqe2.append(num)

print("2nd Way",uniuqe2)



# ✅ 3. Using dict.fromkeys() (preserves order)

# Why this works:
# dict.fromkeys(nums) creates a dictionary with keys from nums (and removes duplicates since dictionary keys are unique).

# Then we convert the keys back into a list.
unique3 = list(dict.fromkeys(nums))

print("3rd way",unique3)



# ✅ 4. Using list comprehension + set
# This also preserves order.
# Trick: set.add() returns None, so x in seen or seen.add(x) works to both check and add.
seen = set()
unique4 = [x for x in nums if not (x in seen or seen.add(x))]
print("4th way",unique4)



# ✅ 5. Using collections.OrderedDict() (older Python < 3.7)
from collections import OrderedDict
unique5 = list(OrderedDict.fromkeys(nums))
print("5th way", unique5)


# ✅ 6. Using pandas (if already working with DataFrames)
import pandas as pd
unique6 = pd.Series(nums).drop_duplicates().tolist()
print("6th way",unique6)

# ✅ 7. Using NumPy (if you're working with numeric data)

import numpy as np
unique7 = np.unique(nums).tolist()
print("7th way ",unique7)