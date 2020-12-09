"""
Lab:

Create a class called "BuildTarget" that represents an object file we're building. Each build target has "Dependencies" which are other "BuildTarget" objects. When building a BuildTarget we should first build all of its dependencies.

Let's assume that to build a "BuildTarget" we just need to print its name.

This is a sample code that uses the new class:

```
main = BuildTarget("main")

common = BuildTarget("common")
ui = BuildTarget("ui")

gui = BuildTarget("gui")
cli = BuildTarget("cli")

ui.depends_on(gui, cli)
gui.depends_on(common)
main.depends_on(common, ui)

main.build()
# common, cli, gui, ui, main
```

The code should print out a list of each BuildTarget as it builds them, and make sure not to build any target multiple times and to build each target before building other targets that require it.
"""

class BuildTarget:
    def __init__(self, name):
        self.name = name
        self.dependencies = []
        self.built = False

    def depends_on(self, *modules):
        self.dependencies += modules

    def build(self):
        if self.built:
            return None

        for component in self.dependencies:
            component.build()
        print(self.name)

        self.built = True


if __name__ == '__main__':
    main = BuildTarget("main")

    common = BuildTarget("common")
    ui = BuildTarget("ui")

    gui = BuildTarget("gui")
    cli = BuildTarget("cli")

    ui.depends_on(gui, cli)
    gui.depends_on(common)
    main.depends_on(common, ui)

    main.build()
