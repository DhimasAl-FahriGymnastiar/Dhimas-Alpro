def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    "Budi",
    "Santoso",
    age=20,
    major="Industrial Engineering",
    university="UNS"
)

print(my_profile)