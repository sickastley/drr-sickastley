from redusers import Redusers

client = Redusers()
client.test('data.csv')


# # # to get userlist from existing subs
# client.bulk('DesiMeta', 'data.csv', 1000)
# client.bulk('indiaspeaks', 'data.csv', 1000)
# client.bulk('rwingnat', 'data.csv', 1000)
# client.bulk('Sham_Sharma_Show', 'data.csv', 1000)

# # # client.bulk('librandu', 'librandu.csv', 5000)

# # # to invite  from the given file
# # # client.invite('data.csv')

# # # to merge old csv to new type.
# # # last value tells whether the file has userbase which has been invited or not.
# # # True for invited and False for not invited.

# # # client.oldToNew('pholder_indiaspeaks.csv', 'data.csv', 'False')
# # # client.oldToNew('test.csv', 'data.csv', 'False')
# # # client.oldToNew('chodi.csv', 'data.csv', 'False')
# # # client.oldToNew('users.csv', 'data.csv', 'False')

# # # client.oldToNew('sent.csv', 'data.csv', 'True')
