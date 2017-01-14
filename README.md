Aaron's Pig Latin Translation Microservice

Python/Flask-based microservice that translates arbitrary English text into Pig Latin.

It requires a GET request with a parameter named 'msg' that includes the URL-encoded text.


INSTALL:

  1. System Prerequisites
      * python
      * python-pip
      * python-virtualenv
  2. create dir
      ~~~~
      mkdir vicpig
      cd vicpig
      ~~~~
  3. create virtualenv
      ~~~~
      virtualenv venv
      . venv/bin/activate
      ~~~~
  4. install requirements
      ~~~~
      pip install -r vicpig/requirements.txt
      ~~~~
  5. clone source
      ~~~~
      git clone https://github.com/aaroncutchin/vicpig.git
      ~~~~
  6. run the app
      ~~~~
      export FLASK_APP=vicpig/vicpig.py
      FLASK_DEBUG=1 flask run
      ~~~~

USAGE:

You can now test the app with various strings like: 

      ~~~~
      curl -G "http://localhost:5000/translate/" --data-urlencode 'msg=Hello, world!'
      ~~~~


