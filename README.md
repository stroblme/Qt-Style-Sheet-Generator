# Style Sheet Generator

## Description

This software generates a QT style sheet based on the following two software components:
- Paletton (https://paletton.com/)
- Breeze Style Sheet (https://github.com/Alexhuszagh/BreezeStyleSheets)

From Paletton, you can define a 3-color based template and export it as a .txt file.
This then can be merged either with one of the by SSG provided templates:
- dark.template
- light.template

Last but not least, you have to specify an output directory, where your custom QSS file will be written to.

This file then can be used for creating a QT conform asset.

## Workflow

A workflow like the following one is suggested but ofcourse not enforced:

1. Create two Palettes (dark and light theme) on Paletton
2. Run SSG
3. Check if the theme fitts your application
4. Start improving your theme by repitively changing the color palette.
5. If things don't look as expected, try to manipulate the template files

Note, that creating a single palette and running both template files on this palettes, might give unwanted results, as the color shades are not distributed linearily.

## Tips and Tricks

For a faster development, it's a good idea to tell your IDE to run SSG before starting the application. This will ensure, that you're always using the latest style sheet and lets you test your new palette instantly.
See the command line arguments for further details on how to do this.

## Help

```
usage: ssg.py [-h] [-p PALETTE] [-t TEMPLATE] [-o OUTPUT]

Register Converter Script

optional arguments:
  -h, --help            show this help message and exit
  -p PALETTE, --palette PALETTE
                        Your color palette
  -t TEMPLATE, --template TEMPLATE
                        Template file
  -o OUTPUT, --output OUTPUT
                        Output file
```