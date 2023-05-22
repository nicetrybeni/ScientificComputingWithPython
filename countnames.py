counts = dict()
names = ['beni', 'beni', 'duqs', 'robec', 'lloyd', 'mags', 'sherwin', 'keneth']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)