from populating_hashmap import *


def permute_palindrome(st):

    hashmap = {}

    for i in st:
        if i in hashmap:
            del hashmap[i]
        else:
            hashmap[i] = 1
    
    if len(hashmap.keys()) == 1 and len(st) % 2 != 0:
        return True

    if len(hashmap.keys()) == 0 and len(st) % 2 == 0:
        return True
        
    return False
