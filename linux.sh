#!/usr/bin/env bash


# TheHive cli controller version 1.0
# Developed By: Prime Security 2020 - 2024
 


# color codes 
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'

#source "/etc/os-release"

# global const varables 
CONFIG_PATH="config/config.json"
GET_TARGET=$1
SCRIPT_VERSION="1.0"
PIP_PACKAGET_FILE="requirements.txt"


# print functions 
p_error(){
    printf "$red[-]$reset $1 \n"
}

p_info(){
    printf "$green[+]$reset $1 \n"
}

# command checker 
check_command(){
    command -v $1 > /dev/null
    if [[ "$?" != "0" ]]; then
        p_error "$1 Not Found, install $1 and try run this script!"
        exit 1
    else
        p_info "$1 detected in system\tOK..."
    
    fi 

}

# check all commands 
check_reqiered_commands(){

    p_info "CHECKING REQUIRED PACKAGETS"
    printf "\n"
    
    check_command "jq"
    check_command "python3"
    check_command "pip3"
    check_command "cat"
    check_command "make"
    check_command "cmake"
    check_command "gcc"
    check_command "g++"
    check_command "sed"
    printf "\n"

}

# help menu printer 
print_help_exit(){
    printf "\n"
    
    printf "$blue<-[ Help Menu ]->\n$reset"  
    p_info "Script Version:\t$SCRIPT_VERSION"
    printf "\n"

    printf "COMMANDS:\n"
    
    printf "$0 --check-commands\t\t:Check the required commands status\n"
    printf "$0 --install-pip-packagets\t:Install Required pip packagets\n"
    printf "$0 --wizard\t\t\t:Otomatik indirme aracı\n"
    printf "$0 --help/-h\t\t\t:Open this menu\n"
    printf "\n"
    exit 0

}

# reading conf file 
# conf file type    : json 
# bash json parser  : jq
p_info "Reading Config File:\t$CONFIG_PATH"
db_name=$(cat $CONFIG_PATH | jq ".database_config.database")
db_username=$(cat $CONFIG_PATH | jq ".database_config.user")
db_password=$(cat $CONFIG_PATH | jq ".database_config.password")
db_hostname=$(cat $CONFIG_PATH | jq ".database_config.host")
db_port=$(cat $CONFIG_PATH | jq ".database_config.port")


# parse json data with sed rmove " chars
db_name=$(echo $db_name | sed 's/"//g')
db_username=$(echo $db_username | sed 's/"//g')
db_password=$(echo $db_password | sed 's/"//g')
db_hostname=$(echo $db_hostname | sed 's/"//g')
db_port=$(echo $db_port | sed 's/"//g')

# set container name and max postgreSQL connection 
container_name="$db_name-postgresql-docker"
postgre_max_connections=200
container_package_name="postgres"   # container package name


# parse the argumant and execute the protocol 


# stop container for user 
if [[ "$1" == "--start-hive" ]]; then
    printf "\n"
    printf "$blue<-[ Starting TheHive ]->\n$reset"  
    printf "\n"
    sleep 1

    python3 main.py

elif [[ "$1" == "--install-model" ]]; then
    printf "\n"
    printf "$blue<-[ Installing Insightface Model ]->\n$reset"  
    printf "\n"
    sleep 1

    python3 hivelibrary/install_insightface_model.py
    if [[ "$?" != "0" ]]; then
        p_error "Failed to install insightface model..."
        exit 1

    else
        p_info "OK..."
    
    fi 


elif [[ "$1" == "--wizard" ]]; then
    printf "\n"
    printf "$blue<-[ Otomatik İndirme Aracı Başlatılıyor ]->\n$reset"  
    printf "\n"

    checkRoot=1

    if [[ "$checkRoot" == "1" && "$UID" == "0" ]] ;then
        p_error "Otomatik indirme yardımcısı root olarak çalışamaz! Gerekli oldugu zaman sudo parolası ister!"
        printf "\n"
        printf "Eğer sistemi root olarak kullanıyorsanız 347. satırdaki \$checkRoot=1 değerini \$checkRoot=0 yapınız."
        exit 1
    fi

    bash ./linux.sh --install-pip-packagets

    bash ./linux.sh --start-hive






elif [[ "$1" == "--install-pip-packagets" ]]; then
    printf "\n"
    printf "$blue<-[ Starting pip package installing ]->\n$reset"  
    printf "\n"
    sleep 1
    p_info "Using file:\t$PIP_PACKAGET_FILE"

    while read current_packaget
    do
        p_info "Installing packaget:\t$current_packaget"
        python3 -m pip install $current_packaget
    done < $PIP_PACKAGET_FILE

    exit 0


# manuel command check for user 
elif [[ "$1" == "--check-commands" ]]; then
    check_reqiered_commands

# handle --help 
elif [[ "$1" == "--help" || "$1" == "-h" ]]; then
    print_help_exit
    

# invalid arg handler 
else

    p_error "Invalid args!"
    print_help_exit

fi
