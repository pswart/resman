class Engaged(Exception):
    """
    Exception if a resource is already engaged by a user.

    Attributes:
        engaged_by -- user that resource is engaged by
    """
    def __init__(self, engaged_by):
        self.engaged_by = engaged_by

class Free(Exception):
    """
    Exception thrown to indicate that the resource is already free.
    """
    pass

class ResourceManager(object):
    """
    Resource manager. Manages resources.

    Attributes:
        resource_list -- list of resources
    """
    def __init__(self, resource_list=None):
        if resources is not None:
            self._resources = dict((res, None) for res in resource_list)
        else:
            self._resources = {}

    def addResource(self, resource):
    """
    Adds a resource, sets user of resource to None.
    
    Attributes:
        resource -- name of resource
    """
        self._resources[resource.name] = None

    def removeResource(self, resource):
    """
    Removes a resource.
    
    Attributes:
        resource -- name of resource
    """
        self._resources.pop(resource)

    def engageResource(self, resource, user):
    """
    Assigns a resource to a user.
    
    Attributes:
        resource -- name of resource
        user -- name of user who wishes to engage resource

    Raises:
        Engaged -- if resource already engaged by a user
    """
        if self._resources[resource] is not None:
            raise Engaged(self._resources[resource])

        self._resources[resource] = user  

    def freeResource(self, resource, user):
    """
    Frees a resource by setting user of resource to None.
    
    Attributes:
        resource -- name of resource
        user -- name of user who wishes to free resource

    Raises:
        Free -- if resource already free
        Engaged -- if resource engaged by another user
    """
        if self._resources[resource] is None:
            raise Free()

        if self._resources[resource] != user:
            raise Engaged(self._resources[resource])
        
        self._resources[resource] = None
