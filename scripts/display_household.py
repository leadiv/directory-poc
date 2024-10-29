def transform_person(id, people_info, is_primary):
    person_found = [
        info for info in people_info
        if info.get('id', '') == id
    ]

    try:
        return {
            'avatar': person_found[0].get('attributes', {}).get('avatar', ''),
            'name': person_found[0].get('attributes', {}).get('name', ''),
            'is_primary': is_primary,
            'membership': person_found[0].get('attributes', {}).get('membership', ''),
            'status': person_found[0].get('attributes', {}).get('status', ''),
        }

    except:
        return None

def transform_household(household, people_info):
    return {
        'household_image': household.get('attributes', {}).get('avatar'),
        'household_name': household.get('attributes', {}).get('name'),
        'household_members': [
            transform_person(person_ref['id'], people_info, person_ref['id'] == household['attributes']['primary_contact_id']) for person_ref in household['relationships']['people']['data']
            if person_ref['type'] == 'Person'
        ]

    }

def create_member_html(member):
    if member.get('is_primary'):
        data_primary = f'data-primary '
    else:
        data_primary = ''

    data_membership = f'data-membership="{member.get('membership')}" '
    data_status = f'data-status="{member.get('status')}"'

    return ''.join((
        '<li>',
        f'<img src="{member.get('avatar')}" alt="{member.get('name')}"/>',
        f'<span {data_primary}{data_membership}{data_status}>',
        member.get('name'),
        '</span>,',
        '</li>'
    ))

def create_household_html(household):
    return ''.join((
        f'<img src="{household.get('household_image')}" alt="{household.get('household_name')}"/><br/>',
        f'<h2>The {household.get('household_name')}</h2>',
        '<ul>',
        ''.join([
            create_member_html(member) for member in household.get('household_members', [])
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
