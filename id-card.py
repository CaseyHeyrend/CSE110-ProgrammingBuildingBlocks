#Taking input from the user
print("Please enter the following information:")
firstn = input("First Name: ")
lastn = input("Last Name: ")
email = input("Email address: ")
phonenum = input("Phone Number: ")
job = input("Occupation: ")
id = input ("ID: ")
#Output
print()
print("The ID Card is:")
print("----------------------------------------")
print(f"{lastn.upper()}, {firstn}")

print("Occupation: " + job)
print("ID: " + id)
print()
print("Email address: " + email)
print("Phone Number: " + phonenum)
print("----------------------------------------")

