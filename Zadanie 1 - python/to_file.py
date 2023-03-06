text = input("Podaj tekst, który chcesz dodać do pliku: ")
with open("text.txt","a") as f:
    f.write(text + "\n")