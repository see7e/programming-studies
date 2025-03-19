---
title: Configuring a Bot for GH Actions
tags:
  - studies
  - programming
use: DevOps, GitHub, GitHub Actions
languages: Yaml
dependences: GitHub, GitHub Actions
---

# Intro

Lets say that you want to create an issue automatically in a (for example) Documentation repo:

```yaml
# Create issue in Documentation Repository
- name: Create Issue in Docs Repo
  id: doc_issue
  uses: dacbd/create-issue-action@v2.0.0
  with:
    token: ${{ secrets.GH_TOKEN_BOT }}  # Ensure this is a PAT with issue creation permissions
    owner: YOUR_ORG_OR_USERNAME
    repo: YOUR_DOCUMENTATION_REPO
    title: "[Docs] ${{ github.event.pull_request.title }}"
    body: |
      **Documentation Request from PR**: [#${{ github.event.pull_request.number }}](${{ github.event.pull_request.html_url }})
      **Author**: @${{ github.event.pull_request.user.login }}
      **Target Version**: ${{ steps.milestone2label.outputs.label }}

      ### PR Description:
      ${{ steps.get_pr_body.outputs.body }}

      ### Commits tagged with [needs-doc] or [FEATURE]:
      ${{ steps.filter_commits.outputs.commits }}
```

For that whe have the possibility to achieve that:
- Option 1: Using a Personal GitHub Account (not ideal for shared projects).
- Option 2: Creating a dedicated bot account (recommended for organizations).

Let's walk through the more structured path.

## Creating a dedicated Bot account

To create, configure, and set permissions for the **GitHub bot**, you need to follow these steps:


### 1. Create the account

1. Sign out of GitHub (if currently logged in).
2. Create a **new GitHub account** with a bot-like name (e.g., `your-repo-bot`).
3. Set an email (consider using `noreply` GitHub emails for privacy).
4. Verify the account through email.

> [!TIP]
> If this bot is for an organization, consider inviting it to your organization.


### 2. Generate a Personal Access Token (PAT)

The bot account needs a **Personal Access Token (PAT)** to authenticate API requests.

### How to Generate a PAT

1. Log in to the **bot account**.
2. Go to **Settings** → **Developer settings** → **Personal access tokens**.
3. Click **Generate new token (classic)**.
4. **Select scopes (permissions):**
   - `repo` → Full control of repositories (needed for PR and issue actions).
   - `public_repo` → (If the repository is public).
   - `issues` → Read/write permissions for creating issues.
   - `pull_requests` → Read/write permissions for commenting on PRs.
   - `contents` → Read access to repo content (if needed).
   - `workflow` → (If modifying GitHub Actions workflows).
5. Click **Generate Token** and **copy the token** (you won’t see it again!).


### 3. Add Bot's PAT as a Secret

The workflow will need access to this PAT.

### How to Add the Token to Repository Secrets

1. **Go to your repository** (or organization).
2. Click **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. Name it: `GH_TOKEN_BOT`.
5. Paste the **Personal Access Token (PAT)**.
6. Save.


### 4. Configure Bot's permissions in the repo

To ensure the bot has access, follow these steps:

#### For Personal Repositories

- If using a **personal repo**, the bot needs to be added as a **collaborator**:
  1. Go to **Settings** → **Manage Access**.
  2. Click **Invite a Collaborator**.
  3. Search for your bot (e.g., `your-repo-bot`).
  4. Select **Write access** (so it can comment, label, and create issues).

#### For Organizations

- If using a **GitHub Organization**, it’s better to create a **GitHub App** or **add the bot to the team**:
  1. **Invite the bot** to the organization.
  2. Assign it to a team that has **write** access to repositories.


### 5. Test

To verify everything is set up correctly:
1. Manually run the **GitHub Actions workflow**.
2. Check if configured actions taken by the bot.

If something goes wrong:
- **Check GitHub Actions logs** (Under "Actions" → Click on a failed job).
- **Check token permissions** (Did you add `repo`, `issues`, and `pull_requests` scopes?).


> [!WARNING]
> Is also important to have some security considerations about how the token is called inside of the workflow.

