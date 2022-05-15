# Architectural illustration

## Structure

![Package Structure](./photos/architecture-package.png)

Package _ui_ contains user interface, _services_ contains application logic and _repositories_ contains code corresponsible for saving calculations.

## Application logic

Class _CalculationService_ forms and responds for application logic, which represents different calculations and their storage through _CalculationRepository_.

```mermaid
 classDiagram
     CalculationService "1" -- "1" CalculationRepository
     class CalculationService{
         calcdata
     : constant_pi()
     : constant_e()
     : string_to_number(var_s)
     : sum_service(var_a, var_b)
     : sub_service(var_a, var_b)
     : mul_service(var_a, var_b)
     : div_service(var_a, var_b)
     : sqrt_service(var_a)
     : exp_service(var_a, var_b)
     : inv_service(var_a)
     : ceil_service(var_a)
     : floor_service(var_a)
     : clean_result(result)
     : count()
     : return_calculations()
     : add_result(result)
     : get_last_result()
     : clear_last_calculation()
     : clear_all_calculations()
     : memory_is_empty()
     }
     class CalculationRepository{
         db
     : add_calculation(result)
     : print_calculations()
     : count_calculations()
     : memory_is_empty()
     : get_last()
     : clear_last()
     : clear_all()
     }
```

![Package Structure and Classes](./photos/architecture-package-and-classes.png)

_CalculationService_ can access and manage calculations in sqlite3 database memory through _CalculationRepository_.

## Main functionalities

Sequence diagram illustrating functionality of the application calculating 2 to the power of 12.

```mermaid
 sequenceDiagram
     actor User
     main->>IO: calculator.start()
     IO->>IO: start()
     IO->>IO: print_guide()
     IO->>User: input("Enter command: ")
     User->>IO: "exp"
     IO->>IO: command == "exp"
     IO->>User: input("Enter first number: ")
     User->>IO: "2"
     IO->>IO: var_a = "2"
     IO->>User: input("Enter second number: ")
     User->>IO: "12"
     IO->>IO: var_b = "12"
     IO->>IO: callable(calculation)
     IO->>IO: True
     IO->>CalculationService: exp_service("2", "12")
     CalculationService->>CalculationService: if isna(var_a) or isna(var_b)
     CalculationService->>CalculationService: False
     CalculationService->>CalculationService: var_x = string_to_number(var_a)
     CalculationService->>CalculationService: var_x = int(2)
     CalculationService->>CalculationService: var_y = string_to_number(var_b)
     CalculationService->>CalculationService: var_y = int(12)
     CalculationService->>CalculationService: if (var_x == 0) and (var_y < 0)
     CalculationService->>CalculationService: False
     CalculationService->>CalculationService: result = var_x**var_y
     CalculationService->>CalculationService: result = clean_result(result)
     CalculationService->>CalculationService: if var_y == 0.5
     CalculationService->>CalculationService: False
     CalculationService->>CalculationService: result = int(4096)
     CalculationService->>CalculationRepository: add_result(result)
     CalculationRepository->>CalculationRepository: add_calculation(result)
     CalculationRepository->>CalculationRepository: if not isintance(result, str)
     CalculationRepository->>CalculationRepostiory: True
     CalculationRepository->>CalculationRepository: result = str(result)
     CalculationRepository->>CalculationRepository: cursor = _db.cursor()
     CalculationRepository->>CalculationRepository: cursor.execute("INSERT INTO Calculations (result) VALUES (?)", [result])
     CalculationRepository->>CalculationRepository: _db.commit()
     CalculationService->>IO: "2^12 = 4096"
     IO->>IO: print("2^12 = 4096\n")
     IO->>IO: continue
     IO->>User: input("Enter command: ")
     User->>IO: "exit"
     IO->>IO: command == "exit"
     IO->>IO: print("Exiting Calculator..\n")
     IO->>IO: break
```

Illustration of application calculating the square root of 9, returning count and result of calculations in memory.  

