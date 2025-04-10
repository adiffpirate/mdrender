# My Awesome Markdown Test Document

This document is designed to comprehensively test the rendering capabilities of your terminal Markdown tool. It includes a variety of formatting options, nested lists, code snippets, and more.

## Introduction

Welcome!  This is a demonstration of how Markdown can look and behave in a terminal environment.  Let's see if it handles everything correctly.

### Important Notes

*   Pay close attention to the numbering of the lists below.
*   Verify that code fences are displayed correctly with appropriate syntax highlighting.
*   Check the handling of bold, italic, and underlined text.
*   Make sure that the table is rendered without errors.

## Nested Lists

This section demonstrates nested lists.

1.  Level 1
    *   Level 2
        1.  Level 3
        *   Level 3.1
        *   Level 3.2
    *   Level 2.1
    *   Level 2.2

## Code Examples

Let's showcase some code snippets:

```python
def hello_world():
  print("Hello, world!")

hello_world()
```

```javascript
console.log("This is some JavaScript code.");
```

```bash
echo "This is a bash command."
```

## Formatting Options

This section tests various formatting options:

*   **Bold** text is important to render correctly.
*   *Italic* text should also be displayed properly.
*   `Inline code` is frequently used.
*   <u>Underlined</u> text is a visual marker.  It's a bit trickier to render well.
*   ~~Strikethrough~~ text should be displayed with a strikethrough effect. (Might not work everywhere)

## Tables

Let's see how the table rendering works:

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Cell 1   | Cell 2   | Cell 3   |
| Row 2    | Row 2    | Row 2    |
| Row 3    | Row 3    | Row 3    |

## Blockquotes

This demonstrates blockquotes:

> This is a blockquote.
> It can span multiple lines.
>  Feel free to add more indentation for visual clarity.

## Horizontal Rule

---

## References and Links

Here are some links and references:

[Example Link](https://www.example.com)

*   [Another Link](https://www.wikipedia.org/)
*   [GitHub](https://github.com/) - A popular platform for developers.

## Task Lists (Checkboxes)

This demonstrates task lists:

- [ ]  Task 1: Complete the testing.
- [ ]  Task 2: Verify the table rendering.
- [x]  Task 3:  Successfully completed!
- [ ]  Task 4:  Future work...

## Image and Emoji

![A cute cat](https://placekitten.com/Image/wide)
😊 😄 🤩

## Section with Multiple Code Fences

This section includes multiple code fences to ensure that the renderer handles them correctly.

```cpp
#include <iostream>

int main() {
  std::cout << "Hello, world!" << std::endl;
  return 0;
}
```

```rust
fn main() {
  println!("Hello, world!");
}
```

```html
<!DOCTYPE html>
<html>
<head>
  <title>Example HTML</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```

## Section with Nested Code Fences

````markdown
# Code Project

This is the README.md example for a cool json parser.

## Installation

```bash
pip install cooljsonparser
```

## Usage

Parse json file

```bash
cooljsonparser -f file.json
```
````
