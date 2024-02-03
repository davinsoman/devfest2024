'''
@author: anthony saidenberg ajs174
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists.
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''

    a = []
    b = []
    lis = list(ratings[name])
    #print("lis:", lis)
    recs = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    for num in range(len(lis)):
        if lis[num] == 0:
            b.append(items[num])
        else:
            a.append(items[num])

    c = []
    d = []
    for item in recs:
        #print(item)
        if item[0] in a:
            c.append(item)
        if item[0] in b:
            d.append(item)
    #print("a:", a)
    #print("b:", b)
    #print(d)
    e = sorted(c, key = lambda x: -x[1])
    f = sorted(d, key = lambda x: -x[1])
    #print(e)
    #print(f)
    
    x = [RecommenderEngine.similarities(name, ratings)]
    print(3)
    print(x)
    y= x[0][0][0]
    print(y)
    
    z = ratings2[y]
    print(z)
    ratings2[name] = z
    strlist = z[0]
    return "we reccomend joining the " + strlist + " chat to " + name
    #return (e[:top], f[:top])



if __name__ == '__main__':
    name = 'student1367'

    items = ['I find it difficult to get out of bed in the morning?', 'I have less apetite than before', 'I feel lonely',
             'I have less interests in my hobbies', 'I feel anxious often', 'I have low energy', 'I have scuicial thoughts', 'I have trouble concentrating', 'I find it difficult to sleep', 
             'I overindulge in drugs and/ or alcohol']
    
    items2 = ['depression', 'bipolar', 'ADHD', 'OCD', 'Anxiety', 'Anorexia', 'Bulimia']

    ratings = {'student1367': [0, 3, 5, 0, 0, 1, 5, 1, 3, 0],

               'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5],

               'student1206': [5, 0, 1, 0, 3, 0, 5, 3, 3, 0],

               'student1103': [3, 3, 3, 5, 0, 0, 5, 3, 5, 5]}
    
    

    ratings2 = {'student1046': ['depression'],

               'student1206': ['bipolar'],

               'student1103': ['ADHD']}

    numUsers = 2

    top = 3

    print(makerecs(name, items, ratings, numUsers, top))
