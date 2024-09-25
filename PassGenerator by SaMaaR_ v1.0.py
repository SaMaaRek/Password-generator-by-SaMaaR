import random
small = "abcdefghijklmnopqrstvwxyz"
big = small.upper()
numbers = "1234567890"
rest = "!@#$%^&*()-_=+]}[{;:'/?.>,<\|~``}]" + '"'
charts = small + numbers + big + small + big + small + big + rest
a = True
c = ""
d = ""
def generujHasło():
    x = 0
    i = 0
    b = True
    password = ""
    while b == True:
        print("Ile chcesz znaków? (12-99)")
        ask = input()
        try:
            ask = int(ask)
        except ValueError:
            print("Nieprawidłowy typ!")  
        if type(ask) is int and 10<=ask<=99:
            b = False
        else: 
            print("Coś poszło nie tak, spróbuj ponownie")
    while(x < ask):
        c = random.choice(charts)
        if(x>0):
            if(i % 4 == 0):
                password = password + "-"
        password = password + c
        x+=1
        i+=1
    print("Twoje hasło to: " + password)

print("Generator haseł by SaMaaR_")
print("Aby zapewnić największe bezpieczeństwo, hasło powinno mieć minimum 10 znaków oraz minimum jedną cyfrę oraz jeden znak specjalny")
generujHasło()
while a == True:
    print("Czy chcesz wygenerować nowe hasło? (Y/N)")
    ask = input()
    if(ask.capitalize() == "Y"):
        generujHasło()
    else:
        a = False
print("Dziękuję, za użycie generatora haseł"' v1.0 PassGen by SaMaaR_')