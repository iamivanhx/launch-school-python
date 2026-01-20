# Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(f"Original = {info}")
info = info.replace(':', '+')
print(f"Modified = {info}")