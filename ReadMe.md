CycleColorSchemes is a plugin that lets you quickly switch between through your favorite color schemes in [Sublime Text 2](http://sublimetext.com/2) or [Sublime Text 3](http://sublimetext.com/3).

Edit the `cycled_color_schemes` preference to tell the plugin which schemes you want to cycle through.  (You can also use **Add current to cycle** and **Remove current from cycle** in the command palette.)  For example, putting this in your settings file lets you toggle between Solarized light and dark:

    "cycled_color_schemes":
    [
        "Packages/User/Solarized (Modified Light).tmTheme",
        "Packages/Color Scheme - Default/Solarized (Dark).tmTheme"
    ],

After defining your color schemes, you can cycle through them with **Next in cycle (Ctrl-M)** and **Previous in cycle (Ctrl-Shift-M)**.
