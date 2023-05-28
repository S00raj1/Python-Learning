yoda = {
    'age' : 910,
    'species' : 'Yodas',
    'gender' : 'male',
    'affiliations' : ['Jedi','Galatic Republic'],
    'master' : {
        'name' : 'Qui-Gon jinn',
        'age' : 48,
        'affiliations' : ['Jedi','Galatic Republic','Heliost Clan'],
        'master' : {
            'name' : 'Dooku',
            'age' : 83,
            'affiliations' : ['House Serenno', 'Jedi']
        }
    }
}

# print(yoda['affiliations'][0])
# yoda['master']['master']['affiliations'].append('Sith') 
# print(yoda)

yoda.pop('master')
print(yoda)