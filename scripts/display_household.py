def transform_person(id, people_info):
    person_found = [
        info for info in people_info
        if info['id'] == id
    ]

    try:
        attributes = person_found[0]['attributes']

        return {
            'avatar': attributes['avatar'],
            'name': attributes['name'],
        }

    except:
        return None

def transform_household(household, people_info):
    attributes = household['attributes']

    return {
        'household_image': attributes['avatar'],
        'household_name': attributes['name'],
        'household_members': [
            transform_person(person_ref['id'], people_info) for person_ref in household['relationships']['people']['data']
            if person_ref['type'] == 'Person'
        ]

    }

def create_member_html(member, is_last_member):
    if is_last_member:
        separator = ''
    else:
        separator = ','

    return ''.join((
        '<li>',
        f'<img src="{member.get('avatar')}" alt="{member.get('name')}"/>',
        f'<span>',
        member.get('name'),
        f'</span>{separator}',
        '</li>'
    ))

def create_household_html(household):
    return ''.join((
        f'<img src="{household.get('household_image')}" alt="{household.get('household_name')}"/>',
        f'<h2>The {household.get('household_name')}</h2>',
        '<ul>',
        ''.join([
            create_member_html(member, index == len(household.get('household_members', [])) - 1) for index, member in enumerate(household.get('household_members', []))
            if member
        ]),
        '</ul>'
    ))

def display_household(household_json):
    household_data = household_json.get('data', [])
    household_people = household_json.get('included', [])

    household_info = [transform_household(household, household_people)  for household in household_data]

    html = [create_household_html(household) for household in household_info]

    return ''.join(html)
