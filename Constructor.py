class tennis:
    def __init__ (self, costo, talla, color):
        self.costo = costo
        self.talla = talla
        self.color = color

#utiliza el nombre de la clase correctamente (tennis en lugar de tenis)
nike_air = tennis("1800", 28, "negro")
nike_air_2 = tennis("2800", 27, "rojos")

#utiliza f-strings para formatear las cadenas 
print(f"Primer Tennis:{nike_air.color},{nike_air.talla},{nike_air.costo}")
print(f"Segundos Tennis: {nike_air_2.color},{nike_air_2.talla},{nike_air_2.costo}")

