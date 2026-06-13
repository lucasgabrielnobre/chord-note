import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    with open("logo.txt", "r") as file:
        logo = file.read() 
        print(logo)
    print("Gerenciador de Acordes em Musica")

if __name__ == "__main__":
    main()
