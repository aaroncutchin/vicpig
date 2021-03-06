Aaron's Pig Latin Translation Microservice

Python/Flask-based microservice that translates arbitrary English text into Pig Latin.

It requires a GET request with a parameter named 'msg' that includes the URL-encoded text.


USAGE:

You can test the app with various curl command like:

      ```
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=Hello, world!'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=numbers like 15'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=possessives like Alan\'s'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=Capitalized Words'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=ALL CAPS'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg="quoted strings"'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg="quotes", followed by commas'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg="commas", followed by quotes'
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg=Sentences with commas, oxford commas, and periods.'
      ```

You can also put text in a plain text file (file.txt), and translate it with the following curl command. This would be useful for multi-sentence or multi-paragraph text.

      ```
      curl -G 'http://localhost:5000/translate/' --data-urlencode 'msg@file.txt'
      ```

