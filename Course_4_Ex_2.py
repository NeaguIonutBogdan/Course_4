def aria(lungime, latime = 0):
    if latime != 0:
        return (lungime*latime)//2
    else:
        return lungime*lungime
arg= int(input("introduceti un nr pentru a calcula aria patratului:"))
x = aria(arg)
print("Aria patratului este: {}".format(x))
#pt triunghi am hardcodat valorile
print("Aria dreptunghiului este: {}".format(aria(16,20)))
