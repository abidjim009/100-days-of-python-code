class Library:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def info(self):
        print(f"Library Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

    def check_availability(self, book_title):
        # This is a placeholder for actual availability check logic
        if len(self.name) > 0 and len(self.address) > 0:
            print(f"The book '{book_title}' is available in the library.")
        else:
            print(f"The book '{book_title}' is not available in the library.")


# Example usage:
a = Library("City Library", "123 Main St", "123-456-7890")
a.info()
a.check_availability("Python Programming")
