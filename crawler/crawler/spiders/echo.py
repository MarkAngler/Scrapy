from pathlib import Path
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Echo

# https://api.bazaarvoice.com/data/products.json?passkey=m466omwtor2bbn5emh8n30kg5&locale=en_US&allowMissing=true&apiVersion=5.4&filter=id:DCS-2500T
# https://api.bazaarvoice.com/data/products.json?resource=products&filter=id%3Aeq%3ADCS-2500T&filter_reviews=contentlocale%3Aeq%3Aen_MX%2Cen_US%2Cen_US&filter_reviewcomments=contentlocale%3Aeq%3Aen_MX%2Cen_US%2Cen_US&filteredstats=Reviews&stats=Reviews&passkey=m466omwtor2bbn5emh8n30kg5&apiversion=5.5&displaycode=9581_2_0-en_us

# apiUrl = "https://api.bazaarvoice.com/data/products.json"




class EchoSpider(CrawlSpider):
    name = 'EchoChainsaws'
    allowed_domains = ['echo-usa.com']
    start_urls = ['https://www.echo-usa.com/chainsaws/dcs-2500t']
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    

    # Define the rules for which URLs to follow
    rules = (
        Rule(LinkExtractor(allow=('/chainsaws/', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log('Visited %s' % response.url)
        echo_item = Echo()
        echo_item['title'] = response.css('title::text').get()
        echo_item['price'] = response.css('.fw-bold.mb-3::text').getall()
        yield echo_item