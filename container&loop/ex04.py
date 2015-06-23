input_id = input('아이디를 입력하세요.')
members = ['egoing', 'leezche', 'grapittie']
for member in members:
    if member == input_id:
        print('Hello!, ' + member)
        import sys
        sys.exit()

print('Who are you?')
