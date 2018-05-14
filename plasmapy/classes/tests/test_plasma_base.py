from plasmapy.classes.plasma_base import (
                        GenericPlasmaRegistrar,
                        GenericPlasma,
                        PLASMA_CLASSES
                        )

class NoDataSource(GenericPlasmaRegistrar):
    pass

class HasDataSource(GenericPlasmaRegistrar):
    is_datasource_for = 'source'


class TestRegistrar:
    def test_no_data_source(self):
        assert not 'NoDataSource' in PLASMA_CLASSES

    def test_has_data_source(self):
        assert 'HasDataSource' in PLASMA_CLASSES
        assert PLASMA_CLASSES['HasDataSource'] == 'source'


def test_subclasses():
    assert issubclass(GenericPlasma, GenericPlasmaRegistrar)
