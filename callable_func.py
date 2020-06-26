import inspect
import importlib


def get_callables(module_path, decorators=None):
    callables = []
    try:
        module_label = " / ".join([v.capitalize() for v in module_path.split(".")])
        module = importlib.import_module(module_path)
    except ModuleNotFoundError as err:
        print ("Error: ", err)
        return []

    module_src = inspect.getsource(module)
    is_callable = False
    for line in module_src.split("\n"):
        if line.strip():
            if not is_callable:
                if decorators:
                    if line.replace("@", "").strip() in decorators:
                        is_callable = True
                        continue
                if line.startswith("@"):
                    is_callable = True
                    continue

            if is_callable and line.startswith('def '):
                callable_name = line.split("def ")[1].split("(")[0]
                value = module_path + '.' + callable_name
                label = module_label + ' / ' + callable_name
                callables.append((value, label))

            is_callable = False
    return callables


# callables = get_callables("pkg1.pkg11.module", decorators=['tes_decorator'])
callables = get_callables("pkg1.pkg11.module")
print(callables)
