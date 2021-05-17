# Radon Markdown Reports

Utility for executing [Radon](https://radon.readthedocs.io/en/latest/) analysis on a specific folder.

The following metrics will be processed and gathered into a single md table:

- Cyclomatic complexity (CC)
- Maintainability Index (MI)

### Usage

```bash
python main.py <path_to_harvest>
```

### Sample result

| File | MI | Type | Name | CC |
--- | --- | --- | --- | ---
| main.py | <b>A</b> | | | |
| main.py | | F | convert_results | <b>B</b> |
| main.py | | F | write_report | <b>A</b> |
| main.py | | F | harvest | <b>A</b> |
| main.py | | C | ContentResult | <b>A</b> |
| main.py | | C | FileResult | <b>A</b> |

### License

Copyright 2021, [percil](https://github.com/percil).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
