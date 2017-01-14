Aaron's Pig Latin Translation Microservice

## BASIC DEV INSTALL

This will host the app at http://localhost:5000/translate

1. System Prerequisites

  * python
  * python-pip
  * python-virtualenv
  * curl (if you want to test from the command line)

2. create dir

        mkdir vicpig
        cd vicpig

3. create virtualenv

        virtualenv venv
        . venv/bin/activate

4. clone source

        git clone https://github.com/aaroncutchin/vicpig.git

5. install requirements

        pip install -r vicpig/requirements.txt

6. run the app

        export FLASK_APP=vicpig/vicpig.py
        FLASK_DEBUG=1 flask run



## UBUNTU 16.04 / NGINX / SYSTEMD / GUNICORN INSTALL:


Assumes the following configuration:
* ubuntu 16.04
* standard nginx, running as www-data:www-data
* app located at /var/www/html/vicpig
* hosting on port 80, no name-based virtual hosting

Pretty much everything here must be done as root, so you might as well just 'sudo su -'

1. Install system packages

        apt-get install python python-pip python-virtualenv libpython2.7-dev nginx

2. prepare application dir

        mkdir /var/www/html/vicpig
        cd /var/www/html/vicpig
        virtualenv venv
        . venv/bin/activate
        git clone https://github.com/aaroncutchin/vicpig.git
        pip install -r vicpig/requirements.txt
        chown -R www-data:www-data  /var/www/html/vicpig

3. create nginx site config file (/etc/nginx/sites-available/vicpig.conf):

        server {
            listen 80;
            server_name <INSERT_SYSTEM_HOSTNAME_OR_IP_ADDRESS_HERE>;
            location / {
                include proxy_params;
                proxy_pass http://unix:/var/www/html/vicpig/vicpig.gunicorn.wsgi.sock;
            }
        }

4. symlink to sites-enabled

        ln -s /etc/nginx/sites-available/vicpig.conf /etc/nginx/sites-enabled/vicpig.conf

5. create systemd service file (/etc/systemd/system/vicpig.service)

        [Unit]
        Description=Gunicorn WSGI instance to serve vicpig
        After=network.target
        [Service]
        User=www-data
        Group=www-data
        WorkingDirectory=/var/www/html/vicpig/vicpig
        Environment="PATH=/var/www/html/vicpig/venv/bin"
        ExecStart=/var/www/html/vicpig/venv/bin/gunicorn --workers 3 --bind unix:/var/www/html/vicpig/vicpig.gunicorn.wsgi.sock -m 007 vicpig:app
        [Install]
        WantedBy=multi-user.target  

6. reload systemd and start the Gunicorn/vicpig service

        systemctl daemon-reload
        systemctl start vicpig

7. restart nginx

        systemctl restart nginx

8. you should now be able to use the service at

        http://<system_hostname_or_ip_address>/translate/?msg=foo




UNIT TESTS:

You can run unit tests by invoking the virtual environment as above, and executing pytest.


