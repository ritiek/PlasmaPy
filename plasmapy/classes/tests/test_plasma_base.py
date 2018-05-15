from plasmapy.classes.plasma_base import (
                        GenericPlasmaRegistrar,
                        GenericPlasma,
                        PLASMA_CLASSES
                        )

class NoDataSource(GenericPlasmaRegistrar):
    pass

class IsDataSource(GenericPlasmaRegistrar):
    @classmethod
    def is_datasource_for(cls, **kwargs):
        return True

class IsNotDataSource(GenericPlasmaRegistrar):
    @classmethod
    def is_datasource_for(cls, **kwargs):
        return False


class TestRegistrar:
    def test_no_data_source(self):
        assert not PLASMA_CLASSES.get(NoDataSource)

    def test_is_data_source(self):
        assert PLASMA_CLASSES.get(IsDataSource)
        assert PLASMA_CLASSES[IsDataSource]()
        # Delete the class from registry once test is done
        # to not interfere with plasma factory tests
        del PLASMA_CLASSES[IsDataSource]

    def test_is_not_data_source(self):
        assert PLASMA_CLASSES.get(IsNotDataSource)
        assert not PLASMA_CLASSES[IsNotDataSource]()
        del PLASMA_CLASSES[IsNotDataSource]


def test_subclasses():
    assert issubclass(GenericPlasma, GenericPlasmaRegistrar)
