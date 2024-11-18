# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <jayesh@ambhora.com>
# --------------------------------------------------------------------------------------------------

import mori.compiler
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


class http_server(http.server.HTTPServer):
    def __init__(self, root_path, *args, **kwargs):
        self.root_path = root_path
        super().__init__(*args, **kwargs)

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self, directory=self.root_path)


def serve(input_dir, compile_options, server_options):
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
    server_address = ("", params["port"])
    httpd = http_server(params["input_dir"], server_address, http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()
