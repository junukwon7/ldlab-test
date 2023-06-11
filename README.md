# Logic Design Assembly Test Code

This repository provides a series of sample instruction codes which can used for evaluate the actuall microprocessor implementation.

Upload one of the Verilog modules to a secondary board, and connect pins for testing.

Also, use `process.py` for testing the code. It's a python-based microprocessor implementation which also provides detailed step-by-step analysis.

Sample usage:
```bash
# Upload your microprocessor to the FPGA
# Upload imem1.py to the FPGA
python process.py --file imem1.v
# Check the differences
```

# Reference
* LDLAB SPEC
* [TIS-100 Runner (GAME)]([https://www.fpga4student.com/2017/04/verilog-code-for-16-bit-risc-processor.html](https://github.com/benWindsorCode/assemblyRunner))
* [Fictional processor with Python](https://github.com/tdjsnelling/tis-100-python)
* [Sample](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test2.test) [Microprocessor](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test3.test) [Instructions](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test4.test)
* [Turing Complete (GAME)](https://store.steampowered.com/app/1444480/Turing_Complete/)
