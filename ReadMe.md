CycleColorSchemes is a plugin that lets you quickly switch between through your favorite color schemes in [Sublime Text 2](http://sublimetext.com/2) or [Sublime Text 3](http://sublimetext.com/3).

Cycle through color schemes with **Next in cycle (Ctrl-M)** and **Previous in cycle (Ctrl-Shift-M)**.

Set which color schemes are in the cycle with **Add current to cycle** and **Remove current from cycle**.  You can also manually edit the `cycled_color_schemes` preference.  For example, putting this in your settings file lets you toggle between Solarized light and dark:

    "cycled_color_schemes":
    [
        "Packages/Color Scheme - Default/Solarized (Light).tmTheme",
        "Packages/Color Scheme - Default/Solarized (Dark).tmTheme"
    ],
