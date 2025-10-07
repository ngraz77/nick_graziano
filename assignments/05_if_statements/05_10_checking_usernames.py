current_users = ('Nick', 'Power Man', 'Penguin', 'Graz', 'JD')

new_users = ('Nick', 'Power Man', 'CJ', 'Bron', 'Matt')

for new_users in new_users:
    if new_users in current_users:
        print("you need to enter a new username.")

for new_users in new_users:
    if new_users not in current_users:
        print("This username is available.")