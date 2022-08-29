# LightSSTICheck.py

LightSSTICheck is a tool designed to find basic SSTI vulnerabilities in a list of urls

## Install:
```bash
$ git clone https://github.com/mathis2001/LightSSTICheck
```

## Usage:
```bash
$ cat urls.txt | python3 LightSSTICheck.py [--get] [--post]

or with an other tool like waybackurls

$ waybackurls exemple.com | python3 LightSSTICheck.py [--get] [--post]
```
## Screenshots

![tempsnip](https://user-images.githubusercontent.com/40497633/186141880-771d40a6-cbcb-4969-bc10-5b8a60821222.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/186141632-fb47fb35-3519-412e-87cb-f2e17d0692fd.png)
