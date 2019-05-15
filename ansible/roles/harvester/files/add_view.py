'''
Team 21 Deadly Sin Analysis
City: Melbourne
Team Members:
    Anupa Alex : 1016435
    Luiz Fernando Franco : 1019613
    Suraj Kumar Thakur : 999886
    Waneya Iqbal : 919750
    Yan Li : 984120
'''
#This file adds all the views to the corresponding database
from couchdb import design
import couchdb
import sys
USERNAME = 'admin'
PASSWORD = 'admin'
DATABASEADDRESS=sys.argv[1]
twitter_db_name = 'twitter_streaming'
instagram_db_name = 'instagram_data'
couch = couchdb.Server("http://%s:%s@%s:5984" % (USERNAME, PASSWORD,DATABASEADDRESS))
twitter_db = couch[twitter_db_name]
instagram_db = couch[instagram_db_name]
twitter_design = 'Twitter_Analysis'
instagram_design = 'Insta_Analysis'
def create_views(db_name,design_name,view_name,map_fun,reduce_fun):
	view = design.ViewDefinition(design_name, view_name, map_fun, reduce_fun=reduce_fun)
	view.sync(db_name)

#Views for twitter data analysis

#To create view for getting total count of words
map_fun = '''
function (doc) {
	if(doc.coordinates!=null){
	  doc.text.toLowerCase().split(" ").forEach(function (word) {	    
	       emit(doc.suburb_id, lust);
	  });
	 
	}
}'''
reduce_fun = '_sum'
view = 'count'

create_views(twitter_db,twitter_design,view,map_fun,reduce_fun)
#......................................................

#To create view for getting total count of lustful words
map_fun = '''
function (doc) {
	lust_list = ['naughtycorner', 'lilbitkinky', 'wetpussy', 'lifemybaby', 'hornypussy', 'hownottobeadick', 'virginmobileaus', 'uravagina', 'httpstcobdsmdyssrn', 'httpstcoocrfwet', 'httpstcopstoycumo', 'jerkmindy', 'gorgeousday', 'breastcancerawareness', 'thatrainkissthough', 'tennispenis', 'sideboob', 'zoonabar', 'romanticdoes', 'eroticmassage', 'nudefoodday', 'kinkuji', 'nakedned', 'bikiniweather', 'lingeriemodel', 'twerkhottie', 'allaboutthecleavage', 'httptcoanalkr', 'httptcockoroniw', 'foodbooty', 'skyporn', 'drmarwank', 'macrobusinesslivetweetfuck', 'httpstcollauasexd', 'wonderlustmelbourne', 'orgasmos', 'debutsingle', 'thatgirleliana', 'whorefake', 'dirtystreetpiestripper', 'jesuispetite', 'bromance', 'toohot', 'bachatasensual', 'bigassfetishcom', 'jleehooker', 'alancumming', 'happyhumpday', 'yaasssssss', 'thongsdaily', 'merrychristmassexy', 'arabmuslimfck', 'lovelustandlonging', 'denimunderwear', 'slutwife','hookers', 'bars', 'booties', 'pussys', 'singles', 'boobs', 'breasts', 'kisses', 'kinks', 'assesses', 'wives', 'assess', 'virgins', 'bikinis', 'girlssssss', 'cums', 'babys', 'cocks', 'wifes', 'penises', 'whores', 'fetishes', 'pussies', 'vaginas', 'girls', 'fucks', 'jerks', 'orgasms', 'asses', 'thongs', 'babiessssss', 'sexes', 'babies', 'petites', 'dicks', 'nudes', 'romantics', 'strippers','hottie','hot','sexy','gorgeous','kinky','fetish','lust','seductive','seduce','lustforme','cock','penis','naked','fuck','sensual','sex','sesky','sensual','erotic','fuck','lust','cleavage','boobs','breasts','CleavageQueen','HumpDay','AssWednesday','Orgasm','sexpositive','HumpDayHappiness','Naughty','wetwednesday','bargirl','hooker','sexy','petite','ass','lbfm','bigtits','lingerie','bikini','Romance','Romantic','OneNightStand','bar','single','beingsingle','fck','fxck','kink','seduction','erotica','longing','wet','wetlook','nips','nippon','thong','underwear','stripper','vagina','virgin','ass','lustlegwear','horny','sexybaby','cum','cumshot','cumming','arousal','moaning','bdsm','couples','wife','kiss','booty','nude','nudes','fuckme','porn','hotgirl','momhot','cumtribute','cumslut','cockslut','whiteslut','tits','pussy','dick','cumonme','slutty','whore','anal','jerkoff','jerk','wank','masturbate','balls','boobies','collegeslut','cumwhore','teenslut','cocktribute','spankme','camsex']
  
	if(doc.coordinates!=null){
	  doc.text.toLowerCase().split(" ").forEach(function (word) {
	    if (lust_list.indexOf(word)>=0) {
	       emit(doc.suburb_id, lust);
	      
	    }
	    

	  });
	 
	}
}'''
reduce_fun = '_sum'
view = 'count-lust'

