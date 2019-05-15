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
//Map function to find count of all word in a suburb which are proud
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
}
