class Ticket:
    def _init_(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

class SupportSystem:
    def _init_(self):
        self.tickets = []

    def create_ticket(self, description):
        ticket_id = len(self.tickets) + 1
        new_ticket = Ticket(ticket_id, description, "Nuevo")
        self.tickets.append(new_ticket)
        print(f"Ticket creado con ID {ticket_id}")

    def display_menu(self):
        print("1. Crear nuevo ticket")
        print("2. Revisar tickets")
        print("3. Validar tickets")
        print("4. Salir")

    def review_tickets(self):
        print("Revisando tickets:")
        for ticket in self.tickets:
            print(f"ID: {ticket.id} - Descripción: {ticket.description} - Estado: {ticket.status}")

    def validate_tickets(self):
        print("Validando tickets:")
        for ticket in self.tickets:
            ticket.status = "Validado"
            print(f"ID: {ticket.id} - Ticket validado")

def main():
    support_system = SupportSystem()

    while True:
        support_system.display_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            description = input("Ingrese la descripción del ticket: ")
            support_system.create_ticket(description)
        elif choice == "2":
            support_system.review_tickets()
        elif choice == "3":
            support_system.validate_tickets()
        elif choice == "4":
            print("Saliendo del sistema de soporte.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "_main_":
    main()