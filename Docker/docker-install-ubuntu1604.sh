# Docker installation script for Ubuntu 16.04 (Xenial)
#Crypto-Gemmy
 
YELL='\033[1;33m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

echo -e "${YELL}########## ==> ${WHITE}Running Update${NC}"
sudo apt-get update -y

echo -e "${YELL}########## ==> ${WHITE}Running Upgrade${NC}"
sudo apt-get upgrade -y

echo -e "${YELL}########## ==> ${WHITE}Installing APT HTTPS Support packages${NC}"
sudo apt-get install -y apt-transport-https ca-certificates

echo -e "${YELL}########## ==> ${WHITE}CURL repo keys${NC}"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

echo -e "${YELL}########## ==> ${WHITE}Adding Repo URL${NC}"
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

echo -e "${YELL}########## ==> ${WHITE}Running Update to get Docker packages${NC}"
sudo apt-get update -y

echo -e "${YELL}########## ==> ${WHITE}Installing Docker${NC}"
sudo apt-get install -y docker-ce

echo -e "${YELL}########## ==> ${WHITE}Checking Status${NC}"
sudo systemctl status docker | grep Active