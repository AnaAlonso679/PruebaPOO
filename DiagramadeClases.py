class cafe:
    def tipo_cafe(self,tipo):
        return tipo
    def marca_cafe(self,marca):
        return marca
    def tamaño_cafe(self,tamaño):
        return tamaño
    
class Ventas(cafe):
    def id_venta(self,id):
        return id 
    def vendedor(self,vendedor):
        return vendedor
    def fecha_venta(self,fecha):
        return fecha
    def hora_venta(self,Hora):
        return Hora  
    def total_venta(self,total):
        return total

Ventas = Ventas()

print(Ventas.tipo_cafe("chocolate"))
print(Ventas.marca_cafe("andatti"))
print(Ventas.tamaño_cafe("grande"))
print(Ventas.id_venta(1))
print(Ventas.fecha_venta(251123))
print(Ventas.hora_venta(1))
    