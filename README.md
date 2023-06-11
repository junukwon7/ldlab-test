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
* [RISC processor with Verilog](https://www.fpga4student.com/2017/04/verilog-code-for-16-bit-risc-processor.html)
* [Fictional processor with Python](https://github.com/tdjsnelling/tis-100-python)
* [Sample Microprocessor Instructions](https://raw.githubusercontent.com/skystar-p/logic-design-test-case/master/test2.test)
* [16-bit CPU with Verilog](https://github.com/vprabhu28/16-Bit-CPU-using-Verilog)
* 
