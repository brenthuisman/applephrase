import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_spanish.txt'
    default_neighbor_lexicon = 'orthographic_spanish.txt'
    default_word_lexicon = 'orthographic_spanish.txt'
    default_lookup_lexicon = 'orthographic_spanish.txt'

    double_letters = ['aa', 'au', 'ai', 'ea', 'ee', 'ia', 'ie', 'io',
                      'oo', 'oe', 'oi', 'ou', 'ui', 'ue', 'ei', 'eu', 'ae', 'oa']
    single_letters = ['a', 'e', 'i', 'o', 'u', 'y']
    accented_letters = [u'á', u'à', u'ê', u'è', u'é',
                        u'í', u'ó', u'â', u'ô', u'ú', u'ü', u'ö']
    double_letter_pattern = u'|'.join(double_letters)
    single_letter_pattern = u'|'.join(single_letters)
    accented_letter_pattern = u'|'.join(accented_letters)
    nucleuspattern = u'%s|%s|%s' % (
        double_letter_pattern, accented_letter_pattern, single_letter_pattern)
    oncpattern = re.compile(u'(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
