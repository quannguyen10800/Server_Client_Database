'''
Assignment 2 - COMP348
Quan Nguyen - 40108890
'''

import socket


host_id = "127.0.0.1"   #local host
port_number = 9999  #port number 9999


#open file
f = open("data.txt", "r")
db = []
index = 0


for i in f:

    i = i.replace("\n", "")

    split = i.split("|")
    db.append(tuple(split))

f.close()


#connecting to a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host_id, port_number))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Status connected {address}")

        while True:
            request = connection.recv(1024)
            request = request.decode("utf-8")

            if request == "":
                client_choice = 0
            else:
                request_list = request.split("&")
                client_choice = int(request_list[0])

            notice_stop = False

            if client_choice == 1:
                input_str = str(request_list[1])

                detector_name = False
                for i in db:
                    if input_str == i[0]:
                        detector_name = True
                        information_client = ""
                        for j in i:
                            information_client += j + "|"

                        information_client = "Server Response: " + str(information_client[:len(information_client) - 1]) + "\n"
                        connection.send(bytes(information_client, 'utf-8'))

                if not detector_name:
                    name_exist = bytes("Server Response: " + input_str + " NOT FOUND!", 'utf-8')
                    connection.send(name_exist)
                not_stopping = False

            elif client_choice == 2:
                input_str = str(request_list[1])
                new_customer_info = input_str.split("|")
                detector_name = False
                for i in db:
                    if new_customer_info[0] == i[0]:
                        detector_name = True

                if detector_name:
                    bad_resp = "Already existed\n"
                    connection.send(bytes(bad_resp, 'utf-8'))

                else:
                    db.append(tuple(new_customer_info))
                    file_append = open("data.txt", "a")
                    file_append.write("\n" + input_str)
                    file_append.close()
                    res_2_ok = "Succesfully written in DB"
                    connection.send(bytes(res_2_ok, 'utf-8'))

            elif client_choice == 3:
                input_str = str(request_list[1])
                for i in db:
                    if input_str == i[0]:
                        db.remove(i)

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:
                            for line in input:
                                if input_str not in line.strip("\n"):
                                    replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        res_3_ok = "Successfully deleted " + input_str
                        connection.send(bytes(res_3_ok, 'utf-8'))
                        notice_stop = True
                        break
                    if notice_stop:
                        break

                if index == len(db) - 1:
                    reply = "DOES NOT EXIST"
                    connection.send(bytes(reply, 'utf-8'))




            elif client_choice == 4:
                input_str = str(request_list[1])
                age = request_list[2]
                index = -1
                for i in db:
                    index += 1
                    if input_str == str(i[0]):
                        info_as_list = list(db[index])
                        info_as_list[1] = age
                        info_as_tuple = tuple(info_as_list)

                        db[index] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:

                            for line in input:

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        reply = "UPDATED!"
                        connection.send(bytes(reply, 'utf-8'))
                        notice_stop = True
                        break
                    if notice_stop:
                        break

                if index == len(db) - 1:
                    reply = "NOT FOUND!"
                    connection.send(bytes(reply, 'utf-8'))


            elif client_choice == 5:
                input_str = str(request_list[1])

                new_address = request_list[2]
                index = -1
                for i in db:
                    index += 1
                    if input_str == str(i[0]):
                        info_as_list = list(db[index])
                        info_as_list[2] = new_address
                        info_as_tuple = tuple(info_as_list)

                        db[index] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:

                            for line in input:

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        reply = "UPDATED!"
                        connection.send(bytes(reply, 'utf-8'))
                        notice_stop = True
                        break
                    if notice_stop:
                        break

                if index == len(db) - 1:
                    reply = "NOT FOUND"
                    connection.send(bytes(reply, 'utf-8'))

            elif client_choice == 6:
                input_str = str(request_list[1])
                new_phone_num = str(request_list[2])
                index = -1

                for i in db:
                    index += 1
                    if input_str == str(i[0]):
                        info_as_list = list(db[index])
                        info_as_list[3] = new_phone_num
                        info_as_tuple = tuple(info_as_list)

                        db[index] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]
                        new_info_str += "\n"
                        replacement_file_text = ""

                        with open("data.txt", "r") as input:

                            for line in input:

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)
                            print("Option 6")
                            print(db)
                        reply = "UPDATED!"
                        connection.send(bytes(reply, 'utf-8'))
                        notice_stop = True
                        break
                    if notice_stop:
                        break

                if index == len(db)-1:
                    reply = "NOT FOUND"
                    connection.send(bytes(reply, 'utf-8'))

            elif client_choice == 7:

                sort_database = sorted(db)
                txt = " Python DB contents \n"
                for i in sort_database:
                    for j in i:
                        txt += j + "|"
                    txt = txt[:len(txt) - 1]
                    txt += "\n"

                connection.send(bytes(txt, 'utf-8'))

            elif client_choice == 8:
                print()
