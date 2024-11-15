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
        'household_allowed_count': len(people_info),
        'household_members': [
            _transform_person(person_ref['id'], people_info) for person_ref in household['relationships']['people']['data']
            if person_ref['type'] == 'Person'
        ]

    }

def _should_use_separator(index, total):
    return (total > 1) and (index != total - 1)

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
        '<article class="directory-household">',
        f'<h2>The {household.get('household_name')}</h2>',
        f'<img src="{household.get('household_image')}" alt="{household.get('household_name')}"/>',
        '<ul>',
        ''.join([
            _create_member_html(member, index, household.get('household_allowed_count')) for index, member in enumerate(household.get('household_members', []))
            if member
        ]),
        '</ul>',
        '</article>',
    ))

def _is_include_in_the_online_pictorial_directory_field(field_datum):
    FIELD_DEFINITION_ID = '830513'

    is_associated_with_person = field_datum['relationships']['customizable']['data']['type'] == 'Person'
    is_field_definition = field_datum['relationships']['field_definition']['data']['type'] == 'FieldDefinition'
    is_correct_field = field_datum['relationships']['field_definition']['data']['id'] == FIELD_DEFINITION_ID

    return is_associated_with_person and is_field_definition and is_correct_field

def _get_person_id_from_field_datum(field_datum):
    return field_datum['relationships']['customizable']['data']['id']

def _get_allowed_people(api_json):
    included = api_json['included']

    return [
        _get_person_id_from_field_datum(field_datum) for field_datum in included
        if _is_include_in_the_online_pictorial_directory_field(field_datum)
    ] 


def display_household(household_json, allowed_people):
    household_data = household_json.get('data', [])
    household_people = [
        person for person in household_json.get('included', [])
        if person['id'] in allowed_people
    ]

    household_info = [_transform_household(household, household_people)  for household in household_data]

    html = [_create_household_html(household) for household in household_info]

    return ''.join(html)

def get_people_links(household_json):
    return [
        f"{household['relationships']['people']['links']['related']}?include=field_data" for household in household_json['data']
    ]

def get_allowed_people_list(api_links, api_call):
    white_list = []
    for api_link in api_links:
        results = api_call(api_link)
        white_list.extend(_get_allowed_people(results))

    return white_list

