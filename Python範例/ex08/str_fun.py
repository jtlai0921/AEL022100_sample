s1 = 'python內建函式可以對字串做字串轉換、字串搜尋、字串分割。'
s2 = 'hello world!'

print(s1.find('字串'))
print(s1.rfind('字串'))
print(s1.startswith('字串'))
print(s1.endswith('。'))
print(s1.index('字串', 17))
print(s1.rindex('字串', 0, 17))
print(s1.count('字串'))
print(s1.split('、', 1))
print(s1.rsplit('、', 1))
print(','.join(s1.split('、')))
print(s1. replace('串','元'))
print(s2. capitalize())
print(s2. title())
print('Hello\tWorld!'.expandtabs(4))
print('\tHello World!\n'.strip())
print(s2.rstrip('!'))
print(s2.lstrip('h'))
print(s2.upper())
print('ABCDEF'.lower())
print(s2.title().swapcase())
print(max(s2))
print(min(s2))
