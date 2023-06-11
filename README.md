# Logic Design Assembly Test Code

This repository provides a series of sample instruction codes which can used for evaluate the actuall microprocessor implementation.

Upload one of the Verilog modules to a secondary board, and connect pins for testing.

Also, use `process.py` for testing the code. It's a python-based microprocessor implementation which also provides detailed step-by-step analysis.

Sample usage:
```bash
# Upload your microprocessor to the FPGA
# Upload imem1.py to the FPGA
python process.py imem1.v
# Check the differences
```

# Reference
* LDLAB SPEC
* [Assembly Runner](https://github.com/benWindsorCode/assemblyRunner) by benWindsorCode
* [Fictional processor with Python](https://github.com/tdjsnelling/tis-100-python) by tdjsnelling
* [Sample](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test2.test) [Microprocessor](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test3.test) [Instructions](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test4.test) by skystar-p
* [Turing Complete (GAME)](https://store.steampowered.com/app/1444480/Turing_Complete/) by levelhead
