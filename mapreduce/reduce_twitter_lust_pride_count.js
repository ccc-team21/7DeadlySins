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
//Reduce function to summarise of all words, count of lustful words and proud words in a suburb
function (keys, values, rereduce) {
  var result_lust = 0;
  var result_pride = 0;
  var result_count = 0
  var suburbs_lust = [];
  var suburbs_pride = [];
  var suburbs_count = [];
  for(i=0;i<123;i++){
    suburbs_lust.push(0);
    suburbs_pride.push(0);
    suburbs_count.push(0);
  }
  if (rereduce) {
    values.forEach(function (v) {
      result_lust += v.result_lust;
      result_pride += v.result_pride;
      result_count += v.result_count;
      for(i=0;i<123;i++){
        suburbs_lust[i]+=v.suburbs_lust[i];
        suburbs_pride[i]+=v.suburbs_pride[i];
        suburbs_count[i]+=v.suburbs_count[i];
      }
    });
  } else {
    values.forEach(function (vObj) {
      result_lust += vObj.lust;
      result_pride += vObj.pride;
      result_count += vObj.count;
      suburbs_lust[vObj.suburb_id]+=vObj.lust;
      suburbs_pride[vObj.suburb_id]+=vObj.pride;
      suburbs_count[vObj.suburb_id]+=vObj.count;
      
    });
  }
  return ({result_lust:result_lust,result_pride:result_pride,result_count:result_count,suburbs_lust:suburbs_lust,suburbs_pride:suburbs_pride,suburbs_count:suburbs_count});
}
