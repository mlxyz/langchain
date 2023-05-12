# flake8: noqa

STRUCTURED_FORMAT_INSTRUCTIONS = """The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json
{{
{format}
}}
```"""

PYDANTIC_FORMAT_INSTRUCTIONS = """The output should be formatted as a JSON instance that conforms to the JSON schema below.

As an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}}}
the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Here is the output schema:
```
{schema}
```"""

GERMAN_PYDANTIC_FORMAT_INSTRUCTIONS = """Die Ausgabe muss als JSON-Instanz formatiert werden, die dem unten stehenden JSON-Schema entspricht. Die Ausgabe darf keinen normalen Text enthalten, sondern nur JSON im entsprechenden Schema.

Beispielsweise, für das Schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}
ist das Objekt {{"foo": ["bar", "baz"]}} eine korrekte Instanz des Schemas. Das Objekt {{"properties": {{"foo": ["bar", "baz"]}}}} ist nicht korrekt.

Hier ist das Ausgabe-Schema:
```
{schema}
```
"""