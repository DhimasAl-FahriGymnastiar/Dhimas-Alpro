current_users=['admin', 'user1', 'user2', 'user3', 'user4']

new_users=['user1', 'user5', 'user6', 'user7', 'user8']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")