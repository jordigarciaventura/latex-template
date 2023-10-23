# LaTeX Template
LaTeX template and workflow recommendations (see [example.pdf](./template/example.pdf))

> Keep your project locally, with source control and without limitations. 


I use [Docker](https://www.docker.com/) in order to have all the LaTeX dependencies (e.g. TeX Live, Java, Perl, Python) packaged and controlled, so you can remove them whenever you want.

Then I use [Visual Studio Code](https://code.visualstudio.com/) with the [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension to edit, compile and visualize the document.

Finally, I use [Zotero](https://www.zotero.org/) to track my bibliograph. You can synchronize it with the project using the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) add-on and  inside vscode using the [Zotero LaTeX](https://marketplace.visualstudio.com/items?itemName=bnavetta.zoterolatex) extension. 

I recommend to use some grammar checking extension like [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

## Requirements
- Docker (running)
- Visual Studio Code
- ~5GB disk space for latex image
- Zotero (optional)

## Installation

You can use both methods because they use the same LaTeX image (no extra space needed) and none of them is perfect (check their drawbacks).

### First method (devcontainers)
> Drawbacks: slower startup, [Zotero LaTeX](https://marketplace.visualstudio.com/items?itemName=bnavetta.zoterolatex) extension doesn't work.
1. Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
2. Open the [template/](./template/) directory in vscode and use the `Reopen in Container` option (it will take some minutes).
### Second method (manual)
> Drawbacks: can't build individual files, just the whole project.
1. Open the project with Visual Studio Code and install the recommended extensions. See details below:
     - [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
     - [Zotero LaTeX](https://marketplace.visualstudio.com/items?itemName=bnavetta.zoterolatex) (optional)
2. (Optional) You can install [Zotero](https://www.zotero.org/) and the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) add-on in order to use the [Zotero LaTeX](https://marketplace.visualstudio.com/items?itemName=bnavetta.zoterolatex) vscode extension (follow the extension page instructions).

## First run

> If using the second method, the first run will install the docker image that contains all the LaTeX dependencies and will last for some minutes. 

1. Try to build the [main.tex](./template/main.tex) file from the toolbar (upper right) or from the extension settings (Ctrl+Alt+X).
2. The process should success and you should be able to preview the document with the extension options or manually (see out/main.pdf).


## Template guide
```
.
├── .vscode/
│   ├── extensions.json     Recommended extensions
│   └── settings.json       Extension settings
└── template/
    ├── examples/           Code snippets
    ├── media/              Media folder for images, tables, etc.
    ├── out/                Output files (cache files and pdf result)
    ├── packages/           My custom packages
    ├── sections/           Split the project in subfiles (e.g. by section)
    ├── abstract.tex        Abstract
    ├── appendix.tex        Appendix
    ├── bibliography.bib    Bibliography in BibLaTeX format
    ├── glossaries.tex      Special terms and acronyms
    ├── main.tex            Root file
    ├── preamble.sty        All dependencies and configurations
    └── title.tex           Title
```

- Check the [examples](./template/examples) directory to begin.
- The root file that references the rest of the files is the [main.tex](./template/main.tex) file.
  - Select just one language (English or Spanish)
  - Uncomment/Comment the appropriate lines according to your needs.
  - Add more sections using `\subfile{}` .
- If you want to add packages use the [preamble.tex](./template/main.tex) file.
- The "Build" button depends on the current active file in the editor. It means that you can build separate sections without the need of building the whole project (only working in devcontainer).
- There are two preconfigured builds recipes:
  - Fast (default): there can be minor problems (missing references, glossaries and bibliography).
  - Complete: for the final delivery (all should work).

## Recommendations
- Create the tables in an external app (e.g. Google Sheets) and then use a table editor (e.g. [LaTeX Tables Editor](https://www.latex-tables.com/)) to convert them into LaTeX (the "File>Import Table>Paste a table" option works well).
- Save the tables in separate files and then include them using `\input{}` (see [tables.tex](./template/examples/tables.tex)).
- Create the equations in an external equation editor.
- Use scalable formats like PDF for media (e.g. diagrams made with [draw.io](https://www.drawio.com/)) because it is scalable (you can make infinite zoom).
- Debug build errors:
  - Check the "Problems" vscode panel.
  - Check the LaTeX Workshop output in the "Output" vscode panel.
  - Try the "Complete" build recipe if the "Fast" doesn't complete successfully.
  - Delete the `/out` directory to make a fresh build.
  - Try to build some sections separately (comment the rest out).
  - If you have added new packages, check for compatibility issues or take into account that the order in which you import the packages matter.

## Websites and tools
- [Overleaf](https://www.overleaf.com/project)
- [Match.io](https://www.mathcha.io/editor)
- [Mathpix](https://mathpix.com/)
- [Detexify](http://detexify.kirelabs.org/classify.html)
- [LaTeX Tables Editor](https://www.latex-tables.com/)
- [LaTeX Equation Editor](https://www.latex4technics.com/)
- [draw.io](https://www.drawio.com/)