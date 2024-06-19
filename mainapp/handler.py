from django.db import models


def checkAccountAccess(Class_obj,user):
    # get all feilds from this class_obj which end with access
    # fields_mtm = [f.name for f in Class_obj._meta.get_fields() if f.name.endswith('access') and isinstance(f, models.ManyToManyField)]
    fields_nmtm = [f.name for f in Class_obj._meta.get_fields() if f.name.endswith('access') and not isinstance(f, models.ManyToManyField)]
    value_nmtm = {f: getattr(Class_obj, f) for f in fields_nmtm}
    # Get the related developmentPageAccess objects
    development_pages = getattr(Class_obj, 'development_page_access').all()

    # Get the Auth_teachers_access value for each developmentPageAccess object
    auth_teachers_access = {page:list(getattr(page, 'Auth_teachers_access').all()) for page in development_pages}
    auth_teachers_access_values= [val for value in auth_teachers_access.values() for val in value ]
    # print(auth_teachers_access_values)
    # print(list(value_nmtm.values()))
    # print(user,user in auth_teachers_access_values or user in list(value_nmtm.values()))
    return user in auth_teachers_access_values or user in list(value_nmtm.values())
