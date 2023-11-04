import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_serbian_cyrillic.txt'
    default_neighbor_lexicon = 'orthographic_serbian_cyrillic.txt'
    default_word_lexicon = 'orthographic_serbian_cyrillic.txt'
    default_lookup_lexicon = 'orthographic_serbian_cyrillic.txt'

    single_vowels = ['a', 'e', 'и', 'o', 'u', 'р']
    nucleuspattern = '%s' % (single_vowels)
    oncpattern = re.compile('(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
