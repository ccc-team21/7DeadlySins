/*
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
*/
//Map function to find count of all words, count of lustful words and proud words in a suburb
function (doc) {
  lust_list = ['naughtycorner', 'lilbitkinky', 'wetpussy', 'lifemybaby', 'hornypussy', 'hownottobeadick', 'virginmobileaus', 'uravagina', 'httpstcobdsmdyssrn', 'httpstcoocrfwet', 'httpstcopstoycumo', 'jerkmindy', 'gorgeousday', 'breastcancerawareness', 'thatrainkissthough', 'tennispenis', 'sideboob', 'zoonabar', 'romanticdoes', 'eroticmassage', 'nudefoodday', 'kinkuji', 'nakedned', 'bikiniweather', 'lingeriemodel', 'twerkhottie', 'allaboutthecleavage', 'httptcoanalkr', 'httptcockoroniw', 'foodbooty', 'skyporn', 'drmarwank', 'macrobusinesslivetweetfuck', 'httpstcollauasexd', 'wonderlustmelbourne', 'orgasmos', 'debutsingle', 'thatgirleliana', 'whorefake', 'dirtystreetpiestripper', 'jesuispetite', 'bromance', 'toohot', 'bachatasensual', 'bigassfetishcom', 'jleehooker', 'alancumming', 'happyhumpday', 'yaasssssss', 'thongsdaily', 'merrychristmassexy', 'arabmuslimfck', 'lovelustandlonging', 'denimunderwear', 'slutwife','hookers', 'bars', 'booties', 'pussys', 'singles', 'boobs', 'breasts', 'kisses', 'kinks', 'assesses', 'wives', 'assess', 'virgins', 'bikinis', 'girlssssss', 'cums', 'babys', 'cocks', 'wifes', 'penises', 'whores', 'fetishes', 'pussies', 'vaginas', 'girls', 'fucks', 'jerks', 'orgasms', 'asses', 'thongs', 'babiessssss', 'sexes', 'babies', 'petites', 'dicks', 'nudes', 'romantics', 'strippers','hottie','hot','sexy','gorgeous','kinky','fetish','lust','seductive','seduce','lustforme','cock','penis','naked','fuck','sensual','sex','sesky','sensual','erotic','fuck','lust','cleavage','boobs','breasts','CleavageQueen','HumpDay','AssWednesday','Orgasm','sexpositive','HumpDayHappiness','Naughty','wetwednesday','bargirl','hooker','sexy','petite','ass','lbfm','bigtits','lingerie','bikini','Romance','Romantic','OneNightStand','bar','single','beingsingle','fck','fxck','kink','seduction','erotica','longing','wet','wetlook','nips','nippon','thong','underwear','stripper','vagina','virgin','ass','lustlegwear','horny','sexybaby','cum','cumshot','cumming','arousal','moaning','bdsm','couples','wife','kiss','booty','nude','nudes','fuckme','porn','hotgirl','momhot','cumtribute','cumslut','cockslut','whiteslut','tits','pussy','dick','cumonme','slutty','whore','anal','jerkoff','jerk','wank','masturbate','balls','boobies','collegeslut','cumwhore','teenslut','cocktribute','spankme','camsex']
  pride_list = ['own', 'mine', 'alone', 'theone', 'myself', 'self', 'self-love', 'best', 'better', 'iamthebest', 'iambetter', 'amourpropre', 'ego', 'egoism', 'egotism', 'pomposity', 'proud', 'self-admiration', 'self-assumption', 'self-conceit', 'self-congratulation', 'self-esteem', 'selfesteem', 'self-glory', 'self-importance', 'self-opinion', 'self-satisfaction', 'smugness', 'vanity', 'exellence', 'accomplishment', 'greatness', 'merit', 'perfection', 'purity', 'quality', 'supremacy', 'virtue', 'arete', 'class', 'distinction', 'eminence', 'excellency', 'fineness', 'goodness', 'preeminence', 'transcendence', 'worth', 'highquality', 'superbness', 'eclat', 'swelledhead', 'swellheadedness', 'vaingloriousness', 'vainglory', 'vainness', 'perfect', 'wisdom', 'wise', 'beauty', 'awesome', 'positivity', 'pride', 'fun', 'wonderful', 'different', 'heels', 'hard', 'faithful', 'selfie', 'honored', 'respected', 'respect', 'cool', 'style', 'beautiful', 'moda', 'fab', 'rare', 'pretty', 'cute', 'power', 'marvellous', 'wonderfull', 'high', 'fantastic', 'fabulous', 'amazing', 'real', 'smart', 'win', 'liveyourbestlife', 'mylife', 'iamawesome', 'feelinggood', 'lovingourlife', 'positivepower', 'weareawesome', 'bepositive', 'befun', 'beyourself', 'yourself', 'iammarvellous', 'iamwonderful', 'iamdifferent', 'naturalpic', 'highheels', 'realgirls', 'awesomeme', 'amfabulous', 'amrare', 'amdifferent', 'amreal', 'amoriginal', 'amfantastic', 'amwonderful', 'amblack', 'amfab', 'onfleek', 'havingablast', 'workhardplayhard', 'funinthesun', 'lifeisgood', 'lifeisbeautiful', 'somuchlove', 'somuchmore', 'havingfun', 'saturdaynight', 'nightout', 'selfienation', 'selfietime', 'justme', 'proudmom', 'prouddad', 'proudsis', 'proudbrother', 'feelingcute', 'feelingawesome', 'killinit', 'amcool', 'socool', 'amhip', 'amfaithful', 'amkind', 'amcute', 'ambeautiful', 'amhonored', 'amrespected', 'amhumble', 'amsmart', 'beingcool', 'beingawesome', 'beingperfect', 'ampretty', 'selfiemode', 'amhappy', 'amartsy', 'lovemylife', 'proudofmyself', 'blazetheworld', 'myawesomelife', 'stonerlife', 'beingthebest', 'feelinggreat', 'selflove', 'iloveme']
  lust = 0
  pride = 0
  //lust_words = []
  //pride_words = []
  words = []
  doc.text.toLowerCase().split(" ").forEach(function (word) {
    words.push(word)
    if (lust_list.indexOf(word)>=0) {
      lust = 1;
     

    }
    if (pride_list.indexOf(word)>=0) {
      pride = 1;
      
    }

  });
  emit(doc._id,{suburb_id:doc.suburb_id,lust:lust,pride:pride,count:1});
  
}


