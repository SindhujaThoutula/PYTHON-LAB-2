import numpy as np
a = np.random.randint(5,15,20)
print("List:")
print(a)
print("Frequent value:")
print(np.bincount(a).argmax())