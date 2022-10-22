# Brainfuck+
Custom made bf interpreter + some extra features. Read the docs for
help.

## **Docs**
Basic documentation for bfPlus
## Introduction

BfPlus uses 10 keywords instead of 8 like normal brainfuck. Lets have a look at them.

## Basics

List of new keywords: 

```
* = multi-move -> moves pointer according to given number
@ = setter -> sets current memory block to given number
```

## Running code

There are three options to run your bf+ script:
- Use the function bf(*code*) inside main script or import it to antoher project
- Inside terminal run `python bfp_compiler.py "<your_code>"
