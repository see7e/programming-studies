---
title: First Time - Markdown
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

# Intro

> [User Guide](https://help.obsidian.md/Home)

![user-guide-network|400](user-guide-net.png)

## Getting started

> [Roadmap](https://trello.com/b/Psqfqp7I/obsidian-roadmap)

If you're new to Obsidian, learn the basics of note-taking with Obsidian using our guides:

1.  [Download and install Obsidian](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian)
2.  [Create a vault](https://help.obsidian.md/Getting+started/Create+a+vault)
3.  [Create your first note](https://help.obsidian.md/Getting+started/Create+your+first+note)
4.  [Link notes](https://help.obsidian.md/Getting+started/Link+notes)

From here, you can build your own custom experience by enabling additional features through _plugins_. Explore the [Core plugins](https://help.obsidian.md/Plugins/Core+plugins) that ships with Obsidian, or any of our [Community plugins](https://help.obsidian.md/Extending+Obsidian/Community+plugins).

Customize the look and feel of Obsidian using [Themes](https://help.obsidian.md/Extending+Obsidian/Themes) and [CSS snippets](https://help.obsidian.md/Extending+Obsidian/CSS+snippets).

# Syntax

This [site](https://www.markdownguide.org/basic-syntax/) provides a good amount of information about the syntax using examples and the "code" snipets, but will add some more userfull and important.

### Headings

To create a heading, add number signs (`#`) in front of a word or phrase. The number of number signs you use should correspond to the heading level. For example, to create a heading level three (`<h3>`), use three number signs (e.g., `### My Header`).

| Markdown                 | HTML                       |
| ------------------------ | -------------------------- |
| `# Heading level 1`      | `<h1>Heading level 1</h1>` |
| `## Heading level 2`     | `<h2>Heading level 2</h2>` |
| `### Heading level 3`    | `<h3>Heading level 3</h3>` |
| `#### Heading level 4`   | `<h4>Heading level 4</h4>` |
| `##### Heading level 5`  | `<h5>Heading level 5</h5>` |
| `###### Heading level 6` | `<h6>Heading level 6</h6>` |

This can be filtered by the automatic Table of Contents (`- [header](#header)`). For best practice, you should also put blank lines before and after a heading for compatibility.

### Paragraphs

To create paragraphs, use a blank line to separate one or more lines of text. Unless the [paragraph is in a list](https://www.markdownguide.org/basic-syntax/#paragraphs), don’t indent paragraphs with spaces or tabs.

### Bold

To bold text, add two asterisks or underscores before and after a word or phrase. To bold the middle of a word for emphasis, add two asterisks without spaces around the letters.

| Markdown                     | HTML                                      | Rendered Output            |
| ---------------------------- | ----------------------------------------- | -------------------------- |
| `I just love **bold text**.` | `I just love <strong>bold text</strong>.` | I just love **bold text**. |
| `I just love __bold text__.` | `I just love <strong>bold text</strong>.` | I just love **bold text**. |
| `Love**is**bold`             | `Love<strong>is</strong>bold`             | Love**is**bold             |

Markdown applications don’t agree on how to handle underscores in the middle of a word. For compatibility, use asterisks to bold the middle of a word for emphasis.

### Italic

To italicize text, add one asterisk or underscore before and after a word or phrase. To italicize the middle of a word for emphasis, add one asterisk without spaces around the letters.

| Markdown                               | HTML                                          | Rendered Output                      |
| -------------------------------------- | --------------------------------------------- | ------------------------------------ |
| `Italicized text is the *cat's meow*.` | `Italicized text is the <em>cat's meow</em>.` | Italicized text is the _cat’s meow_. |
| `Italicized text is the _cat's meow_.` | `Italicized text is the <em>cat's meow</em>.` | Italicized text is the _cat’s meow_. |
| `A*cat*meow`                           | `A<em>cat</em>meow`                           | A*cat*meow                           |

Markdown applications don’t agree on how to handle underscores in the middle of a word. For compatibility, use asterisks to italicize the middle of a word for emphasis.

## Blockquotes

To create a blockquote, add a `>` in front of a paragraph.

```
> Dorothy followed her through many of the beautiful rooms in her castle.
```

The rendered output looks like this:

> Dorothy followed her through many of the beautiful rooms in her castle.

Blockquotes can contain multiple paragraphs. Add a `>` on the blank lines between the paragraphs.

```
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

## Lists

You can organize items into ordered and unordered lists.

### Ordered Lists

To create an ordered list, add line items with numbers followed by periods. The numbers don’t have to be in numerical order, but the list should start with the number one.

1.  First item
2.  Second item
3.  Third item
    1.  Indented item
    2.  Indented item
4.  Fourth item

#### Ordered List Best Practices

CommonMark and a few other lightweight markup languages let you use a parenthesis (`)`) as a delimiter (e.g., `1) First item`), but not all Markdown applications support this, so it isn’t a great option from a compatibility perspective. For compatibility, use periods only.

| ✅  Do this                          | ❌  Don't do this                    |
| ------------------------------------ | ------------------------------------ |
| `1. First item`</br>`2. Second item` | `1) First item`</br>`2) Second item` |

### Unordered Lists

To create an unordered list, add dashes (`-`), asterisks (`*`), or plus signs (`+`) in front of line items. Indent one or more items to create a nested list.

- First item
- Second item
- Third item
    - Indented item
        - Indented item
- Fourth item

## Images

`![alt-text](url)`

## Code

To denote a word or phrase as code, enclose it in backticks (`` ` ``).

| Markdown | HTML | Rendered Output |
| --- | --- | --- |
| ``At the command prompt, type `nano`.`` | `At the command prompt, type <code>nano</code>.` | At the command prompt, type `nano`. |

### Escaping Backticks

If the word or phrase you want to denote as code includes one or more backticks, you can escape it by enclosing the word or phrase in double backticks (` `` `).

| Markdown | HTML | Rendered Output |
| --- | --- | --- |
| ``` ``Use `code` in your Markdown file.`` ``` | ``<code>Use `code` in your Markdown file.</code>`` | ``Use `code` in your Markdown file.`` |

### Code Blocks

To create code blocks, indent every line of the block by at least four spaces or one tab. Additionally you can use the  \`\`\`language to highlight the elements.

```html
    <html>
      <head>
      </head>
    </html>
```

## Links

To create a link, enclose the link text in brackets (e.g., `[Duck Duck Go]`) and then follow it immediately with the URL in parentheses (e.g., `(https://duckduckgo.com)`).

```
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
```

The rendered output looks like this:

My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

### Image link

To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.

```
[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
```


> [!INFO]
> If this isn't enough to help you, try to read from a more advanced [text](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax) tutorial