email = input("Zadajte e-mailovú adresu: ")

if len(email) < 3:
    print("Hmm, e-mailová adresa je príliš krátka.")
elif email.count('@') != 1:
    print("V e-mailovej adrese chýba zavináč.")
else:
    print("Áno, toto môže byť e-mailová adresa.")
