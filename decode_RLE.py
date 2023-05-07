chipper = input("Massukkan chipper text: ")

def decode(chipper_text):
   decoded_message = ""
   i = 0
   run_count=""
   while( i <= len(chipper_text) -1 ):
      if (chipper_text[i].isdigit()):
         run_count += chipper_text[i]
      else:
         run_ch = chipper_text[i]
         run_count = int(run_count)
         decoded_message +=  run_count * run_ch
         run_count=""
      i = i + 1
   return decoded_message

print(decode(chipper))