a = [{'rect': [63, 26, 50, 50], 'emot': [{'confid': 0.328, 'type': 'Joy'}, {'confid': 0.272, 'type': 'Optimism'}, {'confid': 0.216, 'type': 'Pride'}, {'confid': 0.162,'type': 'Vitality'}, {'confid': 0.016, 'type': 'Harmony'}, {'confid': 0.003, 'type': 'Hate'}, {'confid': 0.001, 'type': 'Surprise'}, {'confid': 0.0, 'type': 'Calm'}, {'confid': 0.0, 'type': 'Interest'}, {'confid': 0.0, 'type': 'Embarrassed'}, {'confid': 0.0, 'type': 'Grievance'}, {'confid': 0.0, 'type': 'Conflict'}, {'confid': 0.0, 'type': 'Aggressiveness'}, {'confid': 0.0, 'type': 'Sincerity'}, {'confid': 0.0, 'type': 'Apprehension'}, {'confid': 0.0, 'type': 'Serenity'}, {'confid': 0.0, 'type': 'Trust'}, {'confid': 0.0, 'type': 'Anticipation'}, {'confid': 0.0, 'type': 'Angry'}, {'confid': 0.0, 'type': 'Disgust'}, {'confid': 0.0, 'type': 'Love'}, {'confid': 0.0, 'type': 'Cowardice'}, {'confid': 0.0, 'type': 'Deceptiveness'}, {'confid': 0.0, 'type': 'Acceptance'}, {'confid': 0.0, 'type': 'Annoyance'}, {'confid': 0.0, 'type': 'Gratitude'}, {'confid': 0.0, 'type': 'Insincerity'}, {'confid': 0.0, 'type': 'Contempt'}, {'confid': 0.0, 'type': 'Fatigue'}, {'confid': 0.0, 'type': 'Submission'}, {'confid': 0.0, 'type': 'Admiration'}, {'confid': 0.0, 'type': 'Desire'}, {'confid': 0.0, 'type': 'Envy'}, {'confid': 0.0, 'type': 'Fear'}, {'confid': 0.0, 'type': 'Depression'}, {'confid': 0.0, 'type': 'Boredom'}, {'confid': 0.0, 'type': 'Passiveness'}, {'confid': 0.0, 'type': 'Bravery'}, {'confid': 0.0, 'type': 'Suspicion'}, {'confid': 0.0, 'type': 'Puzzlement'}, {'confid': 0.0, 'type': 'Awe'}, {'confid': 0.0, 'type': 'Distraction'}, {'confid': 0.0, 'type': 'Sadness'}, {'confid': 0.0, 'type': 'Neglect'}, {'confid': 0.0, 'type': 'Boastfulness'}, {'confid': 0.0, 'type': 'Pessimism'}, {'confid': 0.0, 'type': 'Neutral'}, {'confid':0.0, 'type': 'Uneasiness'}, {'confid': 0.0, 'type': 'Insult'}, {'confid': 0.0, 'type': 'Tension'}, {'confid': 0.0, 'type': 'Disapproval'}, {'confid': 0.0, 'type': 'Defiance'}, {'confid': 0.0, 'type': 'Shame'}, {'confid': 0.0, 'type': 'Remorse'}], 'in_whitelist': False}]

def getEmoji(rawData):
    data = []
    for r in rawData:
        d = {}
        d['rect'] = r['rect']
        emoji = []
        for e in r['emot']:
            if e['confid'] > 0.1:
                print()
                emoji.append(e)
            else:
                break
        d['emot'] = emoji
        data.append(d)
    return data


print(getEmoji(a))