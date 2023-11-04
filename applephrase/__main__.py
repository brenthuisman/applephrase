import secrets, string, re, argparse
from wuggy import WuggyGenerator

langdict = {
    'nl': "orthographic_dutch",
    'fr': "orthographic_french",
    'en': "orthographic_english",
    'de': "orthographic_german",
    'pl': "orthographic_polish",
    'eu': "orthographic_basque",
    'es': "orthographic_spanish",
    'it': "orthographic_italian",
    'sc': "orthographic_serbian_cyrillic",
    'sl': "orthographic_serbian_latin",
    'vt': "orthographic_vietnamese",
    'ee': "orthographic_estonian",
}

def parsedicefile(fname,minlen,maxlen):
    words = []
    with open(fname) as file:
        for line in file.readlines():
            m = re.match("([^\W\d]+)\s.*", line.strip())
            if m and len(m.group(1)) >= minlen and len(m.group(1)) <= maxlen:
                words.append(m.group(1))
    return words

def getwuggydicts():
    g = WuggyGenerator()
    print(g.supported_official_language_plugin_names)

def wugglify(args):
    langf = langdict[args.lang]

    g = WuggyGenerator()
    g.load(langf)

    words = parsedicefile(f"{g.language_plugin_data_path}/{langf}.txt",args.min,args.max)

    while True:
        try:
            pws = []
            for j in range(args.np):
                pw = args.sep.join([g.generate_classic([secrets.choice(words)],ncandidates_per_sequence=1)[0]["pseudoword"].capitalize() if not args.nocaps else secrets.choice(words) for i in range(args.nw)]) + args.sep + ''.join([secrets.choice(string.digits + string.ascii_letters) for i in range(args.nc)])
                pws.append(pw)
        except IndexError as e:
            raise e
        except Exception:
            continue
        break
    return pws

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog="applephrase",
                        description="Generate memorable passphrases using pseudowords.")
    parser.add_argument('lang', type=str, choices=list(langdict.keys()), help="Pick a language")
    parser.add_argument('--min', type=int, default=5, help="Minimum word length")
    parser.add_argument('--max', type=int, default=10, help="Maximum word length")
    parser.add_argument('--nw', type=int, default=2, help="Number of words")
    parser.add_argument('--nc', type=int, default=6, help="Number of characters in the random string")
    parser.add_argument('--np', type=int, default=20, help="Number of passphrases to generate")
    parser.add_argument('--sep', type=str, default="-", help="Separator")
    parser.add_argument('--nocaps', help="Don't capitalize words.", action='store_true')

    args = parser.parse_args()

    pws = wugglify(args)

    for pw in pws:
        print(pw)
