/*
Team 21 Deadly Sin Analysis
City: Melbourne
Team Members:
    Anupa Alex – 1016435
    Luiz Fernando Franco - 1019613
    Suraj Kumar Thakur - 999886
    Waneya Iqbal - 919750
    Yan Li – 984120
*/
//Map function to find count of all word in a suburb which are lustful
function (doc) {
function (doc) {
  lust_list = ['naughtycorner', 'lilbitkinky', 'wetpussy', 'lifemybaby', 'hornypussy', 'hownottobeadick', 'virginmobileaus', 'uravagina', 'httpstcobdsmdyssrn', 'httpstcoocrfwet', 'httpstcopstoycumo', 'jerkmindy', 'gorgeousday', 'breastcancerawareness', 'thatrainkissthough', 'tennispenis', 'sideboob', 'zoonabar', 'romanticdoes', 'eroticmassage', 'nudefoodday', 'kinkuji', 'nakedned', 'bikiniweather', 'lingeriemodel', 'twerkhottie', 'allaboutthecleavage', 'httptcoanalkr', 'httptcockoroniw', 'foodbooty', 'skyporn', 'drmarwank', 'macrobusinesslivetweetfuck', 'httpstcollauasexd', 'wonderlustmelbourne', 'orgasmos', 'debutsingle', 'thatgirleliana', 'whorefake', 'dirtystreetpiestripper', 'jesuispetite', 'bromance', 'toohot', 'bachatasensual', 'bigassfetishcom', 'jleehooker', 'alancumming', 'happyhumpday', 'yaasssssss', 'thongsdaily', 'merrychristmassexy', 'arabmuslimfck', 'lovelustandlonging', 'denimunderwear', 'slutwife','hookers', 'bars', 'booties', 'pussys', 'singles', 'boobs', 'breasts', 'kisses', 'kinks', 'assesses', 'wives', 'assess', 'virgins', 'bikinis', 'girlssssss', 'cums', 'babys', 'cocks', 'wifes', 'penises', 'whores', 'fetishes', 'pussies', 'vaginas', 'girls', 'fucks', 'jerks', 'orgasms', 'asses', 'thongs', 'babiessssss', 'sexes', 'babies', 'petites', 'dicks', 'nudes', 'romantics', 'strippers','hottie','hot','sexy','gorgeous','kinky','fetish','lust','seductive','seduce','lustforme','cock','penis','naked','fuck','sensual','sex','sesky','sensual','erotic','fuck','lust','cleavage','boobs','breasts','CleavageQueen','HumpDay','AssWednesday','Orgasm','sexpositive','HumpDayHappiness','Naughty','wetwednesday','bargirl','hooker','sexy','petite','ass','lbfm','bigtits','lingerie','bikini','Romance','Romantic','OneNightStand','bar','single','beingsingle','fck','fxck','kink','seduction','erotica','longing','wet','wetlook','nips','nippon','thong','underwear','stripper','vagina','virgin','ass','lustlegwear','horny','sexybaby','cum','cumshot','cumming','arousal','moaning','bdsm','couples','wife','kiss','booty','nude','nudes','fuckme','porn','hotgirl','momhot','cumtribute','cumslut','cockslut','whiteslut','tits','pussy','dick','cumonme','slutty','whore','anal','jerkoff','jerk','wank','masturbate','balls','boobies','collegeslut','cumwhore','teenslut','cocktribute','spankme','camsex']
  
  if(doc.coordinates!=null){
    doc.text.toLowerCase().split(" ").forEach(function (word) {
      if (lust_list.indexOf(word)>=0) {
         emit(doc.suburb_id, lust);
        
      }
      

    });
   
  }
}