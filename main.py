def parse(query: str) -> dict:
    query_dict = {}
    if '?' in query:
        query_page = query.split('?', 1)[1]
        if query_page:
            key_value = [item for item in query_page.split('&')]
            for item in key_value:
                if '=' in item:
                    key, value = item.split('=', 1)
                    query_dict.update([(key, value)])
        return query_dict
    else:
        return query_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?&color=purple???&') == {'color': 'purple???'}
    assert parse('https://example.com/path/to/page?name=Dima==&age23') == {'name': 'Dima=='}
    assert parse('https://example.com/path/?name=Dima&age=23&sex=men') == {'name': 'Dima', 'age': '23', 'sex': 'men'}
    assert parse('https://example.com/path/to/page?&&??') == {}
    assert parse('https://example.com/path/to/page?name=Dima&age=23??&') == {'name': 'Dima', 'age': '23??'}


# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

