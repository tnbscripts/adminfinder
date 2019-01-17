import requests,platform,sys,os

def banner():
    print("""
 _______  _______  ______   _______    ______              _______           _______           _______
(  ____ \(  ___  )(  __  \ (  ____ \  (  ___ \ |\     /|  (  ____ \|\     /|(  ____ )|\     /|(  ____ \\
| (    \/| (   ) || (  \  )| (    \/  | (   ) )( \   / )  | (    \/( \   / )| (    )|| )   ( || (    \/
| |      | |   | || |   ) || (__      | (__/ /  \ (_) /   | |       \ (_) / | (____)|| |   | || (_____
| |      | |   | || |   | ||  __)     |  __ (    \   /    | |        \   /  |     __)| |   | |(_____  )
| |      | |   | || |   ) || (        | (  \ \    ) (     | |         ) (   | (\ (   | |   | |      ) |
| (____/\| (___) || (__/  )| (____/\  | )___) )   | |     | (____/\   | |   | ) \ \__| (___) |/\____) |
(_______/(_______)(______/ (_______/  |/ \___/    \_/     (_______/   \_/   |/   \__/(_______)\_______)                                                                                                       
""")
def help():
    print(f"Usage is:\n      {sys.argv[0]} <url> <option>")
    print(f"Options:\n      admin - finder admin directories.")
    print(f"      folder - finder any other folder.")
    print(f"Ex:\n      {sys.argv[0]} https://alvo.com.br admin")

def admFind(url):
    print("[-]STARTING[-]")
    try:
        with open("admin.txt") as file:
            for i in file.readlines():
                directory = i.strip()
                print(f"[-] Testando {directory}")
                if url[-1] == "/":
                    full_path = (url+directory)
                else:
                    full_path = (url+"/"+directory)
                user_agent = {"User-Agent":"Googlebot"}
                r = requests.get(full_path, headers=user_agent)
                if str(r.status_code) != "404":
                    if str(r.status_code) == "200":
                        print(f"[*] {full_path} => Size[{len(r.text)}] Code[{r.status_code}]")
                        perg = str(input("Deseja continuar:[Y/n]"))
                        if perg == "" or perg == "Y":
                            continue
                        else:
                            break    
                            
                    print(f"[!] {full_path} => Size[{len(r.text)}] Code[{r.status_code}]")
                    perg = str(input("Deseja continuar:[Y/n]"))
                    if perg == "" or perg == "Y":
                        continue
                    else:
                        break
    except:
        print("Erro ao achar ou abrir wordlist.")


def folderFind(url):
    print("[-]STARTING[-]")
    try:
        with open("folders.txt") as file:
            for i in file.readlines():
                directory = i.strip()
                if url[-1] == "/":
                    full_path = (url+directory)
                else:
                    full_path = (url+"/"+directory)
                user_agent = {"User-Agent":"Googlebot"}
                r = requests.get(full_path, headers=user_agent)
                if str(r.status_code) != "404":
                    if str(r.status_code) == "200":
                        print(f"[*] {full_path} => Size[{len(r.text)}] Code[{r.status_code}]")
                    print(f"[!] {full_path} => Size[{len(r.text)}] Code[{r.status_code}]")
    except:
        print("Erro ao achar ou abrir wordlist.") 


def redirect(url,option):
    if option == "admin":
        admFind(url)
    if option == "folder":
        folderFind(url)


if len(sys.argv) < 3:
    banner()
    help()
    exit()

if platform.system() == "windows" or platform.system() != "linux":
    try:
        os.system("cls")
        os.system("color a")
    except:
        os.system("clear")
#Script começa aqui
banner()
url = str(sys.argv[1])
if str(url[0:8]) != "https://":
    if  str(url[0:7]) != "http://":
        print("Enter http:// or https://")
        exit()
    else:
        pass
else:
    pass
option = str(sys.argv[2])
redirect(url, option)