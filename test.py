def test(a={}):
    a['2'] = 1


a = {'3': 4}
test(a)
print(a)