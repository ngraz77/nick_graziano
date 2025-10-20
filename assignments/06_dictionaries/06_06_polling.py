favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}


people = ['jen', 'sarah', 'edward', 'phil', 'anna', 'mike']


for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")