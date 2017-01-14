from flask import Flask, request
import flask_nicely

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug=True)

CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
VOWELS = 'aeiouAEIOU'
LETTERS = CONSONANTS + VOWELS

@app.route( '/translate/', methods=['GET'] )
@flask_nicely.nice_json
def translate():
	message = request.args.get('msg')
	if message is None:
		return ''
	else:
		term_list = message.split()
		pigified_term_list = pigify_term_list( term_list )
		pigified_message = " ".join( pigified_term_list )
	return pigified_message


def pigify_term_list( term_list ):
	##  A "TERM" IS A SPACE-DELIMITED ELEMENT OF THE MESSAGE, AS RETURNED BY SPLIT
	##  IT MIGHT CONTAIN LEADING OR TRAILING PUNCTUATION, LIKE A QUOTED WORD OR PHRASE INSIDE A SENTENCE,
	##  OR A WORD WITH A TRAILING COMMA OR PERIOD OR BOTH
	##  A "WORD" IS THE ACTUAL WORD SEPARATED FROM IT'S LEADING OR TRAILING PUNCTUATION
	pigified_term_list = []
	for term in term_list:
		##  DON'T PIGIFY TERMS THAT CONTAIN NUMBERS
		if any(char.isdigit() for char in term):
			pigified_term = term
		##  DON'T PIGIFY TERMS THAT DON'T CONTAIN LETTERS (LIKE PUNCTUATION WITHOUT A WORD)
		#elif not any( ( char in term ) for char in LETTERS ):
		elif not any( ( char in LETTERS ) for char in term ):
			pigified_term = term
		else:
			pigified_term = pigify_term( term )
		pigified_term_list.append( pigified_term )
	return pigified_term_list


def pigify_term( term ):
	##  SEPARATE TERM INTO LEADING & TRAILING PUNCTUATION AND THE WORD ITSELF
	lead = ''
	for char in term:
		if char in LETTERS:
			break
		else:
			lead += char
	tail = ''
	for char in reverse_string( term ):
		if char in LETTERS:
			break
		else:
			tail += char

	tail = reverse_string( tail )
	word = term.lstrip(lead).rstrip(tail)

	## PIGIFY THE WORD
	pigified_word = pigify_word( word )

	##  RE-ASSEMBLE AND RETURN
	pigified_term = ''.join( [ lead, pigified_word, tail ] )
	return pigified_term
	

def pigify_word( word ):
	##  EXPECTS A WORD WITHOUT LEADING OR TRAILING PUNCTUATION OR NUMBERS
	##  TOLERATES ENCLOSED PUNCTUATION, LIKE "WE'D", "YOU'LL", "ALAN'S", OR "DE-HYPHENATE"

	## TEST FOR CAPITALIZATON
	all_caps = True if word.isupper() else False
	start_cap = True if word[0].isupper() else False

	## PIG-LATINIZE THE WORD
	if word[0] in CONSONANTS:
		pigified_word = word[1:] + word[0].lower() + 'ay'
	elif word[0] in VOWELS:
		pigified_word = word + 'yay'
	else:
		pigified_word = word

	## RE-CAPITALIZE
	if all_caps:
		pigified_word = pigified_word.upper()
	elif start_cap:
		pigified_word = pigified_word[0].upper() + pigified_word[1:]

	return pigified_word


def reverse_string(string):
    return string[::-1]

