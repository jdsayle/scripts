import re
import fileinput

# change NAME_OF_FILE to local file
for line in fileinput.input(['NAME_OF_FILE'], inplace=True):
    print(re.sub(r'<.*?>', '', line), end='')