create_views(twitter_db,twitter_design,view,map_fun,reduce_fun)
#......................................................





# To create view to count proud words
map_fun = '''
function (doc) {
	pride_list = ['own', 'mine', 'alone', 'theone', 'myself', 'self', 'self-love', 'best', 'better', 'iamthebest', 'iambetter', 'amourpropre', 'ego', 'egoism', 'egotism', 'pomposity', 'proud', 'self-admiration', 'self-assumption', 'self-conceit', 'self-congratulation', 'self-esteem', 'selfesteem', 'self-glory', 'self-importance', 'self-opinion', 'self-satisfaction', 'smugness', 'vanity', 'exellence', 'accomplishment', 'greatness', 'merit', 'perfection', 'purity', 'quality', 'supremacy', 'virtue', 'arete', 'class', 'distinction', 'eminence', 'excellency', 'fineness', 'goodness', 'preeminence', 'transcendence', 'worth', 'highquality', 'superbness', 'eclat', 'swelledhead', 'swellheadedness', 'vaingloriousness', 'vainglory', 'vainness', 'perfect', 'wisdom', 'wise', 'beauty', 'awesome', 'positivity', 'pride', 'fun', 'wonderful', 'different', 'heels', 'hard', 'faithful', 'selfie', 'honored', 'respected', 'respect', 'cool', 'style', 'beautiful', 'moda', 'fab', 'rare', 'pretty', 'cute', 'power', 'marvellous', 'wonderfull', 'high', 'fantastic', 'fabulous', 'amazing', 'real', 'smart', 'win', 'liveyourbestlife', 'mylife', 'iamawesome', 'feelinggood', 'lovingourlife', 'positivepower', 'weareawesome', 'bepositive', 'befun', 'beyourself', 'yourself', 'iammarvellous', 'iamwonderful', 'iamdifferent', 'naturalpic', 'highheels', 'realgirls', 'awesomeme', 'amfabulous', 'amrare', 'amdifferent', 'amreal', 'amoriginal', 'amfantastic', 'amwonderful', 'amblack', 'amfab', 'onfleek', 'havingablast', 'workhardplayhard', 'funinthesun', 'lifeisgood', 'lifeisbeautiful', 'somuchlove', 'somuchmore', 'havingfun', 'saturdaynight', 'nightout', 'selfienation', 'selfietime', 'justme', 'proudmom', 'prouddad', 'proudsis', 'proudbrother', 'feelingcute', 'feelingawesome', 'killinit', 'amcool', 'socool', 'amhip', 'amfaithful', 'amkind', 'amcute', 'ambeautiful', 'amhonored', 'amrespected', 'amhumble', 'amsmart', 'beingcool', 'beingawesome', 'beingperfect', 'ampretty', 'selfiemode', 'amhappy', 'amartsy', 'lovemylife', 'proudofmyself', 'blazetheworld', 'myawesomelife', 'stonerlife', 'beingthebest', 'feelinggreat', 'selflove', 'iloveme']
 
 //Only tweets that have coordinates 0 are considered
if(doc.coordinates!=null){
  doc.text.toLowerCase().split(" ").forEach(function (word) {
    if (pride_list.indexOf(word)>=0) {
      emit(doc.suburb_id, pride);
    }
  });
 
}
}'''
reduce_fun = '_sum'
view = 'count-pride'

