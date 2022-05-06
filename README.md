# Notion PDF
A tool that you can choose either <code>[weasyprint](https://github.com/Kozea/WeasyPrint)</code> or <code>chromedriver(save as pdf)</code> to convert Notion exported html files to pdf files.

# Download

[Donwload for Windows](https://github.com/noworneverev/notion-pdf/releases/download/v1.0.0/notion-pdf.rar)

# Usage
1. Download the [binary]() and unzip it.
2. Export Notion pages as HTML files and unzip the exported file.

![](https://imgur.com/8RGx2rI.jpg)

3. Put the unzipped folder (which should contains all html files) inside the main.exe folder.
![](https://imgur.com/z2RJMet.jpg)

4. Run <code>main.exe</code>
     1. The default mode is based on [weasyprint](https://github.com/Kozea/WeasyPrint). It will be a bit slower than the other mode, but the output pdfs are fairly good from my point of view. Because weasyprint could automatically create bookmarks associated with headers, I set this mode as default mode. **Just double click the <code>main.exe</code> and wait**.
     2. The other mode is based on chromedriver, in this case <code>driver/chromedriver.exe</code> is necessary when execute the main.exe. Open command line, cd to main.exe's directory, and then run <code>main.exe -c</code>.
    ![](https://imgur.com/1tU9awa.jpg)
    ![](https://imgur.com/P7dNe6p.jpg)


# Credits
## weasyprint
The default mode use [weasyprint](https://github.com/Kozea/WeasyPrint) to convert html file to pdf. It's an awesome package written fully based on Python. 
## chromedriver
The other mode use [chromedriver](https://chromedriver.chromium.org/) to save html files as pdfs.

# Todo
- [ ] Preserve directory hierarchy
- [ ] Implement link to block in exported pdfs
- [ ] Combin all subpages to one single pdf