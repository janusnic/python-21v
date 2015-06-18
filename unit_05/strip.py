str = "0000000this is string example....wow!!!0000000"
print (str.strip('0'))

print (str.rstrip('0'))


print (str.lstrip('0'))


str = " Let's learn Python "
print(str.strip())


s = "\t don't shout "
s.lstrip(), s.rstrip(), s.strip()



"<[unbracketed]>".strip("[](){}<>")

"<[unbracketed]>".strip("[](){}<>uned")


"<[unbracketed]>".strip("[]ud(){}<>ne")



var = """
      your text
      goes here
      """

# using string methods 
# split into lines, use every line except first and last, left strip and rejoin.
var2 = "\n".join([line.lstrip() for line in var.split("\n")[1:-1]])

print var2