create_views(twitter_db,twitter_design,view,map_fun,reduce_fun)

#Views for instagram data analysis

#To create view for getting total number of posts
map_fun = '''
function (doc) {
	if(doc.coordinates!=null){
  		emit(doc.suburb_id, 1);
}
}'''
reduce_fun = '_sum'
view = 'count'

create_views(instagram_db,instagram_design,view,map_fun,reduce_fun)
#......................................................

#To create view for getting total count of lustful posts
map_fun = '''
function (doc) {
	lust_list = ['naughtycorner', 'lilbitkinky', 'wetpussy', 'lifemybaby', 'hornypussy', 'hownottobeadick', 'virginmobileaus', 'uravagina', 'httpstcobdsmdyssrn', 'httpstcoocrfwet', 'httpstcopstoycumo', 'jerkmindy', 'gorgeousday', 'breastcancerawareness', 'thatrainkissthough', 'tennispenis', 'sideboob', 'zoonabar', 'romanticdoes', 'eroticmassage', 'nudefoodday', 'kinkuji', 'nakedned', 'bikiniweather', 'lingeriemodel', 'twerkhottie', 'allaboutthecleavage', 'httptcoanalkr', 'httptcockoroniw', 'foodbooty', 'skyporn', 'drmarwank', 'macrobusinesslivetweetfuck', 'httpstcollauasexd', 'wonderlustmelbourne', 'orgasmos', 'debutsingle', 'thatgirleliana', 'whorefake', 'dirtystreetpiestripper', 'jesuispetite', 'bromance', 'toohot', 'bachatasensual', 'bigassfetishcom', 'jleehooker', 'alancumming', 'happyhumpday', 'yaasssssss', 'thongsdaily', 'merrychristmassexy', 'arabmuslimfck', 'lovelustandlonging', 'denimunderwear', 'slutwife','hookers', 'bars', 'booties', 'pussys', 'singles', 'boobs', 'breasts', 'kisses', 'kinks', 'assesses', 'wives', 'assess', 'virgins', 'bikinis', 'girlssssss', 'cums', 'babys', 'cocks', 'wifes', 'penises', 'whores', 'fetishes', 'pussies', 'vaginas', 'girls', 'fucks', 'jerks', 'orgasms', 'asses', 'thongs', 'babiessssss', 'sexes', 'babies', 'petites', 'dicks', 'nudes', 'romantics', 'strippers','hottie','hot','sexy','gorgeous','kinky','fetish','lust','seductive','seduce','lustforme','cock','penis','naked','fuck','sensual','sex','sesky','sensual','erotic','fuck','lust','cleavage','boobs','breasts','CleavageQueen','HumpDay','AssWednesday','Orgasm','sexpositive','HumpDayHappiness','Naughty','wetwednesday','bargirl','hooker','sexy','petite','ass','lbfm','bigtits','lingerie','bikini','Romance','Romantic','OneNightStand','bar','single','beingsingle','fck','fxck','kink','seduction','erotica','longing','wet','wetlook','nips','nippon','thong','underwear','stripper','vagina','virgin','ass','lustlegwear','horny','sexybaby','cum','cumshot','cumming','arousal','moaning','bdsm','couples','wife','kiss','booty','nude','nudes','fuckme','porn','hotgirl','momhot','cumtribute','cumslut','cockslut','whiteslut','tits','pussy','dick','cumonme','slutty','whore','anal','jerkoff','jerk','wank','masturbate','balls','boobies','collegeslut','cumwhore','teenslut','cocktribute','spankme','camsex']
  
	if(doc.coordinates!=null){
	  doc.text.toLowerCase().split(" ").forEach(function (word) {
	    if (lust_list.indexOf(word)>=0) {
	       emit(doc.suburb_id, lust);
	      
	    }
	    

	  });
	 
	}
}'''
reduce_fun = '_sum'
view = 'count-lust'

