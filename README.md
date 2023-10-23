---
title: Studies - Root
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
banner: "![[proggramming_banner.jpg]]"
banner_y: 0.5
banner_lock: true
---

> [!INFO] 
> The links are built for the obsidian branch, i was working in main but now i'll split correctly and after that update all the inter document links over the main branch

---

> This is a list of interesting documents gathered during development studies
# The Big Picture 🌌

This repo is divided in two branches, [main](https://github.com/see7e/programming-studies) has common links and [obsidian](https://github.com/see7e/programming-studies/tree/obsidian) links follow a Zettelkasten adapted model along with Obsidian to map the network of documents. If you want to set up in you computer, [click here](obisidian_init.md).

<details>
	<summary>If you want to know the history, click here.</summary>
	<p>
		I've started using Obsidian and found very userfull to see how my brain works, and all its connections. Sometime after stumbled with the Zettelkasten method, it fits right into the philosophy of the program.</p>
    <p>
	    But the problem is that all my information was divided in a big folder structure, so I took my time and started thinking about how to conciliate both methods, PARA and Zettel.
    </p>
    <p>
	    The links, the special <code>[[]]</code> Obsidian type and the common <code>[](./path/to/file)</code>. The first one don't work in GitHub, and the second one if is a web url Obsidian won't link the way we expect. So what I will do/did is put altogether in one folder, and set <code>.gitignore</code> for exclude the independent sub-folders which are individual repositories, and with that Git won't create a mess during the commits and pushes.
    </p>
</details>

</br>

![Galaxy|500](./src/img/prog-galaxy.png)


# [List of Documents](DIRECTORY.md) 📜

> [!QUOTE] 
> If I have seen further, it is by standing on the shoulders of giants.
> *Isaac Newton*

## [A Fresh start](./Docs/fresh_start.md) 🛣️

Sometimes in the rush to resolve the problems that we face, the learn only to fill the gap that is presented by the obstacle. So I'll try to visit the core/basic concepts of CS, using some guidelines.

## Progress 🏗️

This graph reflects the themes that I'm studying, and the progress of each one. The tree divisions will follow the three different contexts (work, 42 and personal).


```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#23375E',
      'primaryTextColor': '#FFF',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229'
    }
  }
}%%

gantt
  title My Roadmap
  dateFormat DD-MM-YYYY
  tickInterval 1month

  section Work
    %% October
    Networking              :active, 02-10-2023, 30d
    Authentication Systems  :active, 02-10-2023, 01-11-2023
    %% November
    Backend                 :20d

  section 42
    %% October
    Libft                   :active, 02-10-2023, 16-10-2023
    ft_printf               :17-10-2023, 15d
    %% November
    Get_Next_Line           :15d
    Born2beroot             :5d
    %% December

  section Personal
    %% October
    Operating Systems       :active, 02-10-2023, 30d
    Sockets                 :milestone, 16-10-2023, 0d
    Processos e threads     :milestone, 17-10-2023, 0d
    %% November
    Competitive Programming :01-11-2023, 30d
    Code cohesion           :01-11-2023, 7d
    Code coupling           :7d
    Memory Management       :15d
    %% December
    Framewok implementation :01-12-2023, 30d
    C Compilation           :01-12-2023, 7d
    Code Diagnosis          :7d

  section TimeLine
    timespan=thee months :active, 01-10-2023, 31-12-2023

```
> Here's the [archive](progress_archive.md). 

## First time with Markdown? 📑
> Enter [here](first-time.md)

## Some useful links [🔗](links.md) 

## Readings 📚

- Modern Operating Systems - Andrew S. Tanenbaum, Herbert Bos
- Statistical Learning - Trevor Hastie, Robert Tibshirani
- Design Patterns: Elements of Reusable Object-Oriented Software - Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
- Compilers - Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman
- Clean Code - Robert C. Martin
- Refactoring - Martin Fowler, Kent Beck, John Brant, William Opdyke, Don Roberts
- Pragmatic Programmer - From Journeyman to Master - Andrew Hunt, David Thomas
- Make it stick - The Science of Successful Learning - Peter Brown, Henry L. Roediger III, Mark A. McDaniel
- Computer Networking - Andrew S. Tanenbaum, David J. Wetherall

---