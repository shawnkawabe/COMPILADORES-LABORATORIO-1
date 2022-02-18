# Variáveis de controle
current_state =   'q0'
current_char  =   ''
words_accepted_char = ['if', 'for', 'then', 'else']
fixed_char = ''
is_fixed_char = False
CURRENT_EXEC = '0'
print(f'AFD no estado {current_state}')

# Exercicio 2

def verify_letter_index(current_index, current_inputed_char_to_compare):

	for i in words_accepted_char:
		if current_inputed_char_to_compare is list(i)[current_index]:
			return i
	return ''

def ex2_2(current_inputed_char, received_current_state, current_fixed_char):
	
	if received_current_state == 'q0':
		current_fixed_char = verify_letter_index(int(received_current_state[1]), current_inputed_char)
		
	if current_fixed_char != '' and received_current_state == 'q0':
		received_current_state = 'q1'
		print(f'AFD -> estado {received_current_state} {current_fixed_char}')
		print('Palavra aceita')
		return current_fixed_char, 'q1', '2.2'

	elif received_current_state != 'q0' and current_fixed_char != '':
    	
		if current_fixed_char[int(received_current_state[1])] is current_inputed_char and len(current_fixed_char) -1 == int(received_current_state[1]):
			print(f'{current_fixed_char} and len {len(current_fixed_char)}')
			print(f'AFD -> estado qf') 
			print('Palavra aceita')
			return '', 'qf', '0'
		
		if current_fixed_char[int(received_current_state[1])] is current_inputed_char:
			print(f'{current_fixed_char} and len {len(current_fixed_char)}')
			print(f'AFD -> estado q{str(int(received_current_state[1]) + 1)}') 
			print('Palavra aceita')
			return current_fixed_char, 'q'+ str(int(received_current_state[1]) + 1), '2.2'

	print('Palavra não aceita')
	return '', 'qf', '0'

while(current_state != 'qf'):
	
  if CURRENT_EXEC == '0':
    CURRENT_EXEC = input('Digite um exercicio:\n')

  elif CURRENT_EXEC == '1':
	  current_char = input('Digite um caractere:\n')
	  fixed_char, current_state, CURRENT_EXEC = ex2_2(current_char, current_state, fixed_char)

  else:
    print('Digite um exercicio válido!')


  if(current_state == 'qf'):
    print('Estado final')