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
     IO->>IO: command = exp
     IO->>User: input("Enter first number: ")
     User->>IO: "2"
     IO->>IO: var_a = 2
     IO->>User: input("Enter second number: ")
     User->>IO: "12"
     IO->>IO: var_b = 12
     IO->>IO: callable(calculation)
     IO->>IO: True
     IO->>CalculationService: exp_service(2, 12)
     CalculationService->>CalculationService: result = 4096
     CalculationService->>CalculationService: add_result(result)
     CalculationService->>CalculationRepository: add_calculation(result) 
     CalculationService->>IO: "2^12 = 4096"
     IO->>IO: print("2^12 = 4096")
     IO->>User: input("Enter command: ")
     User->>IO: "exit"
     IO->>IO: command = "exit"
     IO->>IO: print("Exiting Calculator..\n")
```
