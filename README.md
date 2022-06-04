# xml_to_db
Converting [Orphanet Nomenclature](http://www.orphadata.org/cgi-bin/ORPHAnomenclature.html) into a searchable database

## Setup
### Clone project
* ```bash 
  git clone https://github.com/mcfa77y/xml_to_db.git
  ```
### Install 
* [Poetry](https://python-poetry.org/docs/)
*   ```bash 
    # Go to project directory
    cd xml_to_db
    
    # Install Poetry (a Python package manager)
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    
    # Install necessary dependencies for xml to db project
    poetry install
    ```
### Run
* ```bash 
  # Run translations of xml to Python classes
  poetry run python xml_chicanery/main.py  
  ```
* this will yield the first 2 disorder objects from `data_small.xml`

## Misc commands
* Create UML code
  * ```bash 
    poetry run xsdata input/from_xml.xsd --output plantuml --package uml_class_diagram  
    ```
  * this will create a directory `uml_class_diagram` with `from_xml.pu` file that can be visualized at [plantuml](https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)

* Create Python classes
  * ```bash 
    poetry run xsdata input/from_xml.xsd  --package model
    ```
  * this will create Python classes in the `model` directory with the `from_xml.py` file




