class calculadora:
    def sumar(numero,numero2):
        return numero+numero2
    def restar(numero,numero2):
        return numero-numero2    
    def multiplicar(numero,numero2):
        return numero*numero2
    def dividir(numero,numero2):
        return numero/numero2
    
obj = calculadora
print(obj.sumar(1,1))
print(obj.restar(1,1))
print(obj.multiplicar(1,1))
print(obj.dividir(1,1))
    