import requests
import functools

from display_household import display_household

def entrypoint():
    results = requests.get(
        'https://api.planningcenteronline.com/people/v2/households?include=people&per_page=10',
        auth=(
            '1c553c82520927b0e25131e0dd760a8600f1978e09a41238162b7399cc30a511',
            'pco_pat_3095534378506a8e6da28687face4f35748abf3e981aa488b1e1522dcba617bf7f802d49'
        )
    )

    json_results = results.json()

    print('<!DOCTYPE html><html><head><style>')
    print('''
        body {
          backgaround-color: black;
        }

        img:not([alt*="Household"]) {
          width: 40px;
          border-radius:20px;
          margin-right: 5px;
        }

        h2,
        span,
        li {
          color: white;
        }

        li {
          list-style: none;
          display: flex;
          align-items: center
        }

        ul {
          padding: 0;
          display: flex;
          align-items: center;
          width: max-content;
          margin: 0 auto 80px auto;
        }

        ul > * + * {
          margin-left: 10px;
        }

        h2,
        ul,
        img[alt*="Household"] {
          text-align: center
        }

        img[alt*="Household"] {
          margin: 0 auto;
          width: max-content;
          display: block;
          border-radius: 20px;
        }

        h2 {
          font-style: italic;
        }

        [data-status="active"] {
          color: green;
        }

        [data-membership]:after {
          content: '[' attr(data-membership) ']';
          display: inline-block;
          margin-left: 5px;
        }
    ''')
    print('</style></head><body>')
    print(display_household(json_results))
    print('</body></html>')

def main():
    if __name__ == "__main__":
        entrypoint()

main()
