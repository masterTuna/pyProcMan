# pyProcMan
Process Manager in Python for Windows
The purpose for this python code is to
create a running process and when the 
running process runs into error, the
try - exception code will catch it and
create a STATUS file. the Process Manager
keep monitoring this file and will kill 
the old process and invoke a new one when
it detects the existence of a complete 
STATUS file.
