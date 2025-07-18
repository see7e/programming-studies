---
title: Python Data Transformations
tags:
  - studies
  - programming
  - python
  - transformation
  - performance
  - enums
  - mapping
  - data-analysis
  - data-quality
  - data-validation
  - data-cleaning
  - data-processing
  - data-structures
  - dictionary
use: Data Analysis
languages: Python
dependences: Pandas
---

<details> <summary>Table of Contents 🔖</summary>

- [Python Data Transformations - Converting Numeric Codes to Human-Readable Labels](#python-data-transformations---converting-numeric-codes-to-human-readable-labels)
  - [The Challenge](#the-challenge)
  - [Dictionary Mapping Solution](#dictionary-mapping-solution)
  - [Safe Handling of Unknown Values](#safe-handling-of-unknown-values)
  - [Advanced Transformation Patterns](#advanced-transformation-patterns)
    - [Function-Based Transformation](#function-based-transformation)
    - [Bidirectional Mapping](#bidirectional-mapping)
    - [Batch Processing with Pandas](#batch-processing-with-pandas)
  - [Best Practices](#best-practices)
    - [Separate Transformation from Rendering](#separate-transformation-from-rendering)
    - [Use Enums for Type Safety](#use-enums-for-type-safety)
    - [Validate Input Data](#validate-input-data)
  - [Common Use Cases](#common-use-cases)
  - [Performance Considerations](#performance-considerations)
- [References](#references)

</details>

---

# Python Data Transformations - Converting Numeric Codes to Human-Readable Labels
When working with data in Python, you'll often encounter **numeric codes that need to be converted to human-readable labels**. This is a common scenario in data processing, API responses, and database records where efficiency demands numeric storage but user interfaces require meaningful text.

## The Challenge
Consider a scenario where you have performance data with numeric codes:

```python
data = {
    "user_1": 20,
    "user_2": 70,
    "user_3": 10,
    "user_4": 99  # Unknown code
}
```

These numbers represent performance levels, but they're meaningless to end users. We need to transform them into readable labels like "Above Target", "On Target", and "Below Target".

## Dictionary Mapping Solution
The most efficient approach uses a dictionary for mapping numeric codes to their corresponding labels:

```python
value_mapping = {
    20: "Above Target",
    70: "On Target", 
    10: "Below Target"
}

# Transform the data
updated_data = {key: value_mapping.get(value, value) for key, value in data.items()}
```

This approach of [dictionary comprehension](https://www.geeksforgeeks.org/python/python-dictionary-comprehension/) offers several advantages:
- **Fast lookups**: Dictionary lookups are $O(1)$ operations
- **Safe handling**: The `.get()` method handles unknown values gracefully
- **Maintainable**: Easy to add, modify, or remove mappings

## Safe Handling of Unknown Values
The `.get()` method is crucial for robust data transformation:

```python
# Without safe handling (dangerous)
risky_transform = {key: value_mapping[value] for key, value in data.items()}
# This would raise KeyError for unknown codes

# With safe handling (recommended)
safe_transform = {key: value_mapping.get(value, value) for key, value in data.items()}
# Unknown codes remain unchanged

# With custom fallback
fallback_transform = {key: value_mapping.get(value, "Unknown") for key, value in data.items()}
# Unknown codes get a default label
```

## Advanced Transformation Patterns

### Function-Based Transformation
For more complex logic, wrap the transformation in a function:

```python
def transform_performance_codes(data, unknown_label="Unknown"):
    """Transform numeric performance codes to human-readable labels."""
    mapping = {
        20: "Above Target",
        70: "On Target", 
        10: "Below Target"
    }
    
    return {
        key: mapping.get(value, unknown_label if isinstance(value, int) else value)
        for key, value in data.items()
    }

# Usage
transformed = transform_performance_codes(data)
```

### Bidirectional Mapping
Sometimes you need to convert both ways:

```python
class PerformanceMapper:
    def __init__(self):
        self.code_to_label = {
            20: "Above Target",
            70: "On Target", 
            10: "Below Target"
        }
        self.label_to_code = {v: k for k, v in self.code_to_label.items()}
    
    def to_label(self, code):
        return self.code_to_label.get(code, code)
    
    def to_code(self, label):
        return self.label_to_code.get(label, label)

# Usage
mapper = PerformanceMapper()
print(mapper.to_label(20))  # "Above Target"
print(mapper.to_code("Above Target"))  # 20
```

### Batch Processing with Pandas
For large datasets, leverage `pandas` for efficient transformation:

```python
import pandas as pd

df = pd.DataFrame({
    'user_id': ['user_1', 'user_2', 'user_3'],
    'performance_code': [20, 70, 10]
})

# Method 1: Using map()
df['performance_label'] = df['performance_code'].map(value_mapping)

# Method 2: Using replace()
df['performance_label'] = df['performance_code'].replace(value_mapping)
```

## Best Practices

### Separate Transformation from Rendering
Keep data transformation logic separate from presentation logic:

```python
# Good: Separate concerns
def get_performance_mapping():
    return {
        20: "Above Target",
        70: "On Target", 
        10: "Below Target"
    }

def transform_data(data):
    mapping = get_performance_mapping()
    return {key: mapping.get(value, value) for key, value in data.items()}

def render_performance_report(data):
    transformed = transform_data(data)
    # Rendering logic here
```

### Use Enums for Type Safety
For better code maintainability. Why? Because using an `Enum` makes it explicit that you’re defining **a fixed set of known, named values**. This signals to anyone reading the code that there are **only these three valid performance levels**—nothing else.

Is much clearer and less error-prone than using ad-hoc constants or loose tuples.

```python
from enum import Enum

class PerformanceLevel(Enum):
    ABOVE_TARGET = (20, "Above Target")
    ON_TARGET = (70, "On Target")
    BELOW_TARGET = (10, "Below Target")
    
    def __init__(self, code, label):
        self.code = code
        self.label = label

# Create mapping from enum
performance_mapping = {level.code: level.label for level in PerformanceLevel}
```

 Regarding "Type Safety", when you pass around an `Enum` member, you can check it in a type-safe way. For example:
 
```python
def handle_performance(level: PerformanceLevel):
	if level == PerformanceLevel.ABOVE_TARGET: ...
```

Here, you’re guaranteed that `level` is one of your predefined `PerformanceLevel` values.  Contrast this with using raw tuples or integers—where any value could slip in unnoticed.

Another great point is the respect to [DRY](../../Docs/dry.md) principle: If you later change your `enum` (e.g., adding `EXCEPTIONAL`), you have **one place to update**, and it’s hard for the system to get into an inconsistent state. Compare this to multiple dicts or scattered constants—more chances of forgetting to update all the places.

### Validate Input Data
Add validation to catch data quality issues early:

```python
def validate_and_transform(data):
    """Validate input data and transform performance codes."""
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    
    mapping = {20: "Above Target", 70: "On Target", 10: "Below Target"}
    unknown_codes = set()
    
    transformed = {}
    for key, value in data.items():
        if isinstance(value, int) and value not in mapping:
            unknown_codes.add(value)
        transformed[key] = mapping.get(value, value)
    
    if unknown_codes:
        print(f"Warning: Unknown codes found: {unknown_codes}")
    
    return transformed
```

## Common Use Cases
This pattern is particularly useful for:
- **Status codes**: Converting HTTP status codes to messages
- **Category IDs**: Transforming database category IDs to names
- **Error codes**: Converting numeric error codes to user-friendly messages
- **Configuration values**: Transforming setting IDs to readable options
- **API responses**: Converting service response codes to client-friendly labels

## Performance Considerations
Dictionary lookups are highly efficient, but for extremely large datasets, consider:
- **Caching**: Store transformed results to avoid repeated calculations
- **Lazy evaluation**: Transform data only when needed
- **Batch processing**: Use vectorized operations with pandas or numpy

---

Dictionary mapping with the `.get()` method provides a robust, efficient solution for transforming numeric codes to human-readable labels. This approach handles unknown values gracefully, maintains good performance, and keeps your code clean and maintainable.

The **key principles to remember**:
- Use **dictionary mapping for fast, clean transformations**
- Always **handle unknown values with `.get()` method**
- **Separate transformation logic from presentation logic**
- Consider **using enums for better type safety**
- **Validate input data** when *data quality is a concern*

This pattern forms the foundation for more complex data transformation scenarios and integrates well with frameworks like Django, Flask, and data processing libraries like pandas.

# References
- [Python Dictionary Comprehension](https://www.geeksforgeeks.org/python/python-dictionary-comprehension/)
- [Python Enum Documentation](https://docs.python.org/3/library/enum.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python Data Validation](https://docs.python.org/3/library/exceptions.html#TypeError)
- [Python Performance Tips](https://docs.python.org/3/howto/performance.html)
- [Python Best Practices](https://docs.python-guide.org/writing/style/)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Error Handling](https://docs.python.org/3/tutorial/errors.html)
- [Python Dictionary Methods](https://docs.python.org/3/library/stdtypes.html#dict)
