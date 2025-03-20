# DSENSP - Dynamic Self-Evolving Network Security Protocol

## Overview
DSENSP is an innovative network security protocol that autonomously evolves its encryption, routing, and deception mechanisms using a genetic algorithm. It is designed to adapt in real time to dynamic network conditions and emerging cyber threats.

## Project Structure
DSENSP/
├── docs/                    
├── src/                     
│   ├── main/                
│   │   ├── protocol/        
│   │   ├── ga/              
│   │   ├── network_simulation/  
│   │   └── logging/         
│   │   └── main.py          
│   └── test/                
├── experiments/             
├── scripts/                 
├── requirements.txt         
├── README.md                
└── LICENSE                  
## Quick Start

1. Set Up Environment:
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt

2. Run the Simulation:
   Navigate to src/main/ and execute:
     python main.py
   Or use:
     ./scripts/run_simulation.sh

3. Run Tests:
   From src/test/ run:
     python -m unittest discover

4. Analyze Results:
     ./scripts/analyze_results.py

## License
See LICENSE for licensing information.
