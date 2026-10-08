from fixit.cli import main


def test_version(capsys):
    try:
        main(["--version"])
    except SystemExit:
        pass
    assert "fixit" in capsys.readouterr().out


def test_palindrome_command(capsys):
    main(["palindrome", "level"])
    assert capsys.readouterr().out.strip() == "True"
