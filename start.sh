sudo apt update
sudo apt install python3-virtualenv -y
sudo apt install python3 python3-pip python3-virtualenv nginx curl

git clone https://github.com/bvelush/aws-practice.git apiv1/
cd apiv1
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt


