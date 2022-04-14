import os
from MenuAuthentification import authentifier_choix
from Chatroom import chatroom_menu
from MenuEncodage import encodage_menu
from MenuHachage import hachage_menu
from MenuCrackage import crackage_menu
from MenuSymetrique import symetrique_menu
from MenuAsymetrique import asymetrique_menu

def main():
    os.system('cls')
    print("__________                     __           __      _________  _________.___")
    print("\______   \_______   ____     |__|  ____  _/  |_   /   _____/ /   _____/|   |")
    print(" |     ___/\_  __ \ /  _ \    |  |_/ __ \ \   __\  \_____  \  \_____  \ |   |")
    print(" |    |     |  | \/(  <_> )   |  |\  ___/  |  |    /        \ /        \|   |")
    print(" |____|     |__|    \____//\__|  | \___  > |__|   /_______  //_______  /|___|")
    print("                 	  \______|     \/                 \/         \/")
    print()

    utilisateur = authentifier_choix()
    choix = ''
    while True:
        print("__________                     __           __      _________  _________.___")
        print("\______   \_______   ____     |__|  ____  _/  |_   /   _____/ /   _____/|   |")
        print(" |     ___/\_  __ \ /  _ \    |  |_/ __ \ \   __\  \_____  \  \_____  \ |   |")
        print(" |    |     |  | \/(  <_> )   |  |\  ___/  |  |    /        \ /        \|   |")
        print(" |____|     |__|    \____//\__|  | \___  > |__|   /_______  //_______  /|___|")
        print("                 	  \______|     \/                 \/         \/")
        utilisateur.afficher()
        print()
        print("---------------Menu Principal--------------")
        print("1- Encodage et Decodage d'un message")
        print("2- Hachage d'un message")
        print("3- Crackage d'un message haché")
        print("4- Chiffrement et déchiffrement symétrique d'un message")
        print("5- Chiffrement et déchiffrement asymétrique d'un message")
        print("6- Chatroom")
        print("7- Quitter")
        print("-------------------------------------------")
        choix = input("Donner le numero du choix:\n> ")
        if (choix == '1'):
            encodage_menu()
        if (choix == '2'):
            hachage_menu()
        if (choix == '3'):
            crackage_menu()
        if (choix == '4'):
            symetrique_menu()
        if (choix == '5'):
            asymetrique_menu()
        if (choix == '6'):
            chatroom_menu(utilisateur)
        if (choix == '7'):
            exit()


if __name__ == "__main__":
    main()
