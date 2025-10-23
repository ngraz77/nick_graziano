def build_profile(first, last, **info):
    profile = {
        "first_name": first,
        "last_name": last
    }
    profile.update(info)
    return profile

user = build_profile("Nick", "Graziano", location="New Jersey", field="Communications")

print(user)