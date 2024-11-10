import unittest

from mock_household import single_household
from mock_household import households_people

from display_household import display_household
from display_household import get_people_links
from display_household import get_allowed_people


class TestHousehold(unittest.TestCase):

    def test_single_display_household(self):
        self.maxDiff = None

        expected = ''.join((
            '<img src="https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>',
            '<h2>The Kocher Household</h2>',
            '<ul>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher"/><span>Rob Kocher</span></li>',
            '</ul>'
        ))
        actual = display_household(single_household, ['36729400'])

        self.assertEqual(expected, actual, 'it should be able to display one family member as HTML')

    def test_multiple_display_household(self):
        self.maxDiff = None

        expected = ''.join((
            '<img src="https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>',
            '<h2>The Kocher Household</h2>',
            '<ul>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher"/><span>Rob Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg" alt="Tammy Kocher"/><span>Tammy Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png" alt="Charisa Kocher"/><span>Charisa Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png" alt="Kupo Kocher"/><span>Kupo Kocher</span></li>',
            '</ul>'
        ))
        actual = display_household(single_household, ['36729400', '49166778', '49657796', '76460632'])

        self.assertEqual(expected, actual, 'it should be able to display multiple amily members as HTML')

class TestPeopleLinks(unittest.TestCase):

    def test_get_people_links(self):
        self.maxDiff = None

        expected = ['https://api.planningcenteronline.com/people/v2/households/6759685/people?include=field_definitions']
        actual = get_people_links(single_household)

        self.assertEqual(expected, actual, 'it should return the API links for the people related to the household')

class TestAllowedPeople(unittest.TestCase):

    def test_get_allowed_people(self):
        self.maxDiff = None

        expected = ['36729400']
        actual = get_allowed_people(households_people)

        self.assertEqual(expected, actual, 'it should be able to return a list of people IDs that are allowed to be shown on the online directory')


if __name__ == '__main__':
    unittest.main()
