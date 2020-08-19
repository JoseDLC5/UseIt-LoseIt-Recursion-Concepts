'''
Name: Jose de la Cruz

Date: 9/30/19

CS115 - HW 2 ~ Recursion

Pledge: I pledge my honor that I have abided by the stevens honor system
'''
def makeChange(amount, coins):
    '''finds the least amount of coins needed to use to evenly divide an amount with a list of given coin values'''
    if (coins == []):
        return [float("inf"), []]
    if (amount == 0):
        return [0, []]
    if (amount <= 0):
        return [float("inf"), []]

    useIt = makeChange(amount - coins[0], coins)
    loseIt = makeChange(amount, coins[1:])

    useIt = [useIt[0] +1, useIt[1] + [coins[0]]]

    if(useIt < loseIt):
        
        return useIt
    else:
        return loseIt

    
def LCS(a, b):
    if not (a and b):
        return ''
    if (a[0]==b[0]):
        return a[0] + LCS(a[1:], b[1:])

    thing = (max(len((LCS(a[1:],b))),len((LCS(a,b[1:])))))

    if (thing == len((LCS(a,b[1:])))):
        return LCS(a,b[1:])
    else:
        return LCS(a[1:],b)


def PLCS(a, b):
    def helper(s1,s2,count):
        if (not s1 or not s2):
            return []
        if (s1[0] == s2[0]):
            return [count] + helper(s1[1:],s2[1:],count + 1)
        else:
            return helper(s1[1:], s2, count + 1)
    substring = LCS(a,b)
    if (substring == ''):
        return [[-1],[-1]]
    if not (a and b):
        return [[-1],[-1]]
    

    return [helper(a,substring,0), helper(b,substring,0)]





