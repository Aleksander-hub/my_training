def introspection_info(obj):

    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [met for met in dir(obj) if callable(getattr(obj, met))]
    module = obj.__class__.__module__

    dict_int = {'Тип': obj_type,
                'Атрибут': attributes,
                'Метод': methods,
                'Модуль': module}

    return dict_int

number_info = introspection_info(42)
print(number_info)