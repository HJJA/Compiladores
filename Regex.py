import re

def Menu():
    print("\n"*50)
    print("\t\t****************************************\n"
          "\t\t** VALIDADOR DE EXPRESIONES REGULARES **\n"
          "\t\t**          DE TIPO: A485btf%$(       **\n"
          "\t\t****************************************\n"
          "\t\t** 1) Validar expresion               **\n"
          "\t\t** 2) Salir                           **\n"
          "\t\t****************************************")
    opc = int(input("Selecione Opcion: "))
    if (opc < 1 or opc>2):
        print("Ingrse opcion valida")
        Menu()
    else:
        return opc

def ValidarExp(entrada):
    patron = re.compile('^[A-Z][\d]{3}[a-z]+[\W]{3}$')

    if patron.search(entrada):
        resul = patron.search(entrada).group(0)
        if (resul == entrada):
            print("La expresion ",entrada,"Pertenece a esta expresión regular...")
    else:
        print("No pertenece a esta expresión regular...")


opc = Menu()
while(opc==1 or opc==2):
    if(opc==1):
        print("\n" * 50)
        entrada = input("INGRESE LA EXPRESION REGULAR: ")
        ValidarExp(entrada)
        input("\n>>>>Presione enter para regresar al menu<<<<")
        opc = Menu()
    if(opc==2):
        print("\n" * 50)
        print("FIN DEL PROCESO")
        opc=0