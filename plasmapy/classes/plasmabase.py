from collections import OrderedDict
from abc import ABC

# GenericPlasma subclass registry
PLASMA_CLASSES = OrderedDict()

class GenericPlasmaRegistrar(ABC):
    _registry = PLASMA_CLASSES

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if hasattr(cls, 'is_datasource_for'):
            cls._registry[cls.__name__] = cls.is_datasource_for


class GenericPlasma(GenericPlasmaRegistrar):
    def __init__(self, **kwargs):
        super(GenericPlasma, self).__init__(**kwargs)
