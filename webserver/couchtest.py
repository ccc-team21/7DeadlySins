import couchdb

couch = couchdb.Server('http://admin:muzifeng1021@127.0.0.1:5984')
db = couch["twitter"]

doc = { "1": {
    "count": 28,
    "name": "fairfield"
  },
  "2": {
    "count": 68,
    "name": "thornbury"
  },
  "3": {
    "count": 169,
    "name": "northcote"
  },
  "4": {
    "count": 20,
    "name": "clifton hill"
  },
  "5": {
    "count": 107,
    "name": "abbotsford"
  },
  "6": {
    "count": 95,
    "name": "fitzroy north"
  },
  "7": {
    "count": 56,
    "name": "brunswick east"
  },
  "8": {
    "count": 142,
    "name": "collingwood"
  },
  "9": {
    "count": 596,
    "name": "fitzroy"
  },
  "10": {
    "count": 199,
    "name": "brunswick"
  },
  "11": {
    "count": 25,
    "name": "princes hill"
  },
  "12": {
    "count": 52,
    "name": "carlton north"
  },
  "13": {
    "count": 196,
    "name": "carlton"
  },
  "14": {
    "count": 77,
    "name": "parkville"
  },
  "15": {
    "count": 3368,
    "name": "melbourne (3000)"
  },
  "16": {
    "count": 17,
    "name": "balwyn north"
  },
  "17": {
    "count": 1,
    "name": "kingsbury"
  },
  "18": {
    "count": 10,
    "name": "kew east"
  },
  "19": {
    "count": 1,
    "name": "deepdene"
  },
  "20": {
    "count": 42,
    "name": "kew"
  },
  "21": {
    "count": 13,
    "name": "canterbury"
  },
  "22": {
    "count": 49,
    "name": "camberwell"
  },
  "23": {
    "count": 54,
    "name": "hawthorn east"
  },
  "24": {
    "count": 15,
    "name": "balwyn"
  },
  "25": {
    "count": 86,
    "name": "preston"
  },
  "26": {
    "count": 130,
    "name": "hawthorn"
  },
  "27": {
    "count": 13,
    "name": "burnley"
  },
  "28": {
    "count": 275,
    "name": "richmond"
  },
  "29": {
    "count": 81,
    "name": "east melbourne"
  },
  "30": {
    "count": 282,
    "name": "south yarra"
  },
  "31": {
    "count": 35,
    "name": "cremorne"
  },
  "32": {
    "count": 68,
    "name": "toorak"
  },
  "33": {
    "count": 0,
    "name": "kooyong"
  },
  "34": {
    "count": 31,
    "name": "glen iris"
  },
  "35": {
    "count": 97,
    "name": "north melbourne"
  },
  "36": {
    "count": 34,
    "name": "brunswick west"
  },
  "37": {
    "count": 26,
    "name": "coburg north"
  },
  "38": {
    "count": 85,
    "name": "reservoir"
  },
  "39": {
    "count": 27,
    "name": "malvern"
  },
  "40": {
    "count": 45,
    "name": "coburg"
  },
  "41": {
    "count": 15,
    "name": "fawkner"
  },
  "42": {
    "count": 8,
    "name": "ashburton"
  },
  "43": {
    "count": 42,
    "name": "armadale"
  },
  "44": {
    "count": 62,
    "name": "malvern east"
  },
  "45": {
    "count": 5,
    "name": "hadfield"
  },
  "46": {
    "count": 180,
    "name": "prahran"
  },
  "47": {
    "count": 79,
    "name": "caulfield north"
  },
  "48": {
    "count": 477,
    "name": "southbank"
  },
  "49": {
    "count": 13,
    "name": "pascoe vale south"
  },
  "50": {
    "count": 119,
    "name": "windsor"
  },
  "51": {
    "count": 15,
    "name": "caulfield east"
  },
  "52": {
    "count": 7,
    "name": "travancore"
  },
  "53": {
    "count": 13,
    "name": "pascoe vale"
  },
  "54": {
    "count": 39,
    "name": "st kilda east"
  },
  "55": {
    "count": 170,
    "name": "south melbourne"
  },
  "56": {
    "count": 6,
    "name": "caulfield"
  },
  "57": {
    "count": 40,
    "name": "essendon"
  },
  "58": {
    "count": 33,
    "name": "carnegie"
  },
  "59": {
    "count": 85,
    "name": "south wharf"
  },
  "60": {
    "count": 66,
    "name": "albert park"
  },
  "61": {
    "count": 5,
    "name": "murrumbeena"
  },
  "62": {
    "count": 394,
    "name": "st kilda"
  },
  "63": {
    "count": 44,
    "name": "balaclava"
  },
  "64": {
    "count": 257,
    "name": "docklands"
  },
  "65": {
    "count": 13,
    "name": "glen huntly"
  },
  "66": {
    "count": 32,
    "name": "glenroy"
  },
  "67": {
    "count": 63,
    "name": "kensington"
  },
  "68": {
    "count": 10,
    "name": "ripponlea"
  },
  "69": {
    "count": 8,
    "name": "hughesdale"
  },
  "70": {
    "count": 7,
    "name": "middle park"
  },
  "71": {
    "count": 45,
    "name": "st kilda west"
  },
  "72": {
    "count": 11,
    "name": "strathmore"
  },
  "73": {
    "count": 82,
    "name": "moonee ponds"
  },
  "74": {
    "count": 67,
    "name": "flemington"
  },
  "75": {
    "count": 3,
    "name": "oak park"
  },
  "76": {
    "count": 30,
    "name": "ascot vale"
  },
  "77": {
    "count": 42,
    "name": "elsternwick"
  },
  "78": {
    "count": 53,
    "name": "west melbourne"
  },
  "79": {
    "count": 8,
    "name": "caulfield south"
  },
  "80": {
    "count": 35,
    "name": "ormond"
  },
  "81": {
    "count": 83,
    "name": "elwood"
  },
  "82": {
    "count": 7,
    "name": "essendon fields"
  },
  "83": {
    "count": 2,
    "name": "gardenvale"
  },
  "84": {
    "count": 5,
    "name": "essendon north"
  },
  "85": {
    "count": 26,
    "name": "mckinnon"
  },
  "86": {
    "count": 5,
    "name": "aberfeldie"
  },
  "87": {
    "count": 44,
    "name": "gowanbrae"
  },
  "88": {
    "count": 0,
    "name": "strathmore heights"
  },
  "89": {
    "count": 18,
    "name": "bentleigh"
  },
  "90": {
    "count": 31,
    "name": "brighton east"
  },
  "91": {
    "count": 91,
    "name": "footscray"
  },
  "92": {
    "count": 80,
    "name": "port melbourne"
  },
  "93": {
    "count": 45,
    "name": "maribyrnong"
  },
  "94": {
    "count": 42,
    "name": "bentleigh east"
  },
  "95": {
    "count": 84,
    "name": "brighton"
  },
  "96": {
    "count": 0,
    "name": "essendon west"
  },
  "97": {
    "count": 21,
    "name": "niddrie"
  },
  "98": {
    "count": 15,
    "name": "seddon"
  },
  "99": {
    "count": 8,
    "name": "airport west"
  },
  "100": {
    "count": 3,
    "name": "hampton east"
  },
  "101": {
    "count": 53,
    "name": "yarraville"
  },
  "102": {
    "count": 11,
    "name": "spotswood"
  },
  "103": {
    "count": 24,
    "name": "maidstone"
  },
  "104": {
    "count": 39,
    "name": "hampton"
  },
  "105": {
    "count": 25,
    "name": "newport"
  },
  "106": {
    "count": 22,
    "name": "avondale heights"
  },
  "107": {
    "count": 15,
    "name": "kingsville"
  },
  "108": {
    "count": 32,
    "name": "west footscray"
  },
  "109": {
    "count": 64,
    "name": "williamstown"
  },
  "110": {
    "count": 17,
    "name": "sandringham"
  },
  "111": {
    "count": 1,
    "name": "south kingsville"
  },
  "112": {
    "count": 26,
    "name": "braybrook"
  },
  "113": {
    "count": 0,
    "name": "tottenham"
  },
  "114": {
    "count": 42,
    "name": "black rock"
  },
  "115": {
    "count": 4,
    "name": "williamstown north"
  },
  "116": {
    "count": 11,
    "name": "beaumaris"
  },
  "117": {
    "count": 11,
    "name": "altona north"
  },
  "118": {
    "count": 32,
    "name": "altona"
  },
  "119": {
    "count": 9,
    "name": "altona meadows"
  },
  "120": {
    "count": 1,
    "name": "seaholme"
  },
  "121": {
    "count": 4,
    "name": "seabrook"
  },
  "122": {
    "count": 145,
    "name": "melbourne (3004)"
  }}

db.save(doc)




