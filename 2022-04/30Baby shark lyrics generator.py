SongText={'doo':'doo doo doo doo doo doo',
          'baby':'Baby shark',
          'mommy':'Mommy shark',
          'daddy':'Daddy shark',
          'grandma':'Grandma shark',
          'grandpa':'Grandpa shark',
          'bloodlust':"Let's go hunt"}
def baby_shark_lyrics():
    result=str()
    for i in range(3):
        result+=f"{SongText.get('baby')}"

print(baby_shark_lyrics())
