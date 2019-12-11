import operator
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

doubleclicknet = ['Youtube', 'Target', 'Best Buy', 'eBay', 'H&M','BBC','NYTimes','Washington Post','Google News','Google News','BBC News','USA TODAY','CNBC','Best Buy','eBay','H&M','Guardian']
googlesyndication = ['Youtube','NYTimes','Washington Post','Google News','BBC','WSJ','USA TODAY','CNBC']
urbanairship = ['Home Depot','BBC','WSJ','USA TODAY','CNBC']
assetsadobe = ['Best Buy','A&F']
apptentative = ['eBay','A&F','CNBC']
branchio = ['Pinterest','Reddit','Macys','A&F']
omtrdcnet = ['Macys','H&M','A&F']
accountkit =['Pinterest','Facebook']
ampprojectorg = ['Google News','CNBC']
#doubleclick.net = ['NYTimes','Washington Post','Google News','BBC News','USA Today','CNBC','Best Buy','eBay','H&M']
insightexpressai = ['Washington Post','USA TODAY','CNBC','Youtube']
crashlyticscom = ['Reddit','Indeed','Guardian','NYTimes','Washington Post','WSJ','USA TODAY','Target','Walmart','Home Depot','IKEA Store','eBay','H&M','Pinterest']
appsflyercom = ['Reddit','Tumblr','Washington Post','WSJ','Macys','Indeed']
googleanalyticscom = ['NYTimes','Indeed']
scorecardresearchcom = ['NYTimes','Washington Post','Yahoo News','BBC News','CNBC','Indeed']
adsafeprotectedcom = ['USA TODAY','CNBC','Washington Post','WSJ']
amazonadsystemcom = ['NYTimes','USA TODAY','Amazon Shopping','Washington Post']
omtrdcnet = ['CNBC','A&F','Macys','H&M','WSJ']
#sectigocom = ['ebay','BBC','WSJ']
sectigocom = ['BBC','eBay','WSJ']
adobedtmcom =['A&F','Best Buy','CNBC']
#adsafeprotected =['Washington Post','USA Today','CNBC']
#demdex.net = ['Best Buy','H&M','A&F']
demdexnet =['A&F','Best Buy','H&M']
doubleverifycom =['Washington Post','USA TODAY','CNBC']
#omtrdcnet =['WSJ','A&F','Macys','H&M','CNBC']

dict = {}
dict['doubleclick.net'] = len(doubleclicknet)
dict['googlesyndication'] = len(googlesyndication)
dict['sectigo']=len(sectigocom)
dict['urbanairship'] = len(urbanairship)
dict['assetsadobe'] = len(assetsadobe)
dict['apptentative']= len(apptentative)
dict['branch.io']=len(branchio)
dict['omtrdc.net']=len(omtrdcnet)
dict['accountkit']=len(accountkit)
dict['ampproject.org']=len(ampprojectorg)
dict['insightexpress.ai']=len(insightexpressai)
dict['crashlytics.com']=len(crashlyticscom)
dict['appsflyer.com']=len(appsflyercom)
dict['googleanalytics.com']=len(googleanalyticscom)
dict['scorecardresearch.com']=len(scorecardresearchcom)
dict['adsafeprotected.com']=len(adsafeprotectedcom)
dict['amazonsystem.com']=len(amazonadsystemcom)
dict['omtrdc.net']=len(omtrdcnet)
#dict['sectigo.com']=len(sectigocom)
dict['adobetm.com']=len(adobedtmcom)
#dict['adsafeprotected']=len(adsafeprotected)
dict['demdexnet']=len(demdexnet)
dict['doubleverify.com']=len(doubleverifycom)
s = ['a','b',]
print(dict)
print(s)
sorted_d = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_d)

common_trackers = [17,14,8,6,6,5,5,4,4,4]#,4,3,3,3,3,3,3,2,2,2]
objects = ('doubleclick.net', 'crashlytics.com', 'googlesyndication', 'appsflyer', 'scorecardresearch', 'omtrdc.net','urbanairship','branch.io','insightexpress','amazonsystem','adsafeprotected.com','demdex.net','sectigo.com','apptentative','adobetm.com','doubleverify.com','assetsadobe.com','googleanalytics.com','ampproject.org','accountkit')
y_pos = np.arange(len(objects))
print(len(objects))
print(type(objects))
print(len(common_trackers))
i = 0
height_bars = plt.bar(y_pos, common_trackers, align='center', width = 0.3 ,alpha=0.5,color = 'blue')
for rect in height_bars:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, objects[i], ha='center', va='bottom')
    i = i + 1
plt.title('Most common trackers across 30 apps')
#plt.xticks(y_pos)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) 
plt.ylabel('Number of apps that tracker is present in')
plt.show()

trackers = set()
website = set()
website.add('Youtube')
website.add('Target')
website.add('Best Buy')
website.add('eBay')
website.add('H&M')
website.add('BBC')
website.add('NYTimes')
website.add('Washington Post')
website.add('Google News')
website.add('BBC News')
website.add('USA TODAY')
website.add('CNBC')
website.add('Best Buy')
website.add('eBay')
website.add('H&M')
website.add('Guardian')
website.add('WSJ')
website.add('Home Depot')
website.add('A&F')
website.add('Pinterest')
website.add('Reddit')
website.add('Macys')
website.add('Facebook')
website.add('Indeed')
website.add('Guardian')
website.add('Walmart')
website.add('IKEA Store')
website.add('Yahoo News')
website.add('Amazon Shopping')
print(website)