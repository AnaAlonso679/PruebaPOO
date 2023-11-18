class CustomerService:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, issue):
        self.customers[name] = issue
        print(f"Gracias {name}, hemos registrado tu problema: '{issue}'")

    def view_issues(self):
        if not self.customers:
            print("No hay problemas reportados actualmente.")
        else:
            print("Problemas reportados:")
            for name, issue in self.customers.items():
                print(f"Cliente: {name} - Problema: {issue}")


service = CustomerService()

while True:
    print("\nOpciones:")
    print("1. Reportar un problema")
    print("2. Ver problemas reportados")
    print("3. Salir")

    choice = input("Seleccione una opción: ")

    if choice == '1':
        name = input("Ingrese su nombre: ")
        issue = input("Describe tu problema: ")
        service.add_customer(name, issue)
    elif choice == '2':
        service.view_issues()
    elif choice == '3':
        print("Gracias, vuelva pronto.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")