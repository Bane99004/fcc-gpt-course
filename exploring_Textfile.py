with open("test.txt",'r', encoding='utf-8') as f:
  text = f.read()
  char = sorted(set(text))
  print(char)
  
string_to_int = {chr:i for i, chr in enumerate(char)} 
int_to_string = {i:chr for i, chr in enumerate(char)} 
print(string_to_int)
print(int_to_string)
encode = lambda a : [string_to_int(c) for c in a]
encode = lambda s : ''.join([int_to_string(c) for c in s])
