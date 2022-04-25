# Architectural illustration

## Structure

![Package Structure](./photos/architecture-package.png)

Package _ui_ contains user interface, _services_ contains application logic and _repositories_ contains code corresponsible for saving calculations.

## Application logic

Class CalculationService forms and responds for application logic, which represents different calculations and their storage through CalculationRepository.

```mermaid
 classDiagram
     CalculationService "1" -- "1" CalculationRepository
     class CalculationService{
         calcdata
     : string_to_number(var_s)
     : sum_service(var_a, var_b)
     : sub_service(var_a, var_b)
     : mul_service(var_a, var_b)
     : div_service(var_a, var_b)
     : sqrt_service(var_a)
     : clean_result(result)
     : count()
     : return_calculations()
     : add(result)
     }
     class CalculationRepository{
         calculations
     : add_calculation(content)
     : print_calculations()
     : count_calculations()
     }
```

![Package Structure and Classes](./photos/architecture-package-and-classes.png)
