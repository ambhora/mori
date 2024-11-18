# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <jayesh@ambhora.com>
# --------------------------------------------------------------------------------------------------

import livereload
import socketserver
import http.server
import posixpath
import urllib


def serve_cli(dirinfo, cli_args):
    params = {
        "input_dir": cli_args.input_dir,
        "port": cli_args.port,
        "tmp": cli_args.tmp,
        "build": not cli_args.no_build,
    }

    serve(params)


class server_param:
    def __init__(self):
        self.input_dir = os.getcwd()


def serve(params):
    """
    Serve the project as a website:

    The function takes a mori project, builds it and servers it as a website. The function has
    an option to watch for changes, rebuild the project on the fly and force a reload in the
    browser to reflect the changes.

    Parameters
    ----------

    input_dir : str

        The input directory for the mori project.

    """

    server = livereload.Server()
    server.watch(params["input_dir"], livereload.shell('echo "index.html changed"'))
    server.serve(root=params["input_dir"], port=params["port"])


def log():
    print("Change detected")
