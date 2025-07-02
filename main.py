from DrissionPage.common import Settings
from DrissionPage import ChromiumPage,ChromiumOptions

from fake_useragent import UserAgent


Settings.set_language('en')

options = ChromiumOptions()

options.incognito(True)
options.headless(False)

options.set_argument('--window-size=1920,1080')
options.set_argument('--start-maximized')

user_agent_random = UserAgent(browsers=['Edge','Chromium','Firefox','Opera','Chrome'])
options.set_argument(f'--user-agent={user_agent_random.random}')



def main():
    page = ChromiumPage(options)
    
    try:
        page.get('https://laptop-ventas.olaclick.menu/',timeout=10)
        
        if page._wait_loaded():
            button_catalogo = page.ele('xpath://button[.//span[normalize-space()="Catálogo 📋"]]')
            button_catalogo.click()
            
            print('Everithing is ok')
            
    except Exception as e:
        print(f'Error: {e}')
        

main()