def finder(files, queries):

    d = {}
    result = []

    for f in files:
        parsed = f.split('/')
        if parsed[-1] in d:
            d[parsed[-1]].append(f)
        else:
            d[parsed[-1]] = [f]

    for q in queries:
        if q in d:
            for f in d[q]:
                result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
