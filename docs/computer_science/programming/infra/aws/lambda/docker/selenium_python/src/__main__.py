
from selenium.webdriver import(
  Chrome,
  ChromeOptions,
)
from lib.sample_module import (
  sample_function,
)

def lambda_handler(
  event, 
  context,
):
  opt = ChromeOptions()
  opts = [
    '--no-sandbox',
    '--single-process',
    '--disable-dev-shm-usage',
    '--homedir=/tmp',
  ]
  opt.headless = True
  for o in opts:
    opt.add_argument(o)
  opt.binary_location = (
    '/opt/headless-chromium'
  )
  driver = Chrome(
    '/opt/chromedriver',
    options=opt,
  )
  driver.get(
    'http://httpbin.org/ip',
  )
  return {
      "statusCode": 200,
      "body": driver.page_source,
  }
