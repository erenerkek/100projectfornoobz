import random

sentences= "Tamam, başlıyoruz. Odaklan. Hız. Ben hızım. Bir kazanan, kırk iki kaybeden. Ben kaybedenleri kahvaltı niyetine yerim. Kahvaltı? Belki de kahvaltı yapmam gerekirdi. Kahvaltı bana iyi gelebilirdi. Hayır, hayır, hayır, odaklan. Hız. Hızlıdan daha hızlı, çabuktan daha çabuk. Benim adım Şimşek. Hız. Ben hızım".split(".")

quote=[]

print(("-" * 30) + "\nPseudo Quote Generator\n" + ("-" * 30))

n = int(input("Enter number of sentences : "))

for i in range(n):
    quote.append(random.choice(sentences))

print("Your pseudo quote is: {}  ".format(".".join(quote)))

