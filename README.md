[![DOI](https://zenodo.org/badge/671239911.svg)](https://zenodo.org/badge/latestdoi/671239911)

The Circuits folder includes all the experimental results.

Please be aware that we have employed the source codes provided in the following repository:([ePrint](https://eprint.iacr.org/2021/1400))


# Run Boyar-Peralta with XOR2 / XOR3 / XOR4 gates

```console
foo@bar:~$ python3 run_bp_xor3.py --help

usage: run_bp_xor3.py [-h] [-xor4c XOR4C] [-xor3c XOR3C] [-iwsec] -xor2c XOR2C
                      -iterations ITERATIONS [-path PATH] -matrix MATRIX

Run Boyar-Peralta with XOR2 / XOR3 / XOR4

optional arguments:
  -h, --help            show this help message and exit
  -xor4c XOR4C          Cost of XOR4 gates
  -xor3c XOR3C          Cost of XOR3 gates
  -iwsec                Run IWSEC algorithm for XOR3 gates
  -xor2c XOR2C          Cost of XOR2 gates
  -iterations ITERATIONS
                        Number of iterations
  -path PATH            Path for matrix file
  -matrix MATRIX        Name of matrix file
```

#### Examples
1. To run Boyar-Peralta with XOR-2 gates for AES matrix:
    ```console
    foo@bar:~$ python3 run_bp_xor3.py -xor2c 1.0 -iterations 1000 -path matrices -matrix AES.txt
    ```
2. To run Boyar-Peralta with XOR-3 and XOR-2 gates for AES matrix:
    ```console
    foo@bar:~$ python3 run_bp_xor3.py -xor3c 1.625 -xor2c 1.0 -iterations 1000 -path matrices -matrix AES.txt
    ```
3. To run Boyar-Peralta (IWSEC) with XOR-3 and XOR-2 gates for AES matrix:
    ```console
    foo@bar:~$ python3 run_bp_xor3.py -xor2c 1.0 -iwsec -iterations 1000 -path matrices -matrix AES.txt
    ```
4. To run Boyar-Peralta with XOR-4, XOR-3 and XOR-2 gates for AES matrix:
    ```console
    foo@bar:~$ python3 run_bp_xor3.py -xor4c 2.4 -xor3c 1.625 -xor2c 1.0 -iterations 1000 -path matrices -matrix AES.txt
    ```
