import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_french.txt'
    default_neighbor_lexicon = 'orthographic_french.txt'
    default_word_lexicon = 'orthographic_french.txt'
    default_lookup_lexicon = 'orthographic_french.txt'

    triple_letters = ['eai', 'iai']
    double_letters = ['aa', 'au', 'ai', 'ea', 'ee', 'ia', 'ie', 'io',
                      'oo', 'oe', 'oi', 'ou', 'ui', 'ue', 'ei', 'eu', 'ae', 'oa']
    single_letters = ['a', 'e', 'i', 'o', 'u', 'y']
    accented_letters = [u'à', u'ê', u'è', u'é', u'â', u'ô', u'ü', u'ö']
    double_accented_letters = [u'ée', u'éo', u'ué', u'éé', u'iè', u'oï']

    triple_letter_pattern = '|'.join(triple_letters)
    double_letter_pattern = '|'.join(double_letters)
    single_letter_pattern = '|'.join(single_letters)
    accented_letter_pattern = '|'.join(accented_letters)
    double_accented_letter_pattern = '|'.join(double_accented_letters)

    nucleuspattern = '%s|%s|%s|%s|%s' % (
        triple_letter_pattern, double_accented_letter_pattern, double_letter_pattern,
        accented_letter_pattern, single_letter_pattern)
    oncpattern = re.compile('(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
