import pytest
from resman import resource_manager

class TestResourceManager(object):
    def test_addResource_without_list(self):
        want = {}
        r = resource_manager.ResourceManager()
        got = r._resources
        assert got == want
