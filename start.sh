sudo apt update
sudo apt install python3-virtualenv -y
sudo apt install python3 python3-pip python3-virtualenv nginx curl

git clone https://github.com/bvelush/aws-practice.git apiv1/
cd apiv1
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt

sudo cp config/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp config/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo cp config/default /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
