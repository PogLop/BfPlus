# Brainfuck+
Custom made bf compiler + some more features. Read the docs for
help.

## **Docs**
Basic documentation for bfPlus
## Introduction

BfPlus works like normal brainfuck, except there are some more functions. So that means, it uses 10 keywords in total (there will be more in the future). Lets have a look at them.

## Basics

List of added keywords: 

```
* = multi-move -> moves pointer according to given number
@ = multi-add -> sets current memory block to given number
```

## Running code

There are three options to run your bf+ script:
- Use the function bf(*code*) inside main script
- Inside terminal run `python bfp_compiler.py "<your_code>"`
- Import bf+ into your script (in future bf+ will be available as pip package)