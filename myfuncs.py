
#una funcion es un segmento de codigo que puede llamarse desde cualquier lugar
#estas pueden o no retornar valores
var3 = 'hola'
def funcion1 ():
    print("funcion 1")

def func_params (param1, param2, param3):
    print("funcion parametros: ", param1, param2, param3)

def func_return():
    return "esto es un retorno"

if __name__ == '__main__':
    funcion1()
    func_params(1,2,3)
    func_params(3,2,1)
    var = func_return()
    print(var)
    print (func_return())