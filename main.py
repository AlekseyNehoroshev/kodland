meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ":"шутка",
            "ЩИЩ":"Одобрение или Восторг",
            "КРИПОВЫЙ":"страшный,пугающий",
            "АГРИТЬСЯ":"злиться"
            }
print("привет, это программа, чтобы расшифровать сленговое слово. Введи слово большими буквами")
for i in range(5):
            word = input("Введите непонятное слово (большими буквами!): ")
            
            if word in meme_dict.keys():
                print(meme_dict[word])
            else:
                print("попробуйте написать слово с соотвествием с условиями")
