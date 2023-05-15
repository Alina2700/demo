'''
-Se citesc datele din fisierul input.txt linie cu linie
a. i. sa scoatem numele separat de nr de absente
-Se aloca drepturile codului asupra fisierului
'''
import io #modulul care se ocupa de gestionare fisiere "input - output"
# f este o variabila care sa reprezinte fisierul
f = open("input.txt", "r") #r=permisiuni de citire. w= permisiuni de scriere
#se citeste prima linie din fisier
header= f.readline()
print(header.split(","))

max_no=0
name= ""

for line in f.readlines():
    #print(line) #se afiseaza linie cu linie
    data=line.split(",")
    data[1]=int(data[1]) #conversie la un nr intreg din sir de caractere
    data=tuple(data) #folosim tuplu pentru ca vom stoca data de tipul "nume, numar"
    if max_no < data[1]: #data[1] este stocat numarul de absente
        max_no=data[1]
        name= data[0]

f.close #obligatoriu cand lucram cu fisiere
print("Elevul cu cele mai multe absente este %s si are %d absente" %(name, max_no))
#se stocheaza in singurul tip de data care permite asta, tuplul
