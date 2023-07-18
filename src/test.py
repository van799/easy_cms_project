def test(endpoint):
    if endpoint is None:
        return True
    if type(endpoint) is not str:
        return True
    if endpoint.strip() == '':
        return True
    return False


print(test('endpoint'))
