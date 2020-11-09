import os
from menu_lvm import *
from functionality import *
from local import *
from TeamInfo import *
from AWS_Menu import *
from remote import *
from docker import *
from ansible_menu import *
from hadoop_menu import *

while (1) :
        os.system("tput setaf 1")
        print("\t\t\t Hii How Can I help You")
        os.system("tput setaf 7")
        print("\t\t--------------------------------------------------")
        TeamMember()

        print()
        print()
        selection()
        inp = input("Enter Where You Want To Perform Operation :- ")
        if (("Mine" in inp) or ("mine" in inp) or ("MINE" in inp) or ("local" in inp) or ("Local" in inp) or ("LOCAL" in inp)) :

            while (1):
                mainMenu()
                os.system("tput setaf 7")

                ch1 = input("Enter Your Choice : ")
                if (("exit" in ch1) or ("quit" in ch1) or ("Exit" in ch1) or ("Quit" in ch1)) :
                    print("""

                        You exit For Current Menu

                    """)
                    break

                elif ((("bas" in ch1) or ("Bas" in ch1)) and (("oper" in ch1) or ("Oper" in ch1) or ("OPER" in ch1))) :

                    local_basicOperation()
                    os.system("tput setaf 7")


                elif ((("pack" in ch1) or ("Pack" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    local_packManagement()
                    os.system("tput setaf 7")

                elif ((("per" in ch1) or ("Per" in ch1) or ("PER" in ch1))) :
                    local_permission()
                    os.system("tput setaf 7")


                elif ((("user" in ch1) or ("User" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    local_userManagement()
                    os.system("tput setaf 7")


                elif ((("net" in ch1) or ("Net" in ch1))) :
                    local_Networking()
                    os.system("tput setaf 7")


                elif ((("serv" in ch1) or ("Serv" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    local_serviceManagement()
                    os.system("tput setaf 7")


                elif ((("Docker" in ch1) or ("docker" in ch1) or ("DOCKER" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    dockerManagement()
                    os.system("tput setaf 7")


                elif ((("aws" in ch1) or ("AWS" in ch1) or ("Aws" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    aws()
                    os.system("tput setaf 7")

                elif ((("lvm" in ch1) or ("LVM" in ch1) or ("Lvm" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    lvm()
                    os.system("tput setaf 7")
 
                elif ((("hadoop" in ch1) or ("hado" in ch1) or ("HADOOP" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    hadoop()
                    os.system("tput setaf 7")

                elif ((("ansible" in ch1) or ("ansi" in ch1) or ("ANSIBLE" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    ansible()
                    os.system("tput setaf 7")

                    
                else :
                    print("No Match Found Please Try Again")

            os.system("tput setaf 7")
            a = input("For Return to main menu Press 1 and For exit Type exit or quit "  )
            if (("exit" in a) or ("quit" in a) or ("Exit" in a) or ("Quit" in a)) :
                print("""

                    You exit From Current Menu

                """)
                break
            os.system("clear")
        elif (("rem" in inp) or ("Rem" in inp) or ("REM" in inp) or ("other" in inp) or ("Other" in inp) or ("OTHER" in inp)) :
            print("You Select Remote System")
            print("Enter Only working IP")
            ip_add = input("Enter the ip Address of Remote System: - ")
            print("""
                    Through ssh key-gen you don't need to enter remote password
                    again and again
                """)
            key = input("Have you Generate ssh-keygen in our system (yes/no) :- ")
            if (("no" in key) or ("No" in key) or ("NO" in key) or ("not" in key) or ("Not" in key) or ("NOT" in key)) :
                os.system("ssh-keygen")
                os.system("ssh-copy-id root@{}".format(ip_add))

            elif ((("yes" in key) or ("Yes" in key) or ("YES" in key))) :
                os.system("ssh-copy-id root@{}".format(ip_add))
            else :
                print("No Match Found Please Try Again")
            while (1):
                mainMenu()
                os.system("tput setaf 7")



                ch1 = input("Enter Your Choice : ")
                if (("exit" in ch1) or ("quit" in ch1) or ("Exit" in ch1) or ("Quit" in ch1)) :
                    print("""

                        You exit For Current Menu

                    """)
                    break

                elif ((("bas" in ch1) or ("Bas" in ch1)) and (("oper" in ch1) or ("Oper" in ch1) or ("OPER" in ch1))) :

                    remote_basicOperation(ip_add)
                    os.system("tput setaf 7")


                elif ((("pack" in ch1) or ("Pack" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    remote_packManagement(ip_add)
                    os.system("tput setaf 7")

                elif ((("per" in ch1) or ("Per" in ch1) or ("PER" in ch1))) :
                    remote_permission(ip_add)
                    os.system("tput setaf 7")

                elif ((("user" in ch1) or ("User" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :


                    remote_userManagement(ip_add)
                    os.system("tput setaf 7")


                elif ((("net" in ch1) or ("Net" in ch1))) :

                    remote_Networking(ip_add)
                    os.system("tput setaf 7")


                elif ((("serv" in ch1) or ("Serv" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :

                    remote_serviceManagement(ip_add)
                    os.system("tput setaf 7")


                elif ((("Docker" in ch1) or ("docker" in ch1) or ("DOCKER" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :

                    remote_dockerManagement(ip_add)
                    os.system("tput setaf 7")

                elif ((("aws" in ch1) or ("AWS" in ch1) or ("Aws" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    aws(ip_add)
                    os.system("tput setaf 7")

                else :
                    print("No Match Found Please Try Again")

            os.system("tput setaf 7")
            a = input("For Return to main menu Press 1 and For exit Type exit or quit: "  )
            if (("exit" in a) or ("quit" in a) or ("Exit" in a) or ("Quit" in a)) :
                print("""

                    You exit For Current Menu

                """)
                break
            os.system("clear")


        elif (("exit" in inp) or ("quit" in inp) or ("Exit" in inp) or ("Quit" in inp)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")
