import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_estonian.txt'
    default_neighbor_lexicon = 'orthographic_estonian.txt'
    default_word_lexicon = 'orthographic_estonian.txt'
    default_lookup_lexicon = 'orthographic_estonian.txt'
    double_letters = ['aa', 'ee', 'ii', 'oo', 'uu', 'ia', 'ie', 'iu',
                      'io', 'oe', 'ou', 'oa', 'oi', 'ei', 'eu', 'ea', 'eo', 'ae',
                      'ai', 'ao', 'au', 'ue', 'ui', 'uo','ua']
    single_letters = ['a', 'e', 'i', 'o', 'u']
    accented_letters = [u'à', u'ê', u'è', u'é', u'â', u'ô', u'ü', u'õ']
    double_letter_pattern = '|'.join(double_letters)
    single_letter_pattern = '|'.join(single_letters)
    accented_letter_pattern = '|'.join(accented_letters)
    nucleuspattern = '%s|%s|%s' % (
        double_letter_pattern, accented_letter_pattern, single_letter_pattern)
    oncpattern = re.compile('(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
