# Architectural illustration

## Structure

![Package Structure](./photos/architecture-package.png)

Package _ui_ contains user interface, _services_ contains application logic and _repositories_ contains code corresponsible for saving calculations.

## Application logic

Class CalculationService forms and responds for application logic, which represents different calculations and their storage through CalculationRepository.

```mermaid
 classDiagram
     class CalculationService{
     : string_to_number()
     : sum_service()
     : sub_service()
     : mul_service()
     : div_service()
     : count()
     : return_calculations()
     : add()
}
```

![Package Structure and Classes](./photos/architecture-package-and-classes.png)
