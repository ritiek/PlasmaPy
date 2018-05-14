from plasmapy.classes import GenericPlasma, PLASMA_CLASSES

from plasmapy.utils.datatype_factory_base import BasicRegistrationFactory
from plasmapy.utils.datatype_factory_base import NoMatchError
from plasmapy.utils.datatype_factory_base import MultipleMatchError
from plasmapy.utils.datatype_factory_base import ValidationFunctionError


class PlasmaFactory(BasicRegistrationFactory):
    pass

Plasma = PlasmaFactory(default_widget_type=GenericPlasma)
Plasma.registry = PLASMA_CLASSES
