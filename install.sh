echo "====================== update system ======================"
sudo apt -y update
sudo apt -y upgrade

echo "================ Install python3 🐍 ======================="

sudo apt -y install python3
sudo apt -y install python3-pip

echo "=============== install openssh-server ===================="
sudo apt -y install openssh-server

echo "=========== install net-tools ============================="
sudo apt -y install net-tools 
