import random
import string
print('''Do you want to type a secret message or decode?
Type 1 for writing a secret message and 2 for decoding 
Typing anything else will lead to Error''')

typeans = input("Input here : ")
if typeans=="1":
 print('''There are 3 types of secret message decoder. Key 1, Key 2 and Key 3.
Each key utilizes a different randomizing system.
Key 3 employs the most challenging randomizing system, making it the most secure option for transmitting any secret message
You must select the right key while decoding or you secret message can't be decoded 
Choose key using 1, 2 and 3. Any other input will lead to error ''')
 key = input("Choose a key between 1 2 3 :")
 if key=="1":
  a = input("Your secret code :")
  reverse = a[::-1]
  words =  ' '.join([''.join(random.sample(string.ascii_lowercase, 3)) + word for word in reverse.split()])
  b = (words)
  if a[0].isupper():
    raise TypeError("Word should not start with a capital letter.")

  elif len(a) > 0:
   print(b)
  else  :
    print ()
 elif key == "2":
  a = input("Your secret code :")
  reverse = a[::-1]
  words =  ' '.join([''.join(random.sample(string.ascii_lowercase, 3)) + word + ''.join(random.sample(string.ascii_lowercase, 3)) for word in reverse.split()])
  b = (words)
  if a[0].isupper():
   raise TypeError("Word should not start with a capital letter.")

  elif len(a) > 0:
    print(b)
  else  :
    print ()

 elif key == "3":
  a = input("Your secret code :")
  reverse = a[::-1]
  words =  ' '.join([''.join(random.sample(string.ascii_lowercase, 6)) + word + ''.join(random.sample(string.ascii_lowercase, 6)) for word in reverse.split()])
  b = (words)
  if a[0].isupper():
   raise TypeError("Word should not start with a capital letter.")

  elif len(a) > 0:
    print(b)
  else  :
    print ()
 else :
  raise TypeError("Invalid input")
elif typeans=="2":
 print('''There are 3 types of secret code decoder. Key 1, Key 2 and Key 3.
 Each key utilizes a different randomizing system.
 You must select the right key while decoding or you secret code can't be decoded.
 Choose key using 1, 2 and 3. Any other input will lead to type error ''')
 key = input("Choose a key between 1 2 3 :")
 if key=="1":
  a = input("Input word to decode :")
  if a[0].isupper():
    raise TypeError("Word should not start with a capital letter.")
  reverse = a[::-1]
  b = ' '.join([word[:-3] for word in reverse.split()])
  if len(a) > 0:
   print(b.capitalize())
  else :
   raise TypeError("Invalid Input")
 if key=="2":
  a = input("Input word to decode :")
  if a[0].isupper():
    raise TypeError("Word should not start with a capital letter.")
  reverse = a[::-1]
  b = ' '.join([word[3:-3] for word in reverse.split()])
  if len(a) > 0:
   print(b.capitalize())
  else :
   raise TypeError("Invalid Input")
 if key=="3":
  a = input("Input word to decode :")
  if a[0].isupper():
    raise TypeError("Word should not start with a capital letter.")
  reverse = a[::-1]
  b = ' '.join([word[6:-6] for word in reverse.split()])
  if len(a) > 0:
   print(b.capitalize())
  else :
   raise TypeError("Invalid Input")
else:
  raise TypeError("Invalid Input")