create_views(instagram_db,instagram_design,view,map_fun,reduce_fun)
#......................................................





# To create view to count proud posts
map_fun = '''
function (doc) {
	pride_list = ['own', 'mine', 'alone', 'theone', 'myself', 'self', 'self-love', 'best', 'better', 'iamthebest', 'iambetter', 'amourpropre', 'ego', 'egoism', 'egotism', 'pomposity', 'proud', 'self-admiration', 'self-assumption', 'self-conceit', 'self-congratulation', 'self-esteem', 'selfesteem', 'self-glory', 'self-importance', 'self-opinion', 'self-satisfaction', 'smugness', 'vanity', 'exellence', 'accomplishment', 'greatness', 'merit', 'perfection', 'purity', 'quality', 'supremacy', 'virtue', 'arete', 'class', 'distinction', 'eminence', 'excellency', 'fineness', 'goodness', 'preeminence', 'transcendence', 'worth', 'highquality', 'superbness', 'eclat', 'swelledhead', 'swellheadedness', 'vaingloriousness', 'vainglory', 'vainness', 'perfect', 'wisdom', 'wise', 'beauty', 'awesome', 'positivity', 'pride', 'fun', 'wonderful', 'different', 'heels', 'hard', 'faithful', 'selfie', 'honored', 'respected', 'respect', 'cool', 'style', 'beautiful', 'moda', 'fab', 'rare', 'pretty', 'cute', 'power', 'marvellous', 'wonderfull', 'high', 'fantastic', 'fabulous', 'amazing', 'real', 'smart', 'win', 'liveyourbestlife', 'mylife', 'iamawesome', 'feelinggood', 'lovingourlife', 'positivepower', 'weareawesome', 'bepositive', 'befun', 'beyourself', 'yourself', 'iammarvellous', 'iamwonderful', 'iamdifferent', 'naturalpic', 'highheels', 'realgirls', 'awesomeme', 'amfabulous', 'amrare', 'amdifferent', 'amreal', 'amoriginal', 'amfantastic', 'amwonderful', 'amblack', 'amfab', 'onfleek', 'havingablast', 'workhardplayhard', 'funinthesun', 'lifeisgood', 'lifeisbeautiful', 'somuchlove', 'somuchmore', 'havingfun', 'saturdaynight', 'nightout', 'selfienation', 'selfietime', 'justme', 'proudmom', 'prouddad', 'proudsis', 'proudbrother', 'feelingcute', 'feelingawesome', 'killinit', 'amcool', 'socool', 'amhip', 'amfaithful', 'amkind', 'amcute', 'ambeautiful', 'amhonored', 'amrespected', 'amhumble', 'amsmart', 'beingcool', 'beingawesome', 'beingperfect', 'ampretty', 'selfiemode', 'amhappy', 'amartsy', 'lovemylife', 'proudofmyself', 'blazetheworld', 'myawesomelife', 'stonerlife', 'beingthebest', 'feelinggreat', 'selflove', 'iloveme']
 
 //Only tweets that have coordinates 0 are considered
if(doc.coordinates!=null){
  doc.text.toLowerCase().split(" ").forEach(function (word) {
    if (pride_list.indexOf(word)>=0) {
      emit(doc.suburb_id, pride);
    }
  });
 
}
}'''
reduce_fun = '_sum'
view = 'count-pride'

create_views(instagram_db,instagram_design,view,map_fun,reduce_fun)

