".. include:: ../documentation/home.md"
try:
    from applephrase.wuggy.evaluators.ld1nn import ld1nn
    from applephrase.wuggy.generators.wuggygenerator import WuggyGenerator
    from applephrase.wuggy.plugins.baselanguageplugin import BaseLanguagePlugin
except:
    from .evaluators.ld1nn import ld1nn
    from .generators.wuggygenerator import WuggyGenerator
    from .plugins.baselanguageplugin import BaseLanguagePlugin