import pytest
import task8
import io


@pytest.mark.parametrize("file_number", list(range(0, 10)))
def test_emails(monkeypatch, capsys, file_number):
    input_data = open(f'input/input0{file_number}.txt')
    expected_data = open(f'output/output0{file_number}.txt')

    monkeypatch.setattr('sys.stdin', io.StringIO(input_data.read()))
    task8.main()
    out, err = capsys.readouterr()
    assert err == ''
    assert out == expected_data.read() + '\n'
