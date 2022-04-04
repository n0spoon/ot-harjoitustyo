```mermaid
 sequenceDiagram
     Main->>Machine: Machine()
     Machine->>FuelTank: FuelTank()
     FuelTank->>FuelTank: fuel_contents = 0
     Machine->>FuelTank: fill(40)
     FuelTank->>FuelTank: fuel_contents = 40
     Machine->>Engine: Engine(FuelTank)
     Main->>Machine: drive()
     Machine->>Engine: start()
     Engine-->>FuelTank: consume(5)
     FuelTank->>FuelTank: fuel_contents = 35
     Machine->>Engine: is_running()
     Engine-->>Machine: True
     Machine->>Engine: use_energy()
     Engine-->>FuelTank: consume(10)
     FuelTank->>FuelTank: fuel_contents = 25
     Machine->>Engine: running
     Engine-->>Machine: True
     Machine->>Engine: use_energy()
     Engine-->>FuelTank: consume(10)
     FuelTank->>FuelTank: fuel_contents = 15
     Machine->>Engine: running
     Engine-->>Machine: True
     Machine->>Engine: use_energy()
     Engine-->>FuelTank: consume(10)
     FuelTank->>FuelTank: fuel_contents = 5
```
