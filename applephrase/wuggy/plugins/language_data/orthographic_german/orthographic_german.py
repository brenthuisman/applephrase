from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'orthographic_german.txt'
    default_neighbor_lexicon = 'orthographic_german.txt'
    default_word_lexicon = 'orthographic_german.txt'
    default_lookup_lexicon = 'orthographic_german.txt'

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
