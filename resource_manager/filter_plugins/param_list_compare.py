from ansible.errors import AnsibleFilterError
def param_list_compare(base, other):
    if not isinstance(base, list):
        raise AssertionError("`base` must be of type 'list'")
    if not isinstance(other, list):
        raise AssertionError("`other` must be of type 'list'")

    combined = []
    alls = [x for x in other if x == "all"]
    bangs = [x[1:] for x in other if x.startswith('!')]
    rbangs = [x for x in other if x.startswith('!')]
    remain = [x for x in other if x not in alls and x not in rbangs and x in base]
    unsupported = [x for x in other if x not in alls and x not in rbangs and x not in base]

    if unsupported:
        raise AnsibleFilterError("The following are unsupported: %s" % (",".join(unsupported)))

    if alls:
        combined = base
    for entry in bangs:
        if entry in combined:
            combined.remove(entry)
    for entry in remain:
        if entry not in combined:
            combined.append(entry)
    combined.sort()
    return {'actionable': combined, 'unsupported': unsupported }


class FilterModule(object):
    ''' param_list_compare '''

    def filters(self):
        return {
            'param_list_compare': param_list_compare
        }