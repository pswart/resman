import pytest
from resman import resource_manager

class TestResourceManager(object):
    def test_init_without_list(self):
        want = {}
        r = resource_manager.ResourceManager()
        got = r._resources
        assert got == want

    def test_init_with_None(self):
        want = {}
        r = resource_manager.ResourceManager(None)
        got = r._resources
        assert got == want

    def test_init_with_list(self):
        want = {'a' : None, 'b' : None}
        r = resource_manager.ResourceManager(['a', 'b'])
        got = r._resources
        assert got == want

    def test_addResource_with_string_to_empty_list(self):
        want = {'a' : None}
        r = resource_manager.ResourceManager()
        r.addResource('a')
        got = r._resources
        assert got == want

    def test_addResource_with_string_to_non_empty_list(self):
        want = {'a' : None, 'b' : None}
        r = resource_manager.ResourceManager('a')
        r.addResource('b')
        got = r._resources
        assert got == want

    def test_addResource_with_None(self):
        r = resource_manager.ResourceManager()
        with pytest.raises(TypeError):
            r.addResource(None)

    def test_addResource_with_int(self):
        r = resource_manager.ResourceManager()
        with pytest.raises(TypeError):
            r.addResource(5)

    def test_removeResource_from_empty_list(self):
        r = resource_manager.ResourceManager()
        with pytest.raises(KeyError):
            r.removeResource('a')

    def test_removeResource_from_non_empty_list(self):
        want = {}
        r = resource_manager.ResourceManager('a')
        r.removeResource('a')
        got = r._resources
        assert got == want

    def test_engageResource_that_is_not_in_list(self):
        r = resource_manager.ResourceManager()
        with pytest.raises(KeyError):
            r.engageResource('a', 'user')

    def test_engageResource_that_is_engaged(self):
        r = resource_manager.ResourceManager('a')
        r.engageResource('a', 'first user')
        with pytest.raises(resource_manager.Engaged):
            r.engageResource('a', 'user')
        
    def test_engageResource_that_is_free(self):
        want = {'a' : 'user'}
        r = resource_manager.ResourceManager('a')
        r.engageResource('a', 'user')
        got = r._resources
        assert got == want


