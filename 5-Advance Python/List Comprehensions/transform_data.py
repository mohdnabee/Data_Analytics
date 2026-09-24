names =  [" Ali " , "Sara " , "JOHN"]

cleaned_data = [new_name.strip().lower()  for new_name in  names  if new_name   ]

print(cleaned_data)