import random
import string

array_letters = list((string.ascii_uppercase))
number_letters = [str(i) for i in range(0, 10)]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
print(
    "".join(
        random.sample(array_letters, 2)
        + random.sample(number_letters, 2)
        + random.sample(special_characters, 2)
    )
)
