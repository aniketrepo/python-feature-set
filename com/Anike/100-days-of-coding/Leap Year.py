# [https://github.com/aniketrepo/python-feature-set/blob/main/com/Anike/stuff/Untitled.png] used for reference
year = int(input("Please enter a year of your choice: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("The year you gave is a leap year")
    else:
      print("The year you gave is not a leap year")
  else:
    print("The year you gave is leap year")
else:
  print("The year you gave is not a leap year")