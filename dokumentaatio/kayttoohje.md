# User manual

Download the [latest release](https://github.com/n0spoon/ot-harjoitustyo/releases/last) by selecting 'Source code' under Assets -section.


## Database configuration

User can configure database filename in _.env_-file.  Database will be named 'calculations.db' by default and placed in the _data_-folder if one doesn't already exist.


## Input and output

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


## Note about Python-version

Application has been tested with Python `3.8`.  Older version of Python might not function as intended.  


## Start

Program opens a TUI (text-based user interface) that shows available commands.  
![Startup View](./photos/startup.png)  


## Usage

Type command followed by an enter key.  
![Basic Usage](./photos/basic-calculations.png)  


A square root will result in a plusminus answer, that will count as one calculation.  When used with 'last' command, calculator will however calculate both negative and positive outcomes which each will count as a calculation.  
![Plusminus Calculations](./photos/plusminus-calculations.png)  


Commands for utility.  
![Utility Commands](./photos/utility-commands.png)  


Example of finding volume of a cylinder with 23cm radius and 42cm height in litres.  
![Volume of a Cylinder](./photos/cylinder-volume.png)  
Formula for the volume is pi*(r^2)*h, so we calculate r^2 first, multiply pi with last result and multiply last result with 42 to get a volume of ??? 69799.9cm^3.  One litre is 1000cm^3 therefore we divide the result by 1000 to get the volume in litres and round up using ceiling function, volume ??? 70L.  
