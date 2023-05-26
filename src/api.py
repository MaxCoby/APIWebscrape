import requests
import json

def yelp(search, location, radius):
    list_of_names = []
    list_of_ratings = []
    list_of_addresses = []
    list_of_yelp = "https://api.yelp.com/v3/businesses/search\nUsing Yelp API - Yelp listings for: " \
                   + search + " in a " + radius + " meter radius of " + location +"\n"

    API_key = "0vxh3O8kZdWX2R6cSwuG8lr6EzyzTIFWS32kKIt7HMlWYQuZCrtIaktyBorp4nWwJ6uhMvSCPvaEcNHwLMlWBzM81p_Dtelo_--IKOXJSwoZwnv2uyXoahuwh-3ZW3Yx"

    header_data = { "Authorization" : "Bearer " + API_key }
    param_data = { "term" : search, "location" : location, "radius" : radius }
    endpoint = "https://api.yelp.com/v3/businesses/search"
    response = requests.get(endpoint, headers=header_data, params=param_data)
    response_data = json.loads(response.text)

    if (len(response_data["businesses"]) == 0):
        return "Nothing Found\n"

    for i in range(0, len(response_data["businesses"])):
        list_of_names.append(response_data["businesses"][i]["name"])
        list_of_ratings.append(response_data["businesses"][i]["rating"])
        list_of_addresses.append(response_data["businesses"][i]["location"]["display_address"][0] + ", " +
                                 response_data["businesses"][i]["location"]["display_address"][1])

    for i in range(0, len(list_of_names)):
        list_of_yelp += ("Name: " + list_of_names[i] + " ||| " + "Rating: " + str(list_of_ratings[i]) +
                         " ||| " + "Address: " + list_of_addresses[i] + "\n")

    return list_of_yelp

