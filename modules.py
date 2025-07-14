# Import platform module once
import platform

# Define a greeting function
def greeting(name):
    print("Hello " + name)

# Define a dictionary
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Call the function
greeting("Jonathan")

# Access and print from the dictionary
a = person1["age"]
print("Age:", a)

# Print current OS
os_name = platform.system()
print("Operating System:", os_name)

# Print all available names in the platform module
platform_details = dir(platform)
print("Platform Module Contents:", platform_details)
