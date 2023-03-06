bruttoval=input("Wprowadź wartość brutto: ")
tax=input("Wprowadź kwotę podatku (w ułamku): ")
nettoval=float(bruttoval)*(1-float(tax))
print(f"Kwota netto wynosi: {nettoval}")