def detect_langauge(text):
    languages = {
        "aa" : "Afar",
        "ab" : "Abkhazian",
        "af" : "Afrikaans",
        "ak" : "Akan",
        "am" : "Amharic",
        "ar" : "Arabic",
        "as" : "Assamese",
        "ay" : "Aymara",
        "az" : "Azerbaijani",
        "ba" : "Bashkir",
        "be" : "Belarusian",
        "bg" : "Bulgarian",
        "bh" : "Bihari",
        "bi" : "Bislama",
        "bn" : "Bengali",
        "bo" : "Tibetan",
        "br" : "Breton",
        "bs" : "Bosnian",
        "bug" : "Buginese",
        "ca" : "Catalan",
        "ceb" : "Cebuano",
        "chr" : "Cherokee",
        "co" : "Corsican",
        "crs" : "Seselwa",
        "cs" : "Czech",
        "cy" : "Welsh",
        "da" : "Danish",
        "de" : "erman",
        "dv" : "Dhivehi",
        "dz" : "Dzongkha",
        "egy" : "Egyptian",
        "el" : "Greek",
        "en" : "English",
        "eo" : "Esperanto",
        "es" : "Spanish",
        "et" : "Estonian",
        "eu" : "Basque",
        "fa" : "Persian",
        "fi" : "Finnish",
        "fj" : "Fijian",
        "fo" : "Faroese",
        "fr" : "French",
        "fy" : "Frisian",
        "ga" : "Irish",
        "gd" : "Scots Gaelic",
        "gl" : "Galician",
        "gn" : "Guarani",
        "got" : "Gothic",
        "gu" : "Gujarati",
        "gv" : "Manx",
        "ha" : "Hausa",
        "haw" : "Hawaiian",
        "hi" : "Hindi",
        "hmn" : "Hmong",
        "hr" : "Croatian",
        "ht" : "Haitian Creole",
        "hu" : "Hungarian",
        "hy" : "Armenian",
        "ia" : "Interlingua",
        "id" : "Indonesian",
        "ie" : "Interlingue",
        "ig" : "Igbo",
        "ik" : "Inupiak",
        "is" : "Icelandic",
        "it" : "Italian",
        "iu" : "Inuktitut",
        "iw" : "Hebrew",
        "ja" : "Japanese",
        "jw" : "Javanese",
        "ka" : "Georgian",
        "kha" : "Khasi",
        "kk" : "Kazakh",
        "kl" : "Greenlandic",
        "km" : "Khmer",
        "kn" : "Kannada",
        "ko" : "Korean",
        "ks" : "Kashmiri",
        "ku" : "Kurdish",
        "ky" : "Kyrgyz",
        "la" : "Latin",
        "lb" : "Luxembourgish",
        "lg" : "Ganda",
        "lif" : "Limbu",
        "ln" : "Lingala",
        "lo" : "Laothian",
        "lt" : "Lithuanian",
        "lv" : "Latvian",
        "mfe" : "Mauritian Creole",
        "mg" : "Malagasy",
        "mi" : "Maori",
        "mk" : "Macedonian",
        "ml" : "Malayalam",
        "mn" : "Mongolian",
        "mr" : "Marathi",
        "ms" : "Malay",
        "mt" : "Maltese",
        "my" : "Burmese",
        "na" : "Nauru",
        "ne" : "Nepali",
        "nl" : "Dutch",
        "no" : "Norwegian",
        "nr" : "Ndebele",
        "nso" : "Pedi",
        "ny" : "Nyanja",
        "oc" : "Occitan",
        "om" : "Oromo",
        "or" : "Oriya",
        "pa" : "Punjabi",
        "pl" : "Polish",
        "ps" : "Pashto",
        "pt" : "Portuguese",
        "qu" : "Quechua",
        "rm" : "Rhaeto Romance",
        "rn" : "Rundi",
        "ro" : "Romanian",
        "ru" : "Russian",
        "rw" : "Kinyarwanda",
        "sa" : "Sanskrit",
        "sco" : "Scots",
        "sd" : "Sindhi",
        "sg" : "Sango",
        "si" : "Sinhalese",
        "sk" : "Slovak",
        "sl" : "Slovenian",
        "sm" : "Samoan",
        "sn" : "Shona",
        "so" : "Somali",
        "sq" : "Albanian",
        "sr" : "Serbian",
        "ss" : "Siswant",
        "st" : "Sesotho",
        "su" : "Sundanese",
        "sv" : "Swedish",
        "sw" : "Swahili",
        "syr" : "Syriac",
        "ta" : "Tamil",
        "te" : "Telugu",
        "tg" : "Tajik",
        "th" : "Thai",
        "ti" : "Tigrinya",
        "tk" : "Turkmen",
        "tl" : "Tagalog",
        "tlh" : "Klingon",
        "tn" : "Tswana",
        "to" : "Tonga",
        "tr" : "Turkish",
        "ts" : "Tsonga",
        "tt" : "Tatar",
        "ug" : "Uighur",
        "uk" : "Ukrainian",
        "ur" : "Urdu",
        "uz" : "Uzbek",
        "ve" : "Venda",
        "vi" : "Vietnamese",
        "vo" : "Volapuk",
        "war" : "Waray Philippines",
        "wo" : "Wolof",
        "xh" : "Xhosa",
        "yi" : "Yiddish",
        "yo" : "Yoruba",
        "za" : "Zhuang",
        "zh" : "Chinese Simplified",
        "zh-Hant" : "Chinese Traditional",
        "zu" : "Zulu",
    }

    API_key = "baeff846db46ed77e5cb81065541130c"
    header_data = { "Authorization" : "Bearer " + API_key }
    param_data = { "q" : text }
    endpoint = "https://ws.detectlanguage.com/0.2/detect"
    response = requests.get(endpoint, headers=header_data, params=param_data)
    response_data = json.loads(response.text)

    language = languages[response_data["data"]["detections"][0]["language"]]
    confidence = response_data["data"]["detections"][0]["confidence"]

    return "https://ws.detectlanguage.com/0.2/detect\nUsing Language Detection API - Interpretation for: "\
           + text + "\nLangauge: " + language + "\nConfidence Rating: " + str(confidence)

def fortnite(username, platform):
    API_key = "632dcf46-d156-45b5-b88e-0fa954748384"
    header_data = {"TRN-Api-Key" : API_key}
    endpoint = "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + username
    response = requests.get(endpoint, headers=header_data)
    response_data = json.loads(response.text)

    if "error" in response_data:
        return "Player Not Found"

    wins = response_data["lifeTimeStats"][8]["value"]
    win_percent = response_data["lifeTimeStats"][9]["value"]
    kills = response_data["lifeTimeStats"][10]["value"]
    kd =  response_data["lifeTimeStats"][11]["value"]

    return "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + username + "\n" + \
           "Using Fortnite Tracker API - Fortnite statistics for: " + username + " on " + platform \
           + "\nWins: " + wins + "\nWin %: " + win_percent + "\nKills: " + kills + "\nK/D: " + kd

if __name__ == '__main__':
    print(yelp("Sushi", "San Francisco Bay Area, CA", "40000"))
    print(detect_langauge("Justin - bu ajoyib mushuk, chunki uning otasi - ota") + "\n")
    print(fortnite("Conn205", "pc"))