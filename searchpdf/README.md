
# searchPDF

no more manually searching a terms from multiple pdfs. this tool will locate terms from multiple pdfs and returns filename and the first found pagenumber  in the given pdf

## directory structure
```
.
├── main.py
├── Unit1-Introduction.pdf
├── Unit2-OS Structure.pdf
├── Unit3-Process Management.pdf
├── Unit3-Process Scheduling.pdf
├── Unit4-Deadlock.pdf
├── Unit5-Memory Management.pdf
├── Unit5-MM-Virtual Memory.pdf
├── Unit6-Input-Output Device Management.pdf
├── Unit8-Security Management.pdf
└── Unit9-Distributed OS.pdf
````

## usage
```
python3 main.py
```

## output
```
search for : process management
searching in Unit5-MM-Virtual Memory.pdf pages=>  43
searching in Unit6-Input-Output Device Management.pdf pages=>  73
searching in Unit1-Introduction.pdf pages=>  44
searching in Unit3-Process Management.pdf pages=>  113
searching in Unit8-Security Management.pdf pages=>  41
searching in Unit5-Memory Management.pdf pages=>  78
searching in Unit4-Deadlock.pdf pages=>  59
searching in Unit9-Distributed OS.pdf pages=>  44
searching in Unit2-OS Structure.pdf pages=>  47
searching in Unit3-Process Scheduling.pdf pages=>  65

Check these pdf:
Unit1-Introduction.pdf page no 39
Unit3-Process Management.pdf page no 1
Unit2-OS Structure.pdf page no 22
Unit3-Process Scheduling.pdf page no 1
```
