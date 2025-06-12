# Changelog

All notable changes to this project will be documented in this file.

## 0.3.0

[9f37240](9f37240c41c3ce200a63356668745ca39e902064)...[244be5e](244be5e2f157d20dea55f906cb4b4f910ebb55a0)

### Bug Fixes

* [04fc620](04fc620ecb8c345112368130985a3e84d85ab7c2): Enclose command substitutions in quotes for improved output formatting 
* [e9a37dd](e9a37dda77e11f15205b29b41c13eedc9210bc9b): Remove LICENSE and README.md from .dockerignore 
* [244be5e](244be5e2f157d20dea55f906cb4b4f910ebb55a0): Update pre-commit hook command to use the correct flag for git-cliff 

### CI

* [6e2d746](6e2d746df33f1723dec766b8cf12a7e5bb9321b2): Add GitLab CI/CD configuration files for building and testing Docker images 
* [c9585b2](c9585b2b0b9a6ef34a8c1445331feadf30b41822): Add conditional rules for remote and project includes in CI configuration 
* [b28f84a](b28f84a1e7dc6d9b3a0dfc45812f6118207db9ac): Add GitHub actions workfloa configuration for building Docker images and validating scripts 

### Documentation

* [1bae805](1bae805e131959d352646a4a104c97b0037327e8): Add  README.md 

### Features

* [dbcd511](dbcd511459984d5f275056a78b9ce5ca29a8729b): Add Docker configuration files 
* [d4b04a4](d4b04a4063c924d825d676699a905fc72a4f7a42): Integrate .build.env environment file for Docker build 

### Miscellaneous Tasks

* [827009d](827009dc01f843abc7d87be0faaee5bdfc4be5ed): Update pre-commit hooks and add pydoclint configuration 
* [c798494](c798494d4bc97588cc8e34f3edf9b2d7034b8980): Reintroduce version bumping tasks in b2v.yml and update bumpversion files in pyproject.toml 

### Testing

* [c5088fe](c5088fe6b2cfee7b26fab105b5b11add1de69596): Add scripts for testing Docker containers and images 

## 0.2.0

### Features

* [72c302c](72c302c6a955eb064a9e83f8c8ddea69b764a59e): Add configuration generation functionality using Jinja2 and YAML 
* [2ee3e6a](2ee3e6af4bda80ccfa67a3013177d785fa441752): Add envconsul configuration and related scripts for Vault integration 

### Miscellaneous Tasks

* [9dbe5a2](9dbe5a2fce9a2a05cd43299f72bc1b56c87fe55a): Add Taskfile configuration for project automation 
* [188accd](188accd3cc779cc26f99b1ee1d4723936216cef7): Add initial configuration files for project setup 
* [70964cf](70964cf2363be8ab6343100415e97b4a73b0167c): Add pyproject.toml for project configuration and dependencies 
* [dc782f3](dc782f33f545e25befaf1fadecc11f1ba6aae40d): Add test configuration generation 
* [7d0c77f](7d0c77f6a97d41206ce4dc81e61f12d8e1b4311d): Add run task for executing pre-commit hooks 
* [15cd9cd](15cd9cd6dd8a15ceb33a3f8a64289b42331ce7fc): Update versioning tasks and configuration files 

### Other

* [afc4b68](afc4b688b9a8bf254f250b064869b5051d868fca): Initial commit 

====
