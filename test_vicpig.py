from vicpig import *

def test_vicpig():

	# words
	assert pigify_word( 'Aaron' ) == 'Aaronyay'
	assert pigify_word( '15' ) == '15'
	assert pigify_word( 'Alan\'s' ) == 'Alan\'syay'
	assert pigify_word( 'Peter\'s' ) == 'Eter\'spay'
	assert pigify_word( 'CAPS' ) == 'APSCAY'

	# terms
	assert pigify_term( '"quoted"' ) == '"uotedqay"'


