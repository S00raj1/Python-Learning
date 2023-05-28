cloud  = False
rained_yesterday = False

if cloud  and rained_yesterday:
    print('it will rain today')
elif cloud and not rained_yesterday:
    print('it wont rain today')

elif not cloud and rained_yesterday:
    print('it wont rain ')
else:
    print('it wont rain todayy')


