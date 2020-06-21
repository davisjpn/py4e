aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')
#if len(aDict) == 0:
#    print('None')
#else:
#    print(max(aDict, key=aDict.get))
n = 'b'
if n in aDict:
    print(aDict[n])
