import re
file=['muditjain788@gmail.com','jainmudit3008@gmail.com','noreply.com']
for addressToVerify in file:
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        	print('Bad Syntax man')
        	raise ValueError('Bad Syntax man')
    else:
                print('true')
