## Prototype analytical core
---
###### title: "Prototype analytical core"
###### author: Osintsev Artem
###### date: 19.05.2022
---
The analytical core processes incoming requests for data processing using predictive analysis methods. The result of the work is a JSON package with the results of the analysis. A packet with the result is sent to the client from which the data came.

## Installation

Step 1. Clone project from GitHub:
```sh
git clone https://github.com/kubenet/analytical_core.git
```

Step 2. Execute setup.py: 
```sh
pip install -e . 
```

Step 3. Run web web-server uvicorn:  
```sh
uvicorn main:app 
```
