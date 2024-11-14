---
name: Bug report
about: Create a report to help us improve this library
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description
A clear and concise description of what the bug is.

## Environment
- Python version: [e.g., 3.8.10]
- Library version: [e.g., 1.2.0]
- OS: [e.g., Ubuntu 20.04, macOS 12.0]
- Dependencies versions (if relevant):
  ```
  httpx==0.24.0
  ```

## Steps To Reproduce
1. Initialize client with '...'
2. Call method '...'
3. Pass parameters '...'
4. See error

## Expected Behavior
A clear and concise description of what you expected to happen.

## Actual Behavior
What actually happened, including error messages, stack traces, or unexpected responses.

```python
# Code sample that reproduces the issue
from novaposhta.client import NovaPoshtaApi

client = NovaPoshtaApi('my-api-token', timeout=30)
response = client.some_method()  # Error occurs here
```

```
# Error output or stack trace if applicable
Traceback (most recent call last):
  ...
Error: Description of the error
```

## API Response (if applicable)
```json
{
  "error": "Error message from API"
}
```

## Additional Context
- Have you reviewed the documentation?
- Are you using any special configuration?
- Any other context about the problem?

## Possible Solution
If you have any ideas about what might be causing the issue or how to fix it, please share them here.
