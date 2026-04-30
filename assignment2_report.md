# Assignment 2: Static Personal Blog Website Report

**Student Name**: Dai Kaixuan  
**Student ID**: ZY2557202  

## 1. Project Overview

This assignment focuses on building and deploying a static personal website. The website is used to present my course assignment work, especially Assignment 1, which includes command line practice, Markdown documentation, matrix multiplication implementation, and correctness verification.

The final website is deployed through GitHub Pages and can be accessed through a public URL.

Website URL:

```text
https://cinnamon-17.github.io/remote-dev-blog/
```

## 2. Tool Choice

I chose to build the website using simple HTML and CSS instead of a more complex framework.

The main reasons are:

- The assignment only requires a static website.
- HTML and CSS are simple, stable, and easy to deploy.
- GitHub Pages can directly host static HTML files.
- This approach avoids unnecessary framework configuration and focuses on the core requirements of the assignment.

The main files used for the website are:

```text
index.html
assignment1/report.md
assignment1/report.html
assignment1/report.pdf
assignment1/matrix_mul.py
assignment1/matrix_mul.c
```

## 3. Website Structure

The website contains a homepage and links to Assignment 1 materials.

The homepage is implemented in:

```text
index.html
```

The homepage includes links to:

- Assignment 1 HTML report
- Assignment 1 PDF report
- Assignment 1 Markdown report
- Python source code
- C source code

This satisfies the requirement of integrating previous work into the personal website.

## 4. Git Version Control Process

The project was managed using Git from the beginning. I initialized a local Git repository and made several meaningful commits during development.

The main Git workflow was:

```bash
git init
git add .
git commit -m "Initial project structure"
```

Then I continued committing after completing each major step, such as adding the Python implementation, adding system information, writing the report, adding the C implementation, generating the PDF version, and creating the website homepage.

Examples of meaningful commits include:

```text
Initial project structure
Add Python matrix multiplication implementation
Add system configuration to report
Add Python verification result
Document Python implementation and verification
Add C implementation and finalize assignment 1 report
Add HTML and PDF versions of assignment 1 report
Create static website homepage
Disable Jekyll processing for GitHub Pages
```

Each commit reflects a clear development step rather than random or unnecessary changes.

## 5. Deployment Process

The website was deployed using GitHub Pages.

First, I created a GitHub repository named:

```text
remote-dev-blog
```

Then I connected the local repository to the remote GitHub repository using SSH:

```bash
git remote set-url origin git@github.com:Cinnamon-17/remote-dev-blog.git
git push -u origin main
```

After pushing the files to GitHub, I enabled GitHub Pages in the repository settings:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```

Since `index.html` is located in the root directory, GitHub Pages can directly use it as the website homepage.

## 6. Integration of Assignment 1

Assignment 1 was integrated into the website by placing its report files and source code under the `assignment1/` directory.

The website provides direct links to:

```text
assignment1/report.html
assignment1/report.pdf
assignment1/report.md
assignment1/matrix_mul.py
assignment1/matrix_mul.c
```

This allows visitors to view the documentation, download the PDF report, and inspect the source code.

## 7. Conclusion

Through this assignment, I practiced building a simple static website, managing the project with Git, publishing files through GitHub, and deploying a public website using GitHub Pages.

This project also connects Assignment 1 and Assignment 2 together: Assignment 1 provides the technical content, while Assignment 2 provides the public website used to present and submit that content.

