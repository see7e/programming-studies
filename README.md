---
title: Studies - Root
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

> [!] The links are built for the obsidian branch, i was working in main but now i'll split correctly and after that update all the inter document links 

---

> This is a list of interesting documents gathered during development studies
# The Big Picture

<details>
	<summary>If you want to know the history, click here.</summary>
	<p>I've started using Obsidian and found very userfull to see how my brain works, and all its connections. Sometime after stumbled with the Zettelkasten method, it fits right into the philosophy of the program.</p>
    <p>
    But the problem is that all my information was divided in a big folder structure, so I took my time and started thinking about how to conciliate both methods, PARA and Zettel.
    </p>
    <p>
    The links, the special <code>[[]]</code> Obisidian type and the common <code>[](./path/to/file)</code>. The first one don't work in GitHub, and the second one if is a web url Obisian won't link the way we expect. So what I will do/did is put altoghether in one folder, and set <code>.gitignore</code> for exclude the independent subfolders wich are individual repositories, and with that Git won't create a mess during the commits and pushs.
    </p>
</details>

</br>

<p align="center">
  <picture>
    <img alt="List_logo" src="./src/img/prog-galaxy.png" style="width:500px">
  </picture>
</p>

This repo is divided in two branches, [main](https://github.com/see7e/programing-studies) has common links and [obsidian](https://github.com/see7e/programing-studies/tree/obsidian) links follow a Zettelkasten adapted model along with Obsidian to map the network of documents. If you want to set up in you computer, [click here](./obisidian_init.md).

# [List of Documents](./DIRECTORY.md)

## Progress

<table>
    <thead>
        <tr>
            <th>HOURS</br>(18h ~ 19:30)</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1ª Part</td>
            <td rowspan=3>(C) CS50</td>
            <td rowspan=2>(Python)</br>Roadmap</td>
            <td rowspan=2>Revisão</td>
            <td>(Python)</br>Libraries</td>
            <td rowspan=3>(C) CS50</td>
        </tr>
        <tr>
            <td>2ª Part</td>
            <td rowspan=2>(Python)</br>Roadmap</td>
        </tr>
        <tr>
            <td>3ª Part</td>
            <td>(Python)</br>Libraries</td>
            <td>PowerBI /</br>Powerapps</td>
        </tr>
    </tbody>
</table>


```mermaid
gantt
	title My Roadmap
    dateFormat  DD-MM-YYYY
    section C
    CS50                    :a1, 02-05-2023, 90d
    42-Common Core          :a2, 02-10-2023, 10d

    section Python
    RoadMap                 :02-05-2023, 60d
    OpenPyXL                :10-05-2023, 5d
    Pandas                  :17-05-2023, 5d
    Lib, No. 3              :24-05-2023, 5d
    Lib, No. 4              :31-05-2023, 5d

    section SQL
    SQL RoadMap             :06-06-2023, 30d
    PostgreSQL              :30d
    PostGis                 :20d

    section Other
    PowerBI (not started)   :02-05-2023, 30d
    PowerApps               :10d
```

Basically, I set aside the days when I have more time to study C and Python, which are the biggest demands. Then comes SQL (Postgre and PostGis) along with PowerBI and PowerApps, for application in the company.

About the time, if you manage to reconcile between demands intervals, great, if not... Use the reserved time per day.

---

**LINKS** (need remember to filter after when I have the time #REVISAR )
- https://roadmap.sh
- cs50
	- https://cs50.me/cs50x
	- https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home
- https://egghead.io/q?access_state=free
- https://my-learning.w3schools.com
- https://leetcode.com/problemset/all
- https://www.codewars.com
- pyqgis
	- http://geospatialdesktop.com/2009/02/creating_a_standalone_gis_application_1/
- [Python @dataclasses](https://www.youtube.com/watch?v=vBH6GRJ1REM)
- [Python builtin functions](https://docs.python.org/3/library/functions.html)
- [Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://www.youtube.com/watch?v=oBt53YbR9Kk)
- [Git Guide (pt)](https://dev.to/leandronsp/pt-br-fundamentos-do-git-um-guia-completo-2djh)
- [Comparison Sorting Algorithms](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)