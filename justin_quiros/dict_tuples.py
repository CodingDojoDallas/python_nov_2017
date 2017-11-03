my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuples():
	new_arr = []
	for key in my_dict:
		#new_arr.append(key)
		new_arr.append((key, my_dict[key]))
	print new_arr
tuples()