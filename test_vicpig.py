from vicpig import *

def test_vicpig():

	# words
	assert pigify_word( 'Aaron' ) == 'Aaronyay'
	assert pigify_word( '15' ) == '15'
	assert pigify_word( 'Alan\'s' ) == 'Alan\'syay'
	assert pigify_word( 'Peter\'s' ) == 'Eter\'spay'
	assert pigify_word( 'CAPS' ) == 'APSCAY'
	assert pigify_word( 'hyphenated-word' ) == 'yphenated-wordhay'

	# terms
	assert pigify_term( '"quoted"' ) == '"uotedqay"'
	assert pigify_term( '"commafollowingquote",' ) == '"ommafollowingquotecay",'
	assert pigify_term( '"quotefollowingcomma,"' ) == '"uotefollowingcommaqay,"'
	assert pigify_term( 'period.' ) == 'eriodpay.'



