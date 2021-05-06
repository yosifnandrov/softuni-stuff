print("Give me your version and i will tell you what is next version(version.version.version)\n")
version = input().split(".")
version_nums = [int(el) for el in version]
if version_nums[1] == 9 and version_nums[2] == 9:
    version_nums[1] = 0
    version_nums[2] = 0
    version_nums[0] += 1
elif version_nums[2] == 9:
    version_nums[1] += 1
    version_nums[2] = 0
else:
    version_nums[2] += 1
version_str = [str(el) for el in version_nums]
final_version = ".".join(version_str)
print(final_version)


