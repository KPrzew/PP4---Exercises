text = input("Podaj tekst, który chcesz dodać do pliku: ")
with open("text.txt","a") as f:
    print(text)
    f.write(text + "\n")