import pytest
import io
import find_path


@pytest.mark.parametrize("city1, city2", [(' ', ' '), ('Кемерово', 'Хельсинки')])
def test_wrong_cities(monkeypatch, city1, city2):
    monkeypatch.setattr('sys.stdin', io.StringIO(f'{city1}\n{city2}'))
    with pytest.raises(ValueError):
        find_path.main()


@pytest.mark.parametrize("file_number", list(range(1, 4)))
def test_by_files(monkeypatch, capsys, file_number):
    input_data = open(f'input/test{file_number}.txt', encoding='utf-8')
    expected_data = open(f'output/test{file_number}.txt', encoding='utf-8')

    monkeypatch.setattr('sys.stdin', io.StringIO(input_data.read()))
    find_path.main()
    out, err = capsys.readouterr()
    assert err == ''
    assert out == expected_data.read() + "\n"
