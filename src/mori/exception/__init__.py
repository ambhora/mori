# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <jayesh@ambhora.com>
# --------------------------------------------------------------------------------------------------

import enum


class ErrorComponent(enum.Enum):
    """Error components."""

    UNKNOWN = 0
    MORI = 1
    LIVERELOAD = 2


class Exception(Exception):
    def __init__(self, error_type, error_component, message):
        self.error_type = error_type
        self.error_component = error_component
        self.message = message
