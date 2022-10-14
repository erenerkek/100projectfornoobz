import random

def nameGen():
    name=["Mynameis","Eren","Jax","Crazyboy"]
    surname=["KahpeninEwladı","Teller","35","Akşamyatmazsabahkalkmazoğulları"]

    return print(random.choice(name)+" "+ random.choice(surname))

for i in range(5):
    nameGen()