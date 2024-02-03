'''
@author: anthony saidenberg ajs174
'''
def averages(items, ratings):
    '''
    This function calculates the average ratings for items.
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    dict = {}
    for num in range(len(items)):
        f = 0
        x = 0
        #print f
        for rating in ratings.values():
            f += rating[num]
            if rating[num] != 0:
                x += 1
        if x != 0:
            dict[items[num]] = float(f / x)
        else:
            dict[items[num]] = float(0)
    don = sorted(dict.items())
    don = sorted(don, key=lambda x: x[1], reverse=True)
    return don






def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    x = ratings[name]
    result = []

    for i in ratings:
        if i == name:
            continue
        y = ratings[i]
        dp = 0
        for rating1, rating2 in zip(x, y):
            if rating1 != 0 and rating2 != 0:
                dp += rating1 * rating2
        result.append((i,dp))
    result.sort(key=lambda x: (-x[1], x[0]))
    return result



def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations
    based on the parameters and weighted average. A two-tuple is returned, where
    the first element is a string and the second element is a float.
    '''

    a = similarities(name, ratings)
    dict = {}
    for num in range(numUsers):
        (k, v) = a[num]
        dict[k] = v
    dictb = {}
    #print(dict)
    for x in dict.keys():
        if x == name:
            continue
        r = []
        for num2 in range(len(items)):
            l = ratings[x][num2]
            num2 = l * dict[x]
            r.append(num2)
        dictb[x] = r
    return (averages(items, dictb))




if __name__ == '__main__':
    name = 'Liam'
    items = ['Cat', 'Dog', 'Zebra']
    ratings = {'Liam': [10, 2, 5], 'Man-Lin': [2, 5, 0], 'Max': [7, 9, 1],
               'Jose': [1, 2, 3]}
    numUsers = 2


    recommendations(name, items, ratings, numUsers)
