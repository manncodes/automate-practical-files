# automate-practical-files

automatic screenshots and logging of practical files.

## steps

- [ ] install required packages by running `pip install -requirements.txt`.
- [ ] create folders for the practical files by running `make_dir.py` in `practicals` directory.
- [ ] write your practical files down in each folder respectively.
- [ ] run `make.py` to create the screenshots and log files. Screenshots are saved in respective folders.
- [ ] check `practicalfiles.log` file if error persist.

## TODO

- Automate making word files.
- Improve synchronization of py runtime call in `screenshot.py`.

## empty file struture

```bash
:
└───practicals
    ├───practical 1
    ├───practical 10
    ├───practical 2
    ├───practical 3
    ├───practical 4
    ├───practical 5
    ├───practical 6
    ├───practical 7
    ├───practical 8
    ├───practical 9
    └───self-practice
     make.py
     screenshot.py
     practicalfiles.log
     make_dir.py
```
