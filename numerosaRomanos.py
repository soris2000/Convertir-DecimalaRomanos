#Convertir Numeros enteros a Romanos
import math 
diccionario={
    "millares":{
        0:"",1:"M",2:"MM",3:"MMM"
    },
    "centenas":{
        0:"",1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCC",9:"CM"
    },
    "decenas":{
        0:"",1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"
    },
    "unidades":{
        0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"
    }
    
}

def convertirNumero(n):
    m=(math.trunc(n/1000))%10
    c=(math.trunc(n/100))%10
    d=(math.trunc(n/10))%10
    u=(math.trunc(n/1))%10
    if m>3:
        print("El numero no se puede calcular")
    else:
   
        numero=diccionario["millares"][m]+diccionario["centenas"][c]+diccionario["decenas"][d]+diccionario["unidades"][u]
        print("El numero romano es: "+numero)
       
    
print("********CONVERTIR NUMEROS A ROMANOS********")
n=int(input("Dame numero a convertir: "))  
convertirNumero(n)