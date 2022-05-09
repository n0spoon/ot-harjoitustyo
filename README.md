# Calculator
Application can perform calculations determined by user input.  

**Input and output numbers are in base-10 and they can be integer or decimal separated with a dot(.) e.g. 2.5, 0.75, 3.1415.**  

*Input and output can also be expressed in powers of ten e.g. 1e3 (represents 10^3 = 1000), 10e3 (represents 10\*10^3 = 10000), 10e-3 (represents 10\*10^-3 = 0.01) or 1e-3 (represents 10^-3 = 0.001).*


## Installation
- Install dependencies
```bash
poetry install
```

- Initialize database
```bash
poetry run invoke init
```

- Start application
```bash
poetry run invoke start
```

**Remember to use a dot . for decimal part representation e.g. 2.5, 0.75, 3.1415**

**Do not input decimals as fractions e.g. 1/2, 3/8 or 1/10, these won't be processed**

## Command line functions

### Tests
- Run tests with pytest
```bash
poetry run invoke test
```

### Coverage
- Generate coverage report
```bash
poetry run invoke coverage-report
```

### Pylint
- Check errors with Pylint
```bash
poetry run invoke lint
```

## Documentation

- [Architectural Illustration](https://github.com/n0spoon/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/n0spoon/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Vaatimusmäärittely](https://github.com/n0spoon/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Working Hours](https://github.com/n0spoon/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Latest Release](https://github.com/n0spoon/ot-harjoitustyo/releases/latest)
- [First Release](https://github.com/n0spoon/ot-harjoitustyo/releases/tag/viikko5)
- [User Manual](https://github.com/n0spoon/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
