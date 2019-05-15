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
function (doc) {
  lust = 0
  pride = 0
  if(doc.is_nude){
    lust = 1;
  }
  if(doc.face_count==1){
    pride = 1
  }  
  emit(doc._id,{suburb_id:doc.suburb_id,lust:lust,pride:pride,count:1});
  
}

