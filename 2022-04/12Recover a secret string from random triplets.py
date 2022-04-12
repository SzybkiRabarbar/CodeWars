    #'triplets is a list of triplets from the secrent string. Return the string.'
def recoverSecret(triplets):
    for tr in triplets:
        for t in tr:
            print(t, end=" ")
    return None


triplets = [ #whatisup
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))