# unknown-numbers

### What does this repo do ?

This repo allows you to create exponential terms using unknown numbers comfortably. You can do various math applications using this repository. Like binomial expansion, derivative, integral...


**How do you install this package ?**
```commandline
pip install unknown-terms
```

**How do you use ?**

```python
from unknown_terms.alpha_term import *

# In this way, you can use every class on the package.
```

**Quick Note: If you don't want this project as a 
package you had to change this lines in alpha_term.py** 

```python
from .multiple_alpha_term import MultipleAlphaTerm
from .printer import TermPrinter
```

**to**
 
 ```python
from multiple_alpha_term import MultipleAlphaTerm
from printer import TermPrinter
```


### AlphaTerm class

You can create a term with a single unknown.

```python
term1 = AlphaTerm(2, "x", 3)  # Created AlphaTerm object
term2 = AlphaTerm(3, "y", 2)
term3 = AlphaTerm(0, "z", 2)
term4 = AlphaTerm(3, "t", 0)
term5 = AlphaTerm(0, "a", 0)
term6 = AlphaTerm() # AlphaTerm(1, "x", 1)

# METHODS
print(term1, term5, term4, sep=" , ")
# prints irregular term -> 2.0x³ , 0.0a⁰ , 3.0t⁰

# TermPrinter.print method returns regular term
print(TermPrinter.print(term1))  # 2x³
print(TermPrinter.print(term5))  # (nothing)
print(TermPrinter.print(term4))  # 3t

# Multiplication 
mterm = term1 * term2
print(mterm)  # 6.0x³y² -> This is a MultipleAlphaTerm object
print(TermPrinter.print(mterm))  # 6x³y²

# Division
mterm = term2 / term4
print(mterm)  # 1.0y²t⁰
print(TermPrinter.print(mterm))  # y²

# Exponentiation
new_term = term2 ** 2
print(new_term) # prints 9y⁴

# Turn to known
number = term1.turn_to_known(value=5)
print(number)  #prints 250


```


- _NOT: Operations such as exponentiation, division, multiplication can also be applied to objects in the MultipleAlpaTerm class._
