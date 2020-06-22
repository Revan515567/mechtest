import math
def fight(r1, r2, tactics):
        
    i, bots = 0, sorted((r2,r1), key=itemgetter('speed'))                    # Get the bots in reversed order!
    for r in bots: r['tactics'] = r['tactics'][::-1]                         # Reverse the tactics to use pop()
    
    while 1:
        i ^= 1                                                               # Swapper
        if bots[i]['tactics']:
            bots[i^1]['health'] -= tactics[ bots[i]['tactics'].pop() ] # Hit
            bots[i^1]['insanity'] += tactics[bots[i]['tactics'].pop()] * math.sqrt(bots[i^1]['health'])
        if bots[i^1]['health'] <= 0 or all(not r['tactics'] for r in bots) or bots[i^1]['insanity'] >= 2000:  # other bot is dead or has reached max. insanity or no tactics for both of them
            break
    
    a,b = bots
    cmp = (a['health'] < b['health']) - (a['health'] > b['health'])          # 1: b wins / -1: a wins / 0: tie
    
    return "The fight was a draw." if not cmp else f"{bots[max(cmp,0)]['name']} has won the fight."
