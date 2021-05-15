# PyPIDataBot by Tomodachi94
# (c) 2021 Tomodachi94, under the MIT License
# The license should have been distributed with this program.
# If not, the license can be found here:
# mit-license.org

import redis

class Parser:
    def __init__(self, r):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
