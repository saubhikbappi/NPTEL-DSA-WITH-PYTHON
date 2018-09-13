def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]

adict = {'match1':{'player1':57, 'player2':38},
        'match2':{'player3':9, 'player1':42},
        'match3':{'player2':41, 'player4':63, 'player3':91}}
print (orangecap(adict))

