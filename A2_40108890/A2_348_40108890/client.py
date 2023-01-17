'''
Assignment 2 - COMP348
Quan Nguyen - 40108890
'''

import socket


host_number = "127.0.0.1"
port_id = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host_number, port_id))

    default_choice = False
    while not default_choice:
        client_choice = input(
            """Python DB Menu
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone
7. Print report
8. Exit
Select: """)
        request = ""

        if not client_choice.isdigit():
            print("Invalid integer!")
            continue
        client_choice = int(client_choice)


        if client_choice == 1:
            name = input("Enter a name: ")

            request = str(client_choice) + "&" + name
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))
        elif client_choice == 2:

            new_str = ""
            new_name_str = input("Enter a name: ")
            new_str += new_name_str + "|"

            new_age_str = input("Enter the new age: ")
            new_str += (str(new_age_str) + "|")

            new_address_str = input("Enter the new address: ")
            new_str += (new_address_str + "|")

            new_phone_num_str = input("Enter the new phone number: ")
            new_str += new_phone_num_str

            request = str(client_choice) + "&" + new_str
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif client_choice == 3:

            str_3 = input("Enter the name to delete from the database: ")
            request = str(client_choice) + "&" + str_3
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif client_choice == 4:
            str_4 = input("Enter name to update the age: ")
            new_age = input("Enter new age: ")

            request = str(client_choice) + "&" + str_4 + "&" + new_age
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif client_choice == 5:
            str_5 = input("Enter name to update the address: ")
            new_address = input("Enter new address: ")

            request = str(client_choice) + "&" + str_5 + "&" + new_address
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))
        elif client_choice == 6:
            str_6 = input("Enter name to update the phone number: ")
            new_phone_num = input("Enter new phone number: ")

            request = str(client_choice) + "&" + str_6 + "&" + new_phone_num
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif client_choice == 7:
            request = str(client_choice)
            s.send(bytes(request, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif client_choice == 8:
            print("Program terminated!")
            default_choice = True
            s.close()

        else:
            print("INVALID INPUT! TRY AGAIN!")
