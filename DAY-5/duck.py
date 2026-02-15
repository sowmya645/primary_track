class pycharm:
    def execute(self):
        print("Compiling+running")
class vscode:
    def execute(self):
        print("running +lining")
def code(editor):
    editor.execute()
code(pycharm())
code(vscode())