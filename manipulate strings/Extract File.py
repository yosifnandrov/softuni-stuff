whole_file = input().split('\\')

file_name , extension = whole_file[-1].split(".")
print(f"File name: {file_name}\nFile extension: {extension}")