```mermaid
 sequenceDiagram
     actor User
     main->>IO: calculator.start()
     IO->>IO: start()
     IO->>IO: print_guide()
     IO->>User: input("Enter command: ")
     User->>IO: "sqrt"
     IO->>IO: command == "sqrt"
     IO->>IO: if command == "sqrt" or command == "inv"
     IO->>IO: True
     IO->>User: input("Enter a positive number: ")
     User->>IO: "9"
     IO->>IO: var_a = "9"
     IO->>IO: callable(calculation)
     IO->>IO: True
     IO->>CalculationService: sqrt_service("9")
     CalculationService->>CalculationService: if isna(var_a)
     CalculationService->>CalculationService: False
     CalculationService->>CalculationService: var_x = string_to_number(var_a)
     CalculationService->>CalculationService: if var_x < 0
     CalculationService->>CalculationService: False
     CalculationService->>CalculationService: result = var_x**(1/2)
     CalculationService->>CalculationService: result = f"±{clean_result(result)}
     CalculationService->>CalculationService: result = "±3"
     CalculationService->>CalculationRepository: add_result(result)
     CalculationRepository->>CalculationRepository: add_calculation(result)
     CalculationRepository->>CalculationRepository: if not isinstance(result, str)
     CalculationRepository->>CalculationRepository: False
     CalculationRepository->>CalculationRepository: cursor = _db.cursor()
     CalculationRepository->>CalculationRepository: cursor.execute("INSERT INTO Calculations (result) VALUES (?)", [result])
     CalculationRepository->>CalculationRepository: _db.commit()
     CalculationService->>IO: "√9 = ±3"
     IO->>IO: print("√9 = ±3")
     IO->>IO: continue
     IO->>User: input("Enter command: ")
     User->>IO: "?"
     IO->>IO: command == "?"
     IO->>IO: if command == "?"
     IO->>IO: True
     IO->>CalculationRepository: count_calculations()
     CalculationRepository->>IO: int(2)
     IO->>IO: print("Calculations: 2")
     IO->>IO: continue
     IO->>User: input("Enter command: ")
     User->>IO: "print"
     IO->>IO: if command == "print"
     IO->>IO: True
     IO->>IO: print("Calculation results in memory: 4096, ±3\n")
     IO->>IO: continue
```


Illustration of fetching last result in memory and clearing memory, while calculator is still running from the state of previous diagram.  

```mermaid
 sequenceDiagram
     actor User
     IO->>User: input("Enter command: ")
     User->>IO: "last"
     IO->>IO: if command == "last"
     IO->>IO: True
     IO->>IO: if not _calculator.memory_is_empty()
     IO->>IO: True
     IO->>CalculationService: _calculator.get_last_result()
     CalculationService->>CalculationRepository: get_last()
     CalculationRepository->>CalculationRepository: if not memory_is_empty()
     CalculationRepository->>CalculationRepository: True
     CalculationRepository->>CalculationRepository: cursor = _db.cursor()
     CalculationRepository->>CalculationRepository: cursor.execute("SELECT * FROM Calculations ORDER BY rowid DESC LIMIT 1")
     CalculationRepository->>CalculationRepository: result = cursor.fetchone()
     CalculationRepository->>CalculationRepository: unpacked_result = dict(zip(result.keys(), result))
     CalculationRepository->>CalculationRepository: return unpacked_result["result"]
     CalculationRepository->>IO: "±3"
     IO->>IO: print("Latest result in memory: ±3\n")
     IO->>IO: continue
     IO->>User: input("Enter command: ")
     User->>IO: "clearall"
     IO->>IO: if command == "clearall" or command == "ca"
     IO->>IO: True
     IO->>CalculationService: _calculator.clear_all_calculations()
     CalculationService->>CalculationService: if not memory_is_empty()
     CalculationService->>CalculationService: True
     CalculationService->>CalculationRepository: clear_all()
     CalculationRepository->>CalculationRepository: cursor = _db.cursor()
     CalculationRepository->>CalculationRepository: cursor.execute("DELETE FROM Calculations")
     CalculationRepository->>CalculationRepository: _db.commit()
     CalculationService->>IO: "Cleared everything from memory.\n"
     IO->>IO: print("Cleared everything from memory.\n")
     IO->>IO: continue
     IO->>User: input("Enter command: ")
     User->>IO: "exit"
     IO->>IO: if command == "exit"
     IO->>IO: print("Exiting calculator..\n")
```
