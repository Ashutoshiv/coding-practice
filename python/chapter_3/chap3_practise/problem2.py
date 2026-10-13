letter = '''Dear <|name|>,
         You are selected!
         <|Date|>'''

print(letter.replace("<|name|>", "Sunny").replace("<|Date|>", "24 September 2028"))