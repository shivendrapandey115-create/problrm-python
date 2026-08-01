# write aprongram to fill in aletter template given below with 
# name and date
letter = '''dear <|name|>,
you are selecter!
<|date|>'''
print(letter.replace("<|name|>", input("ente your name")).replace("<|date|>", input("enter a date")))