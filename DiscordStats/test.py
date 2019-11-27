import requests
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))
    input()

image = requests.get('https://cdn.discordapp.com/attachments/563224217777340437/648744582091243531/unknown.png')

dump(image)
