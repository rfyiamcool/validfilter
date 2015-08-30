#coding:utf-8
import re
def checkdata(template, uncheckdatad, quiet=False, **kwargs):
    try:
        if isinstance(template, tuple):
            valid = False
            for template_option in template:
                try:
                    valid = checkdata(template_option, uncheckdatad, **kwargs)
                    if valid:
                        break
                except FailedValidationError:
                    pass
            if valid:
                return True
            else:
                raise FailedValidationError("None of {0} in template match topmost level of {1}".format(template, uncheckdatad))

        elif isinstance(template, dict) and isinstance(uncheckdatad, dict):
            # Two dictionaries. Compare key-by-key!
            if all([checkdata(template[key], uncheckdatad.get(key), **kwargs) for key in template]):
                return True
            else:
                raise FailedValidationError("{0} in template did not match topmost level of {1}".format(template, uncheckdatad))

        elif isinstance(template, list) and isinstance(uncheckdatad, list):
            # Two lists. The template list should have one element to demonstrate its members'
            # structure. This can be a tuple.
            if all([checkdata(template[0], item, **kwargs) for item in uncheckdatad]):
                return True
            else:
                raise FailedValidationError("Not all list items in {0} matched template {1}".format(uncheckdatad, template))

        elif isinstance(template, type):
            # Template declared a type. Time to compare values.
            print template,uncheckdatad
            if template in (str, unicode) and kwargs.get('fuzzy_string_typing'):
                template = basestring
            if re.search(template,str(uncheckdatad)):
                return True
            else:
                raise FailedValidationError("{0} is not of type {1}".format(uncheckdatad, template))

        else:
            if re.search(template,str(uncheckdatad)) or template is None:
                return True
            else:
                raise FailedValidationError("{0} is not equal to {1}".format(uncheckdatad, template))
    except FailedValidationError, e:
        if quiet:
            return False
        else:
            raise e


class FailedValidationError(Exception):
    pass


def deep_merge(base, incoming):
    if not isinstance(base, dict) or not isinstance(incoming, dict):
        return incoming
    for key in incoming:
        if key in base:
            base[key] = deep_merge(base[key], incoming[key])
        else:
            base[key] = incoming[key]
    return base
