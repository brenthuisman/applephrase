import secrets, string, re, argparse
from wuggy import WuggyGenerator

langdict = {
    "nl": "orthographic_dutch",
    "fr": "orthographic_french",
    "en": "orthographic_english",
    "de": "orthographic_german",
    "pl": "orthographic_polish",
    "eu": "orthographic_basque",
    "es": "orthographic_spanish",
    "it": "orthographic_italian",
    "sc": "orthographic_serbian_cyrillic",
    "sl": "orthographic_serbian_latin",
    "vt": "orthographic_vietnamese",
    "ee": "orthographic_estonian",
}


def parsedicefile(fname, minlen, maxlen):
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

    words = parsedicefile(
        f"{g.language_plugin_data_path}/{langf}.txt", args.min, args.max
    )

    passphrases = []
    for j in range(args.np):
        pseudowords = []
        while len(pseudowords) < args.nw:
            try:
                pseudowords.append(
                    g.generate_classic(
                        [secrets.choice(words)], ncandidates_per_sequence=1
                    )[0]["pseudoword"]
                )
            except:
                # Sometimes g.generate_classic returns empty list.
                # Seems to only happen with German and Serbocroatian Cyrillic.
                continue
        pw = (
            args.sep.join(
                [i.capitalize() for i in pseudowords]
                if not args.nocaps
                else pseudowords
            )
            + args.sep
            + "".join(
                [
                    secrets.choice(string.digits + string.ascii_letters)
                    for i in range(args.nc)
                ]
            )
        )
        passphrases.append(pw)
    return passphrases


def main():
    parser = argparse.ArgumentParser(
        prog="applephrase",
        description="Generate memorable passphrases using pseudowords.",
    )
    parser.add_argument(
        "lang", type=str, choices=list(langdict.keys()), help="Pick a language"
    )
    parser.add_argument("--min", type=int, default=5, help="Minimum word length")
    parser.add_argument("--max", type=int, default=10, help="Maximum word length")
    parser.add_argument(
        "--nw", type=int, default=2, help="Number of words in a passphrase"
    )
    parser.add_argument(
        "--nc", type=int, default=6, help="Number of characters in the random string"
    )
    parser.add_argument(
        "--np", type=int, default=20, help="Number of passphrases to generate"
    )
    parser.add_argument("--sep", type=str, default="-", help="Word separator")
    parser.add_argument("--nocaps", help="Don't capitalize words.", action="store_true")

    args = parser.parse_args()

    passphrases = wugglify(args)

    for passphrase in passphrases:
        print(passphrase)


if __name__ == "__main__":
    main()
