# while cu account cu soldul bancar
#def fun_account():
    # account = 1000
    # print ("suma de bani:",account )
    # baniiDescos = int(input("introdu suma "))
    # while account >= baniiDescos :
    #     account = account - baniiDescos
    #     print ("suma disponibila:", account)
    #     baniiDescos = int(input("introdu suma "))  
#fun_account()

# def bancomat (suma_totala) :
#     print("Suma ramasa:", suma_totala)
#     #suma_de_extras= int(input("Cat doresti sa scoti?"))
#     for step in range (3) :
#         baniiDescos = int(input("introdu suma : "))
#         if suma_totala- baniiDescos >=0:
#             suma_totala-= baniiDescos
#             print("Suma ramasa:", suma_totala)
#         else :
#             print ("Fonduri insuficiente")
#             break
# bancomat (1500)
# print ("Incercari terminate ")


# cuvant = "abcdfg"

# for step in range (len(cuvant)):
#     print (step,cuvant[step])


# txt = " welcome to the town"
# x = txt.split()
# print (x) 

# Lista de cumparaturi 
#QT_B = quantity to buy ; P_P = price per product; M_Q= max quantity

QT_B = [3, 5, 1, 10, 2]
P_P = [10, 4, 8, 6, 1]
M_Q = [100, 30, 40, 10]
def fun_list (QT_B, P_P, M_Q) :
    assert (len(QT_B) ==len(P_P) ==len(M_Q), "Nu putem procesa deoaarece datele sunt invalide") 



fun_list(QT_B, P_P, M_Q)    


try : 
    a = 1
    print (a/0)

except Exception:
    print ("err")

finally:
    print(" Executam de fiecare data ")

print("INCA TRAIESC!")