#!/usr/bin/env python
from flask_script import Manager, Server
from SlqBlog import app

# from SlqBlog import create_app
# app = create_app(os.getenv('config') or 'default')

manager = Manager(app)

# exp: Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = 5000)
)

# null
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# exp: run app if not in import command
if __name__ == "__main__":
    manager.run()
