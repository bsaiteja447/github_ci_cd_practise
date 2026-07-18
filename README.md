# GitHub CI/CD Demo

## Step 1: Login to GitHub and create a repository
- Create a new GitHub repository.
- Do **not** initialize it with a README, .gitignore, or License.

## Step 2: Create README.md in PyCharm

Create a file named:

```text
README.md
```

## Step 3: Open the Terminal in PyCharm

Go to:

```text
View → Tool Windows → Terminal
```

## Step 4: Initialize Git Repository

```bash
git init
```

## Step 5: Add README.md to Git

```bash
git add README.md
```

Or add all files:

```bash
git add .
```

## Step 6: Commit Changes

```bash
git commit -m "first commit"
```

## Step 7: Configure Git (Only if not configured

```bash
git config --global user.name "bsaiteja447"
git config --global user.email "bsaiteja562@gmail.com"
```

## Step 8: Rename Branch to main

```bash
git branch -M main
```

## Step 9: Connect Local Repository to GitHub


```bash
git remote add origin https://github.com/bsaiteja447/github_ci_cd_practise
```

## Step 10: Push Code to GitHub

```bash
git push -u origin main
```

## Verify Remote Repository

```bash
git remote -v
```

## Check Repository Status

```bash
git status
```