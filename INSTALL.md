---
title: INSTALL
tags:
  - studies
use: Guideline, Community
---
# Obsidian Vault GitHub Repository Setup Guide

## Prerequisites
Before starting, ensure you have:
- [Obsidian](https://obsidian.md/) installed on your computer
- A [GitHub](https://github.com/) account
- [Git](https://git-scm.com/) installed on your system

## Step 1: Create Your Obsidian Vault
1. Open Obsidian
2. [Clone the repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
3. (Optionally) Uncomment and initialize the `.gitmodules`
4. Select the location on your computer

## Step 2: Daily Workflow
### Making Changes
1. Edit your notes in Obsidian as usual. Some configurations are default to improve compatibility with other platforms that doesn't use `[[]]` based links. Always try to create interconnected documents, to not leave orphans behind.
2. When ready to save changes to GitHub:
	```bash
	# Add all changes
	git add .
	
	# Commit with descriptive message
	git commit -sm "Add notes on [topic] and update [filename]"
	
	# Push to GitHub
	git push
	```
3. To merge the updates to the main repo and have your changes applied at the GH-Pages don't forget to open a PR.
### Pulling Changes (if working across multiple devices)
```bash
# Pull latest changes from GitHub
git pull origin main
```

## Repository Structure
Your final repository structure should look like:

```shell
drwxrwxrwx 0 see7e see7e   512 Jun 27  2025 .
drwxrwxrwx 0 see7e see7e   512 Oct 22  2024 ..
drwxrwxrwx 0 see7e see7e   512 Jun 27 09:20 .git
drwxrwxrwx 0 see7e see7e   512 Aug  1  2024 .github
-rwxrwxrwx 0 see7e see7e   276 Dec  5  2023 .gitignore
-rwxrwxrwx 0 see7e see7e  2313 Apr 14 08:31 .gitmodules
-rwxrwxrwx 0 see7e see7e  1728 Jun 27 09:35 CONTRIBUTING.md
drwxrwxrwx 0 see7e see7e   512 Oct 30  2023 Courses
-rwxrwxrwx 0 see7e see7e  2555 Jun 27 09:10 DIRECTORY.md
drwxrwxrwx 0 see7e see7e   512 Jun 27 09:09 Docs
-rwxrwxrwx 0 see7e see7e  2685 Jun 27  2025 INSTALL.md
-rwxrwxrwx 0 see7e see7e  1094 Aug 21  2023 LICENSE
drwxrwxrwx 0 see7e see7e   512 Mar 14 10:29 Languages
drwxrwxrwx 0 see7e see7e   512 Aug 21  2023 Programs
drwxrwxrwx 0 see7e see7e   512 Aug 31  2024 Projects
-rwxrwxrwx 0 see7e see7e  6469 Jun 27 09:35 README.md
-rwxrwxrwx 0 see7e see7e 23815 Aug  1  2024 links.md
drwxrwxrwx 0 see7e see7e   512 Aug  1  2024 src

```

## Best Practices
- **Commit frequently** with descriptive messages
- **Use folders** to organize different types of notes
- **Keep sensitive information** in a separate, private vault
- **Back up regularly** by pushing to GitHub
- **Use branches** for experimental note structures
- **Write good commit messages** describing what notes you added/modified

## Troubleshooting

### Common Issues
**Authentication Error:**
- Use personal access token instead of password
- Generate token at: GitHub → Settings → Developer settings → Personal access tokens

**Merge Conflicts:**
- Usually occur when editing same file on different devices
- Resolve manually or use `git mergetool`

**Large Files:**
- Git works best with text files
- Consider Git LFS for large attachments

