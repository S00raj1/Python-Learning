rich = {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
Europe ={ 'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

print('Countries that are rich but not in Europe :',rich-Europe)
print('Countries that are in Europe but not Rich :',Europe-rich)
print('Countries that are both rich and in Europe : ', Europe&rich)
print('Coutnries that are either rich or in Europe :', (Europe | rich)-(Europe & rich))
print('all the countries in either of the sets : ', (Europe | rich)-(Europe & rich))


print(rich.isdisjoint(Europe))
if (rich & Europe) == None :
    print('Sets are disjoint')
else:
    print('sets are joint')

# remov = Europe & rich
# for i in remov:
#     rich.remove(i)
# print(rich)

rich.difference_update(Europe)
print(rich)


asian_rich = {'China','Japan'}
american_rich = {'USA','Canada'}

print(asian_rich.issubset(rich))
print(rich.issuperset(asian_rich))
print(american_rich.issubset(rich))