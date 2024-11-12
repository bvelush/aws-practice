sudo apt install python3-virtualenv -y

git clone https://github.com/bvelush/aws-practice.git apiv1/
cd apiv1
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt


