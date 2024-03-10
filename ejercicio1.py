class Coche:
    def __init__(self, marca, modelo):
        # Asigna la marca proporcionada al atributo 'marca'
        self.marca = marca
        # Asigna el modelo proporcionado al atributo 'modelo'
        self.modelo = modelo

    def conducir(self):
        return f"Conduciendo el {self.marca} {self.modelo}"

if __name__ == "__main__":
    coche = Coche("Toyota", "Corolla")
    coche.conducir()