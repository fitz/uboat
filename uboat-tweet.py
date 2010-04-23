#!/usr/bin/env python
#
# uboat-tweet.py --- post uboat death messages to Twitter
#
# Author: Brian W. Fitzpatrick <fitz@red-bean.com>
# Created: 2010-04-23
#
# Copyright 2010 Brian W. Fitzpatrick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from uboat import Uboat
import twitter

username = 'ironcoffins'
password = ''

if __name__ == '__main__':

  msg = Uboat().death_message()
  api = twitter.Api(username, password)
  status = api.PostUpdate(msg)
  print status.text


