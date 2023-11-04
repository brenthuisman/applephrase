import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_serbian_latin.txt'
    default_neighbor_lexicon = 'orthographic_serbian_latin.txt'
    default_word_lexicon = 'orthographic_serbian_latin.txt'
    default_lookup_lexicon = 'orthographic_serbian_latin.txt'

    single_vowels = ['a', 'e', 'i', 'o', 'u', 'r']
    nucleuspattern = '%s' % (single_vowels)
    oncpattern = re.compile('(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
