
# default argument

# def add(a,b=30,c=40):
#     return a+b+c
# print(add(20))
# print(add(10,10,10))

# Example 2: internationalization
# def greet(key, lang='en'):
#     words = {
#             'hello': {
#                 'en': 'Hello',
#                 'fr': 'Bonjour',
#                 'np': 'नमस्कार',
#                 'jp': 'こにちは'
#             },
#             'bye': {
#                 'en': 'Bye',
#                 'fr': 'au revoir',
#                 'np': 'फेरी भेटौला',
#                 'jp': 'さよなら'
#             }
#     }
#     print(words[key][lang])
# greet('hello')
# greet('hello','np')
# greet('bye','np')
# greet('hello','jp')
# greet('bye','jp')
#


def college(abc,clas='first'):
    courses = {
            'csit' : {
                'first' : 'xyz',
                'second' : 'abc',
                'third' : 'sjjafja'
            },
            'bca' : {
                'first' : 'klm',
                'second' : 'hjk',
                'third' : 'xdaba'
            }
        }
    print(courses[abc][clas])
college('csit','first')


