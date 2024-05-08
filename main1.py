from concrete_creators import ConcreteCreatorA, ConcreteCreatorB
from creator import Creator

def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())

    print("\nApp: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
