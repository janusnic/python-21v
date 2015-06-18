print 'Hello everyone. Say "Hello" to me!'.replace('Hello', 'Goodbye')

str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);


# define our method
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
 
# our text the replacement will take place
my_text = 'Hello everybody.'
 
# our dictionary with our key:values.
# we want to replace 'H' with '|-|'
# 'e' with '3' and 'o' with '0'
reps = {'H':'|-|', 'e':'3', 'o':'0'}
 
# bind the returned text of the method
# to a variable and print it
txt = replace_all(my_text, reps)
print txt    # it prints '|-|3ll0 3v3ryb0dy'

text = 'hello everybody'
w_dic = {'hel':'HEL'}
c_dic = {'E':'3', 'e':'3', 'o':'0'}
text = replace_all(text, w_dic)
text = replace_all(text, c_dic)
print text  # prints 'H3Ll0 3v3ryb0dy'

