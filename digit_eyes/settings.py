# Scrapy settings for digit_eyes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'digit_eyes'

SPIDER_MODULES = ['digit_eyes.spiders']
NEWSPIDER_MODULE = 'digit_eyes.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'digit_eyes (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_IP = 9

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    'digit_eyes.middlewares.DigitEyesSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#    'digit_eyes.middlewares.DigitEyesDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
ITEM_PIPELINES = {
    'digit_eyes.pipelines.DigitEyesPipeline': None,
    'digit_eyes.pipelines.CustomImagesPipeline': 1,
}
IMAGES_STORE = 'images'
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False