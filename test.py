from ossapi import *

api = OssapiV2(int(11627), str('jfkuMglKmdsM58wMnlzAwwLrmps5A1qwhVCskDKn'), 'http://localhost:727/')
print(api.search(query="peppy").users.data[0].profile_colour)
