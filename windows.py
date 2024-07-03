import subprocess
import os
import json
import sys
import time

# TheHive Wimdows Controller 
# 


# Return Codes 
# -1 -> Config File Not Found 



CONFIG_PATH = "config" + os.path.sep + "config.json"


def p_error(msg):
    print(f"[ERROR]: {msg}")

def p_info(msg):
    print(f"[INFO]: {msg}")

def p_warn(msg):
    print(f"[WARNING]: {msg}")   


def printHelp():
    currentFile = sys.argv[0]
    print("\n")
    print(f"--- TheHive Windows Controller Help Menu ---\n")
    print(f"python {currentFile} --help\t\t\t:open this menu and exit")
    print(f"python {currentFile} --check-commands\t\t:check required command status")
    print(f"python {currentFile} --install-pip-packaget\t:install required pip packagets")
    print(f"python {currentFile} --wizard\t\t\t:otomatik indirme yardımcısı")

    print("\n")




def executeSelf(param:str):
    _commands_is = [str(sys.executable.replace(os.sep, os.path.sep)), "windows.py", param]

    subprocess.run(_commands_is,stdout=sys.stdout,shell=True)
    

def startHive():
    _commands_is = [str(sys.executable.replace(os.sep, os.path.sep)), "main.py"]
    subprocess.run(_commands_is,shell=True, stdout=sys.stdout)



def checkCommands(cmd:str) -> None:

    _commands_is = ["powershell","Get-Command", cmd ,"-ErrorAction", "SilentlyContinue"]
    _err = ""
    _std_out = ""
    commandStatus = subprocess.run(_commands_is,capture_output=True,shell=True)
    
    if commandStatus.returncode != 0:
        p_error(f"{cmd} not found, install and add path !")
        print(commandStatus.returncode)
        sys.exit(1)
    else:
        p_info(f"{cmd} detected the system, good...")



if not os.path.exists(CONFIG_PATH):
    p_error(f"Config file not found: {CONFIG_PATH}")
    sys.exit(-1)
    

with open(CONFIG_PATH, "r") as configFile:
    JsonData = json.loads(configFile.read())
    

p_info(f"Reading Config File: {CONFIG_PATH}")


WindowsBinaryPath = "binary" + os.path.sep + "windows" + os.path.sep

# reference!
# -d -p 5432:$db_port -e POSTGRES_PASSWORD=$db_password $container_package_name -N $postgre_max_connections




# reference
#    docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -c "CREATE DATABASE \"$db_name\";"

# reference
#     docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -d "$db_name" -f $CONTAINER_SCHEMA_PATH





def installPackage(package:str) -> None:
    _command = ["powershell", "python", "-m", "pip", "install", package]
    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error(f"indirme işlemi başarısız oldu!\t{package}")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
    else:
        p_info(f"Başarıyla indirildi:\t{package}")

def installPipPackaget():
    
    
    
    
    with open("requirements.txt", "r",encoding="utf-8") as pipFile:
        p_info("pip paketleri kuruluyor...")
        for line in pipFile:
            line = line.strip()
            
            if line == "insightface":
                p_warn(f"Daha sonra indirilecek:\t{line}")
                continue
            
            installPackage(line)
            
        
    
    p_info("Gereksiz kaynak harcanmasın diye önceden derlenmiş paketlere geçildi...")

    for packaget in os.listdir(WindowsBinaryPath):
        if packaget.endswith(".whl"):
            installPackage(package=str(WindowsBinaryPath+packaget))

    p_info("işlem tamamlandı")



if len(sys.argv) < 2:
    printHelp()
    sys.exit(1)


currentParam = sys.argv[1]



if currentParam.lower() == "--help":
    printHelp()
    sys.exit(0)
    

    
elif currentParam == "--start-hive":
    startHive()
    
    
elif currentParam =="--install-pip-packaget":
    installPipPackaget()
    



elif currentParam == "--wizard":
    p_info("Otomatik indirme başlatılıyor...")
    executeSelf("--check-commands")
    executeSelf("--install-pip-packaget")
    executeSelf("--start-hive")
    
    
elif currentParam == "--check-commands":
    p_info("Checking Required Commands ...")
    checkCommands("pip")
    sys.exit(0)



