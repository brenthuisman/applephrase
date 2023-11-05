## applephrase

applephrase is a commandline utility to generate memorable passphrases composed of a number of randomized pseudowords and a brief random string. The pseudowords can be generated for a number of languages: Dutch, French, English, German, Polish, Basque, Spanish, Italian, Serbocroatian Latin, Serbocroatian Cyrillic, Vietnamese, Estonian.

Some examples:

    Odešišćima-Krškrme-aKpmvO
    Ушоут-Џкићак-ON420G
    Brühölde-Beruhrem-dg6fgP
    Toevenboot-Rijswormen-yOrofH
    Kindati-Mirdez-tmGS5k
    Curpina-Beonangica-JVMK0t
    Démièrea-Rammardée-nhlpwd
    Naaled-Läägalide-R6qy04
    Oằnẻo-Namchất-KaRrOm
    Settenti-Ivonendo-kfOC8m
    Trazonents-Oluviungly-nBwpng
    Ulywcał-Ścipczyk-6hmSx7

The idea is that the use of pseudowords generates enough entropy in fewer words compared to regular passphrases. A terminating number of random alphanumeric characters helps get around the most common password requirements, and of course adds to the entropy. Since the pseudowords are (hopefully) pronouncable and the random characters limited in number, the resulting passphrase is memorable and still quite short.

## Wuggy

This project makes heavy use of [Wuggy](https://github.com/WuggyCode/wuggy), the software that generates the pseudowords. The upstream Python package does not install anymore, but this is easily resolved by removing the unnecessarily strict versions from the requirements file. I made some more modifications to it and added the Estonian language found in one of the forks. Wuggy is not very fast but it is fast enough and is the only project I know of to be available in Python and generate pseudowords in languages other than English.

For Serbocroatian Cyrilic and German I had to add a workaround that increases runtime, so don't be worried when it takes a minute.

I include a copy of my modified Wuggy in `applephrase/wuggy`. If anyone is interested, I can break it out again (or help upsteam update their package).

## Alternatives

[https://github.com/chrplr/openlexicon/tree/master/apps/unipseudo](Unipseudo) is fast, but written in R/Shiny. Sources seem available, but it's unclear what license the lexicon is provided under.
