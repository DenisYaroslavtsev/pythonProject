import inspect


def introspection_info(obj):
    type_obj = type(obj).__name__
    atr_obj = [atr for atr in dir(obj) if callable(getattr(obj, atr))]
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]
    module_obj = inspect.getmodule(obj)
    info = {'type': type_obj,
            'attributes': atr_obj,
            'methods': methods_obj,
            'module': module_obj}

    return info


number_info = introspection_info(42)
print(number_info)
