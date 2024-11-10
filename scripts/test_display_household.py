import unittest

from mock_household import single_household
from display_household import display_household

class TestHousehold(unittest.TestCase):

    def test_display_household(self):
        self.maxDiff = None

        expected = ''.join((
            '<img src="https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg" alt="Kocher Household"/>',
            '<h2>The Kocher Household</h2>',
            '<ul>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg" alt="Rob Kocher"/><span>Rob Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg" alt="Tammy Kocher"/><span>Tammy Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png" alt="Charisa Kocher"/><span>Charisa Kocher</span>,</li>',
            '<li><img src="https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png" alt="Kupo Kocher"/><span>Kupo Kocher</span></li>'
            '</ul>'
        ))
        actual = display_household(single_household)

        self.assertEqual(expected, actual, 'it should be able to display the family household as HTML')

if __name__ == '__main__':
    unittest.main()
