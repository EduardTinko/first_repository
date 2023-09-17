def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    query_dict = {}
    if query:
        key_value = query.split(';')
        for item in key_value:
            if '=' in item:
                key, value = item.split('=', 1)
                query_dict.update([(key, value)])
        return query_dict

    else:
        return query_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';name=Dima=;age=28') == {'name': 'Dima=', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;sex=men') == {'name': 'Dima', 'age': '28', 'sex': 'men'}
    assert parse_cookie(';name=Dima;age=28?;') == {'name': 'Dima', 'age': '28?'}
    assert parse_cookie('nameDima;age=28;sex=men') == {'age': '28', 'sex': 'men'}
    assert parse_cookie('nameDima;') == {}
    assert parse_cookie('name-Dima;age-28;sex-men') == {}



