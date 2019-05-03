# ISA (Instruction Set Architecture) 28 bits

## ISA Structure

**cond**(4) **op**(2) **IV**(2) **cmd**(4) **Rn**(4) **Rd**(4) **Src**(8)
**total bits** = 28

1. cond
   This indicates the FLAGS the processor is going to use.

2. op
   This indicates if the operation is arithmetic, of storage/read or branches, in this case we'll not use branches.

3. IV
   This indicate if we will use immediate or not, or also indicates if we will use vector functions.

4. cmd
   This is the operetion that we will use in the ALU for the arithmetics functions.

5. Rn
   This is the register is used for operate.

6. Rd
   This is the register where is going to be allocated the data.

7. Src
   This is the register or immediate that we are going to operate with the Rn.

## Definition of Instructions

### cond

**1110** this is the default for cond. We are going to use only this because we aren't using other cond FLAGS.

### op

- **00:**
  This operation is for arithmetic functions like ADD, SUB, ADDV, SUBV, CIRRV, CIRLV, XORV, ALGV.
- **01:**
  This operation is for using the memory STR, LDR, STRV, LDRV.
- **others:**:
  The other bits aren't used for this project.

### funct

1. **IV:**
   This means Immediate or Vector functions.
   - **00:**
     This is used for registers.
   - **01:**
     This is used for immediate.
   - **10:**
     This is used for vectors registers.
   - **11:**
     This is used for vector and immediate.
2. **cmd**
   - **0000:**
     This is used for ADD function.
   - **0001:**
     This is used for SUB function.
   - **0010:**
     This is used for XOR function.
   - **0011:**
     This is used for ADDV funtion.
   - **0100:**
     This is used for SUBV function.
   - **0101:**
     This is used for XORV function.
   - **0110:**
     This is used for ALGV function.

### **Rn** & **Rn**

This is a definition of registers of 15 normal registers and 8 vectorial registers.

### Src

This is the register of the immediate or registers/vectors.
