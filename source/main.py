#!/usr/bin/python3

import modules.system_info as system_info
import modules.bibliography as bibliography
import os,sys

def system_info_menu():
    print("System Info Menu:")
    print("1. Print All Available System Information")
    print("2. Print CPU Information")
    print("3. Print Memory Usage")
    print("4. Print Disk Usage")
    print("5. Back to Main Menu")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == "1":
        os.system('clear')
        system_info.print_system_info()
    elif choice == "2":
        os.system('clear')
        system_info.print_cpu_info()
    elif choice == "3":
        os.system('clear')
        system_info.print_memory_info()
    elif choice == "4":
        os.system('clear')
        system_info.print_disk_usage()
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")

    system_info_menu()

def user_menu():
    print("User Menu:")
    print("1. System Info")
    print("2. Print Bibliography")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        os.system('clear')
        system_info_menu()
    elif choice == "2":
        os.system('clear')
        bibliography.credit_me()
    elif choice == "3":
        print("Exiting program...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")

while True:
    user_menu()