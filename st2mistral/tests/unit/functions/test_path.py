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

from st2mistral.tests.unit import test_function_base as base

from yaql.language import factory
YAQL_ENGINE = factory.YaqlFactory().create()


class JinjaPathTestCase(base.JinjaFunctionTestCase):

    def test_basename(self):
        template = '{{ basename(_.k1) }}'
        result = self.eval_expression(
            template, {'k1': '/some/path/to/file.txt'})
        self.assertEqual(result, 'file.txt')

        result = self.eval_expression(template, {'k1': '/some/path/to/dir'})
        self.assertEqual(result, 'dir')

        result = self.eval_expression(template, {'k1': '/some/path/to/dir/'})
        self.assertEqual(result, 'dir')

    def test_dirname(self):
        template = '{{ dirname(_.k1) }}'
        result = self.eval_expression(
            template, {'k1': '/some/path/to/file.txt'})
        self.assertEqual(result, '/some/path/to')

        result = self.eval_expression(template, {'k1': '/some/path/to/dir'})
        self.assertEqual(result, '/some/path/to')

        result = self.eval_expression(template, {'k1': '/some/path/to/dir/'})
        self.assertEqual(result, '/some/path/to')


class YAQLPathTestCase(base.YaqlFunctionTestCase):

    def test_basename(self):
        expression = 'basename($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/file.txt'})
        )
        self.assertEqual(result, 'file.txt')

        expression = 'basename($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/dir'})
        )
        self.assertEqual(result, 'dir')

        expression = 'basename($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/dir/'})
        )
        self.assertEqual(result, 'dir')

    def test_dirname(self):
        expression = 'dirname($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/file.txt'})
        )
        self.assertEqual(result, '/some/path/to')

        expression = 'dirname($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/dir'})
        )
        self.assertEqual(result, '/some/path/to')

        expression = 'dirname($.k1)'
        result = YAQL_ENGINE(expression).evaluate(
            context=self.get_yaql_context({"k1": '/some/path/to/dir/'})
        )
        self.assertEqual(result, '/some/path/to')
