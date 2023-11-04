# Subsyllabic Polish
# by Paweł Mandera
# pawel.mandera@ugent.be

import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_polish.txt'

    default_neighbor_lexicon = 'orthographic_polish.txt'
    default_word_lexicon = 'orthographic_polish.txt'
    default_lookup_lexicon = 'orthographic_polish.txt'

    double_letters = ['ia', 'ie', 'io', 'iu']
    single_letters = ['a', 'e', 'i', 'o', 'u', 'y']
    accented_letters = [u'ą', u'ę']
    double_letter_pattern = u'|'.join(double_letters)
    single_letter_pattern = u'|'.join(single_letters)
    accented_letter_pattern = u'|'.join(accented_letters)
    nucleuspattern = u'%s|%s|%s' % (
        double_letter_pattern, accented_letter_pattern, single_letter_pattern)
    oncpattern = re.compile(u'(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
