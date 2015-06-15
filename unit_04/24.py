a_dict = {'server': 'localhost','database':'mysql',1000:['KB','MB','GB'],1024:['KiB','MiB','GiB']}

def is_it_true(anything):
	if anything:
		print('in dict')
	else:
		print('not in dict')

is_it_true({})
is_it_true({'a':1})
is_it_true(a_dict)
