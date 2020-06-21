if __name__ == '__main__':
    dogsTuple = (('dog1',('dog2',)),(('dog3',),('dog4','dog5')))
    #var = ('dog1',('dog2',)) in dogsTuple
    var = dogsTuple[0][1][0]
    print(var)
