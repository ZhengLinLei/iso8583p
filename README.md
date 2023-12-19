# iso8583p.py

[![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


PIP package install:
```
pip install iso8583p
```

Follow the steps in [Pypi](https://pypi.org) to run the project like a python module
Pypi [https://pypi.org/project/iso8583p/](https://pypi.org/project/iso8583p/)



## How to run it?

### 1. Install modules

Install all the modules in `setup.py` file path
```
py setup.py install 
```

Linux user
```
python3 setup.py install
```

or with PIP
```
pip install iso8583p
```

### 2. Import to project

Import the module in your python file, and run it
```python
import iso8583p
```

```python
from iso8583p import Iso8583, MemDump, Str2Bcd, IsoSpec1987BCD

IsoPacket = Iso8583(IsoSpec = IsoSpec1987BCD())

# Create an example ISO message
# 1200 Message, type Sale

IsoPacket.MTI("1200")
# Field 2
IsoPacket.Field(2, 1)
IsoPacket.FieldData(2, 8888806368324521)
# Field 3
IsoPacket.Field(3, 1)
IsoPacket.FieldData(3, 000000)

IsoPacket.PrintMessage()
data = IsoPacket.BuildIso()
data = struct.pack(b"!!", len(data)) + data         
MemDump("Sending:", data)
```

Linux user run the command in your terminal with `python3` and `pip3`

### Love this repo? Give us a star ⭐

<a href="./">
  <img src="https://img.shields.io/badge/iso8583p-Rate-blue">
</a>
