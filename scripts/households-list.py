import requests
import functools
import time
import sys
import argparse
import logging

from display_household import display_household
from display_household import get_people_links
from display_household import get_allowed_people_list


class TooManyRetries(Exception):
    pass

def _api_call(api_url, username, password, log, retry=0):
    MAX_RETRY = 3
    WAIT_BETWEEN_RETRIES = 20

    try:
        log.info(f'Sending {api_url}: username {username}, password {password}')
        results = requests.get(api_url, auth=(username, password))

        return results.json()

    except Exception as error:
        if retry < MAX_RETRY:
            log.error(f'Caught exception. Retry Count: {retry}')
            _api_call(api_url, username, password, retry + 1)
            time.sleep(WAIT_BETWEEN_RETRIES)
        else:
            log.error(f'Failed with too many retries {error}')
            log.error(f'Raw return message {results.content}')
            raise TooManyRetries(f"MAX RETRY of {MAX_RETRY} has been reached. Stopping program")

def entrypoint(args, log):
    api_call = functools.partial(_api_call, username=args.username, password=args.password, log=log)

    log.info('calling very first household')
    json_results = api_call('https://api.planningcenteronline.com/people/v2/households?include=people&per_page=1')
    log.info('getting API links')
    people_api_links = get_people_links(json_results)
    log.info(f'api links ready: {people_api_links}')
    white_list = get_allowed_people_list(people_api_links, api_call)
    log.info(f'white list of directory membership created {white_list}')

    log.info('printing out test page')
    print('<!DOCTYPE html><html><head><link rel="stylesheet" media="screen" href="https://assets.cloversites.com/fonts/picker/proximanova/proximanovaheavy.css"><link rel="stylesheet" media="screen" href="https://assets.cloversites.com/fonts/picker/proximanova/proximanovaregular.css"><style>')
    print('''
        html {
          box-sizing: border-box;
          padding: 0;
          margin: 0;
        }

        body {
          font-family: 'Proxima Nova', 'Proxima Nova Heavy', sans-serif;
          background-color: #2b3f54;
          color: white;
          margin: 0;
        }

        .logo-banner {
            background-color: #f5f5ed;
            text-align: center;
            padding-bottom: 1.5rem;
        }

        .logo-banner__logo {
            width: 360px;
            padding-bottom: .94rem;
            margin-right: 0;
        }

        .intro {
          background-color: #395370;
          padding: 6rem 3rem;
          text-align: center;

          & > * + * {
            margin-top: 1.5rem;
          }

          p {
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
          }
        }

        .intro__heading {
          margin: 0;
          font-size: 2.4em;
          font-weight: 400;
          text-transform: uppercase;
          letter-spacing: 0.01em;
          padding-bottom: 1.5rem;
          max-width: 700px;
          border-bottom: 1px solid #556b83;
          margin-left: auto;
          margin-right: auto;
        }

        main {
          background-color: #f5f5ed;
          padding: 6rem 1.2rem;
          color: #395370;
          min-height: 100vh;

          & > * + * {
            margin-top: 5rem;
          }
        }

        .directory-household {
          max-width: 700px;
          margin-left: auto;
          margin-right: auto;

          & > * + * {
            margin-top: .83rem;
            text-align: center
          }

          h2 {
            font-weight: 400;
            margin: 0;
          }

          img {
            width: 100%;
            display: inline-block;
            border-radius: 20px;
          }

          ul {
            padding: 0;
            display: flex;
            align-items: center;
            width: max-content;
            margin-left: auto;
            margin-right: auto;

            & > * + * {
              margin-left: .6rem;
            }

            li {
              list-style: none;
              display: flex;
              align-items: center
            }

            img {
              width: 40px;
              border-radius: 20px;
              margin-right: .3rem;
            }
          }
        }

        footer {
          text-align: center;
          background-color: #395370;
          padding: 3.5rem 1.5rem;
          color: white;
          font-size: .875em;
          font-weight: 400;

          ul {
            margin: 0;
            padding: 0;
            list-style-type: none;

            li {
              display: inline-block;
            }

            & > * + * {
              margin-left: 1rem;
            }
          }

          span {
            color: #cfcbaa;
          }

          a {
            color: white;
            text-decoration: none;
          }
        }
    ''')
    print('</style></head><body>')
    print('<header class="logo-banner"><a href="https://cbclilburn.org/home"> <img srcset="https://s3.amazonaws.com/media.cloversites.com/df/df215a8c-96d5-4f44-8fee-549745631403/site-images/5779951a-1298-4353-9bd4-a1df28d8d141.png, https://s3.amazonaws.com/media.cloversites.com/df/df215a8c-96d5-4f44-8fee-549745631403/site-images/5779951a-1298-4353-9bd4-a1df28d8d141@2x.png 2x" border="0"> </a></header>')
    print('<article class="intro"><h1 class="intro__heading">Pictorial Directory</h1> <p>Some text here about the pictorial directory.</p> </article>')
    print('<main>')
    print(display_household(json_results, white_list))
    print('</main>')
    print('<footer><ul><li><a href="https://www.google.com/maps/place/869+Cole+Dr+SW,+Lilburn,+GA+30047/@33.860376,-84.117776,17z/data=!3m1!4b1!4m2!3m1!1s0x88f5a53ed0a850c1:0xfc2292c59d2c09d6" target="_blank">869 Cole Drive SW, Lilburn, GA 30047</a></li><li><span>phone:</span> (770) 806-0005</li><li><a href="mailto:office@cbclilburn.org" target="_self"><span>email:</span> office@cbclilburn.org</a></li><li><span>office hours:</span> 8:30-4:30 M-F</li></footer>')
    print('</body></html>')

def main():
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(prog='household-list', description="Creates an HTML page for the online directory")
        parser.add_argument('filename')
        parser.add_argument('-u', '--username')
        parser.add_argument('-p', '--password')
        parser.add_argument('-l', '--loglevel', default=logging.ERROR)
        commandline_args = parser.parse_args(sys.argv)

        error_handler = logging.StreamHandler(sys.stderr)
        logger = logging.getLogger()
        logger.setLevel(commandline_args.loglevel)
        logger.addHandler(error_handler)

        entrypoint(commandline_args, logger)

main()
