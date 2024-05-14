import os

folders_to_create = [
    "Anthony Jeselnik Fire In The Maternity Ward (2019) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Anthony Jeselnik Thoughts And Prayers (2015) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Bill Burr Im Sorry You Feel That Way (2014) [WEBRIP] [1080p] [WEBRip] [YTS.MX]",
    "Bill Burr Live At Red Rocks (2022) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Bill Burr Paper Tiger (2019) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Bill Burr Walk Your Way Out (2017) [WEBRIP] [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Bill Burr You People Are All The Same. (2012) [1080p] [WEBRip] [YTS.MX]",
    "Bill Hicks",
    "Bill Hicks Reflections (2015) [1080p] [WEBRip] [YTS.MX]",
    "Brad Williams Fun Size (2015) [1080p] [WEBRip] [YTS.MX]",
    "Chris Rock Bigger Blacker (1999) [1080p] [WEBRip] [YTS.MX]",
    "Chris Rock Never Scared (2004) [1080p] [WEBRip] [YTS.MX]",
    "Christina P. Mom Genes (2022) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Daniel Sloss X (2019) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Dave Chappelle 8 46 (2020) [1080p] [WEBRip] [YTS.MX]",
    "Dave Chappelle Equanimity (2017) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Dave Chappelle For What Its Worth (2004) [HDTV] [720p] [BluRay] [YTS.MX]",
    "Dave Chappelle Killin Them Softly (2000) [1080p] [WEBRip] [YTS.MX]",
    "Dave Chappelle Sticks Stones (2019) [1080p] [WEBRip] [5.1] [YTS.MX]",
    "Dave Chappelle The Bird Revelation (2017) [1080p] [WEBRip] [5.1] [YTS.MX]"
]

script_directory = os.path.dirname(os.path.abspath(__file__))

for folder_name in folders_to_create:
    folder_path = os.path.join(script_directory, folder_name)
    os.makedirs(folder_path)

print("Folders created successfully.")
