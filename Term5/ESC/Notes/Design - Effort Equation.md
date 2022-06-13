---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Software design]]

## 90-90 rule
> The first 90% of the code accounts for the first 90% of the development time.

> The remaining 10% of the code accounts for the other 90% of the development time.


## The Software Equation
$$
\dfrac{\left(B^{1/3} \times Size\right)}{Productivity} = Effort^{1/3} \times Time^{4/3}
$$
The models basis was formed through analysis of productivity data collected from over 4000 modern day software development projects.

The software equation can be used to show the non-linear correlation between time to complete the project and applied human effort.

### Effort
$$
Effort = \left[\dfrac{Size}{Productivity \times Time^{4/3}}\right]^3 \times B
$$
### Productivity
Research from the collected productivity data supplies initial values for productivity determined by the type of software being developed.

| Productivity value | Description                 |
| ------------------ | --------------------------- |
| 2000               | Real time embedded software |
| 10 000             | Telecommunication software  |
| 12 000             | Scientific software         |
| 28 000             | Business system applications                            |

### Size
Lines of code for the project

### B
Special skills factor. Related to size of product, scale of project.

| B Value | Size of Project |
| ------- | --------------- |
| 0.16    | 5-15K           |
| 0.18    | 20K             |
| 0.28    | 30K             |
| 0.34    | 40K             |
| 0.37    | 50K             |
| 0.39    | > 50K           |

## Time VS Effort
Inverse relationship.
![[Pasted image 20220520100201.png]]

| Cannot | ![[Pasted image 20220520100254.png]] |                                      |
| ------ | ------------------------------------ | ------------------------------------ |
| Can    | ![[Pasted image 20220520100320.png]] | ![[Pasted image 20220520100332.png]] | 

## Estimation of total efforts
A total effort of 10 roughly means that project requires one average developer to work on it in about 10 months, or 4 in 2.5 months.

However, consider there are communication overhead, synchronisation overhead, etc, more efforts are required than the calculation.
- So either more developers are required, or you need to become not-average
- or you need to reduce the size of code (good design) in order to reduce total effort

