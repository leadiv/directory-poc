def _transform_person(id, people_info):
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

def _transform_household(household, people_info):
    attributes = household['attributes']

    return {
        'household_image': attributes['avatar'],
        'household_name': attributes['name'],
        'household_count': attributes['member_count'],
        'household_members': [
            _transform_person(person_ref['id'], people_info) for person_ref in household['relationships']['people']['data']
            if person_ref['type'] == 'Person'
        ]

    }

def _should_use_separator(index, total):
    if total > 1:
        if index != total - 1:
            return False
        else:
            return True
    else:
        return False

def _create_member_html(member, index, total_household):
    if _should_use_separator(index, total_household):
        separator = ','
    else:
        separator = ''

    return ''.join((
        '<li>',
        f'<img src="{member.get('avatar')}" alt="{member.get('name')}"/>',
        f'<span>',
        member.get('name'),
        f'</span>{separator}',
        '</li>'
    ))

def _create_household_html(household):
    return ''.join((
        f'<img src="{household.get('household_image')}" alt="{household.get('household_name')}"/>',
        f'<h2>The {household.get('household_name')}</h2>',
        '<ul>',
        ''.join([
            _create_member_html(member, index, household.get('household_count')) for index, member in enumerate(household.get('household_members', []))
            if member
        ]),
        '</ul>'
    ))

def display_household(household_json, allowed_people):
    household_data = household_json.get('data', [])
    household_people = [
        person for person in household_json.get('included', [])
        if person['id'] in allowed_people
    ]

    household_info = [_transform_household(household, household_people)  for household in household_data]

    html = [_create_household_html(household) for household in household_info]

    return ''.join(html)
