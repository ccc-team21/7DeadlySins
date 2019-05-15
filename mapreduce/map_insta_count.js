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
//Map function to find count of all instagram posts in a suburb
function (doc) {
  emit(doc.suburb_id, 1);
}
