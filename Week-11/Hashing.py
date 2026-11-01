#T.Naga Siddhardha
SIZE = 10

# ---------------- SEPARATE CHAINING ----------------

class SeparateChaining:
    def __init__(self):
        self.table = [[] for _ in range(SIZE)]

    def insert(self, key):
        index = key % SIZE
        if key not in self.table[index]:
            self.table[index].append(key)
        print("Inserted successfully.")

    def search(self, key):
        index = key % SIZE
        if key in self.table[index]:
            print("Element found.")
        else:
            print("Element not found.")

    def delete(self, key):
        index = key % SIZE
        if key in self.table[index]:
            self.table[index].remove(key)
            print("Element deleted.")
        else:
            print("Element not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# ---------------- LINEAR PROBING ----------------

class LinearProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] == key:
                print("Duplicate element.")
                return

            if self.table[pos] is None:
                self.table[pos] = key
                print("Inserted successfully.")
                return

        print("Hash table is full.")

    def search(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                print("Element found.")
                return

        print("Element not found.")

    def delete(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Element deleted.")
                return

        print("Element not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# ---------------- QUADRATIC PROBING ----------------

class QuadraticProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] == key:
                print("Duplicate element.")
                return

            if self.table[pos] is None or self.table[pos] == "DELETED":
                self.table[pos] = key
                print("Inserted successfully.")
                return

        print("No available position found.")

    def search(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                print("Element found.")
                return

        print("Element not found.")

    def delete(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Element deleted.")
                return

        print("Element not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# ---------------- MAIN PROGRAM ----------------

while True:
    print("\n--- HASHING OPERATIONS ---")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Exiting...")
        break

    if choice not in [1, 2, 3]:
        print("Invalid choice.")
        continue

    if choice == 1:
        h = SeparateChaining()
    elif choice == 2:
        h = LinearProbing()
    else:
        h = QuadraticProbing()

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Back to Main Menu")

        op = int(input("Enter operation: "))

        if op == 1:
            key = int(input("Enter key: "))
            h.insert(key)

        elif op == 2:
            key = int(input("Enter key: "))
            h.search(key)

        elif op == 3:
            key = int(input("Enter key: "))
            h.delete(key)

        elif op == 4:
            h.display()

        elif op == 5:
            break

        else:
            print("Invalid operation.")
