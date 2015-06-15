a_dict = {'server': 'localhost','database':'mysql',1000:['KB','MB','GB'],1024:['KiB','MiB','GiB']}

print(a_dict)
print(len(a_dict))

if 1000 in a_dict:
	print('1000 in dict')
else:
	print('not in dict')

print(a_dict[1000])

print(a_dict[1024])

print(a_dict[1024][2])
