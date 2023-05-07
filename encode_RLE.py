text = input("Masukkan Text:")

def encode_message(text):
   encoded_string = ""
   i = 0
   while( i <= len(text)-1 ):
      count = 1
      ch = text[i]
      j = i
      while( j < len(text)-1 ):
         if(text[j] == text[j+1]):
            count = count + 1
            j = j + 1
         else:
            break
      encoded_string = encoded_string + str(count) + ch
      i = j + 1
   return encoded_string