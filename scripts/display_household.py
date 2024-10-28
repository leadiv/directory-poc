def transformHousehold(household):
    return {
        'household_image': household.get('attributes', {}).get('avatar'),
        'household_name': household.get('attributes', {}).get('name')
    }

def createHouseholdHtml(household):
    return ''.join((
        f'<img src="{household.get('household_image')}" alt="{household.get('household_name')}"/><br />',
        f'The {household.get('household_name')}<br />'
    ))

def display_household(household_json):
    household_data = household_json.get('data', [])

    household_info = [transformHousehold(household)  for household in household_data]

    html = [createHouseholdHtml(household) for household in household_info]

    return ''.join(html)
