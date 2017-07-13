# Formatting

## Guidelines

Use standard guidelines

* PEP-8 for Python

* Use corporation guidelines

* Use team guidelines

## Separation

* Vertical
  * Declare variable with small vertical scope. Just before usage
  * Avoid global/large scope variables/object.

* Horizontal
  * Separate huge one-liners

## Function formatting

* Use language idioms and best practices

* Separate try-except blocks, and handle them as a additional level of abstraction
  * Don't raise them again to catch at the top level!