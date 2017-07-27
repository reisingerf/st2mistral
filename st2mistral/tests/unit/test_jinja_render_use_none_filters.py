# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from st2mistral.tests.unit import test_filter_base as base


class JinjaUseNoneFilterTestCase(base.JinjaFilterTestCase):

    def test_use_none(self):
        env = self.get_jinja_environment()

        template = '{{test_var | use_none}}'
        actual = env.from_string(template).render({'test_var': None})
        expected = '%*****__%NONE%__*****%'
        self.assertEqual(actual, expected)

        template = '{{test_var | use_none}}'
        actual = env.from_string(template).render({'test_var': 'foobar'})
        expected = 'foobar'
        self.assertEqual(actual, expected)
