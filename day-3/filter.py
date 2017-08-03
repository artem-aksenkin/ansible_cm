
def get_mongo_src(args, ob, ob1, mongo_ver)
    result = []
    for arg in args:
        if ob and ob1 and mongo_ver in arg:
            result.extend(arg)
    return result