## Security Considerations

There's a security measure where the GitHub Actions workflow does **not** use a sensitive token with write permissions for certain operations.

### How Does This Affect the Explanation Above?

In the explanation above, we set up a **Personal Access Token (PAT)** (`GH_TOKEN_BOT`) as a **GitHub Secret**, which means:
- The token is **not visible in logs**.
- It is **stored securely**.
- The bot **has full control (write permissions)** to repositories where it is given access.

However, **if the workflow uses a clear (publicly visible) token**, such as `GITHUB_TOKEN` (the built-in GitHub Actions token), it has **limited permissions**:
- It **can read and comment on issues and PRs**.
- It **CANNOT create issues in a different repository**.
- It **CANNOT trigger workflows in another repo** (due to GitHub’s security restrictions).

This means:
✅ **The bot can comment on PRs safely.**  
❌ **The bot cannot create issues in another repository unless using a properly scoped PAT.**  

### Implications on the Explanation Above

1. **If the bot should only comment on PRs** → No changes are needed, and using `GITHUB_TOKEN` is safe.
2. **If the bot must create issues in another repository** → You must still use a **PAT stored as a secret** (as explained earlier).
3. **If security is a concern** → Consider using a **GitHub App** instead of a PAT, as it has finer permission control.


### How to Check If a Workflow Exposes the Token Instead of Using a Secret

#### Look for `secrets.GH_TOKEN_BOT` vs `GITHUB_TOKEN`

- **Secure Usage (Uses Secrets)**
  ```yaml
  token: ${{ secrets.GH_TOKEN_BOT }}
  ```
  - The token is stored **securely**.
  - It has **explicitly defined permissions**.

- **Insecure Usage (Exposes a Token)**
  ```yaml
  token: ${{ github.token }}
  ```
  - This uses `GITHUB_TOKEN`, which is **generated by GitHub automatically**.
  - **Limited permissions** (CANNOT create issues in another repo).
  - Cannot be used across repositories.

#### Check if the Token appears in the logs 
- If the workflow logs show:
  ```
  token=ghp_ABC123456789...
  ```
  - The token **is exposed**, meaning it was **not** properly stored as a secret.

- If logs show something like:
  ```
  token=***
  ```
  - The token **is hidden**, meaning it **was stored as a secret**.

#### Look for Direct Token Hardcoding in the Yaml files

- **Secure Workflow Example:**
  ```yaml
  token: ${{ secrets.GH_TOKEN_BOT }}
  ```
  - The token is securely stored and **not visible** in logs.

- **Insecure Workflow Example:**
  ```yaml
  token: ghp_ABC123456789...
  ```
  - The token is **hardcoded** in the YAML file.
  - **Anyone with repo access can see and steal the token!**
  - If exposed in a **public repo**, attackers could use it for malicious purposes.

> [!TIP]
> There's also some workflows that checks the commiting of secrets/tokens.


### Pros and Cons of Using a "Clear" (Non-Secret) Token

| **Method**            | **Pros** | **Cons** |
|-----------------------|---------|---------|
| **`GITHUB_TOKEN` (default)** | ✅ No extra setup needed <br> ✅ Safe for internal repo actions (commenting, labeling, etc.) | ❌ Cannot create issues in another repo <br> ❌ Cannot trigger workflows in another repo |
| **PAT stored as a Secret (`GH_TOKEN_BOT`)** | ✅ Can perform cross-repo actions <br> ✅ Can create issues in another repo <br> ✅ More control over permissions | ❌ Requires setting up a GitHub Secret <br> ❌ If mishandled, it could be exposed |
| **Hardcoded Token in YAML** | ❌ NEVER DO THIS | ❌ Exposes credentials <br> ❌ Security risk if leaked <br> ❌ Can be used by attackers |


### Best Practice Recommendation

- If the bot **only needs to comment on PRs**, use `GITHUB_TOKEN`.  
- If the bot **needs to create issues in another repo**, use a **PAT stored as a secret (`GH_TOKEN_BOT`)**.  
- **Never hardcode tokens in YAML files.**

