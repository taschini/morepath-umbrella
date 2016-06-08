def test_top_level_packages():
    from ..helpers import top_level_packages

    assert top_level_packages({
        'packages': ['one', 'more', 'more.foo', 'more.foo.test', 'more.foobar'],
        'namespace_packages': ['more']}) == ['more.foo', 'more.foobar', 'one']
