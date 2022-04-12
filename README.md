# Calculator
Application can perform calculations with two user given numbers.  
Input and output numbers are in base-10 and they can be integer or decimal separated with a dot(.) e.g. 2.5, 13 or 313.  
Input and output can also be expressed in powers of ten e.g. 1e3 (which represents 10^3 = 1000), 10e3 (which represents 10\*10^3 = 10000), 10e-3 (which represents 10\*10^-3 = 0.01) or 1e-3 (which represents 10^-3 = 0.001).

## Installation
- Install dependencies
```bash
poetry install
```

- Start application
```bash
poetry run invoke start
```

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
